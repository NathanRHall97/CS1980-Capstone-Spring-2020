#!/usr/bin/env python
from os import path, walk
from master_yaml import MasterYaml, yaml_to_dict, merge_dicts
from yaml import dump
from pystache_engine import PystacheEngine
from sys import exit

# INPUT FILE PATHS
MICROSERVICE_IP_ADDRESS = 'ip_address.json'
BASE_API_FILE = 'config/api.yaml'
BASE_DOCKERCOMPOSE = 'config/dockercompose.yaml'
MUSTACHE = "microservices/api_gateway/templates/gateway.mustache"

# OUTPUT FILE PATHS
OUTPUT_API = 'api_gateway.yaml'
SWAGGER_MICROSERVICE_DIR = 'microservices/ui/'
OUTPUT_GATEWAY = 'microservices/api_gateway/api_gateway.py'

# MIRCROSERVICES DIRECTORY
MICROSERVICES_DIR = 'microservices/'

# API GATEWAY
GATEWAY_NAME = 'api_gateway'
DEFAULT_PORT = "8080"

# IP/SUBNET MASK
DEFAULT_IP_AND_SUBNET = '172.16.238.0/24'
ALLOWABLE_SUBNET_MASK = '24'
NUM_VALUES_ONE_BYTE = 255

#  Searches all directories and returns a dict with key,value pairs of microservice, file path to api yaml
def get_api_yaml_paths(directory):
    dict_api_yamls = dict()
    for root, dirs, files in walk(directory):
        for file in files:
            file_path = path.join(root, file)
            if file == 'api_doc.yaml' or file == 'api_doc.yml':
                dict_api_yamls[root] = file_path
    return dict_api_yamls


# Verifies the subnet mask is 0/24. Currently we do not support others 
def get_subnet_range(sub_mask):
    if(sub_mask == ALLOWABLE_SUBNET_MASK):
        return NUM_VALUES_ONE_BYTE
    else:
        print("ERROR: We do not currently allow subnet masks other than '0/24'")
        exit(1)

#  Searches given directory for subdirectories and returns a list
def get_microservices(microservice_path_dir):
    for root, dirs, files in walk(microservice_path_dir):
        if(root == microservice_path_dir):
            return dirs

# Generator that assigns unique IP addresses based on global constants
def get_ip_generator(ip, subnet_range):
    for i in range(5, subnet_range):
        new_ip = ip + str(i)
        yield new_ip

# Traverses all microservices and assigns a unique IP to each
def assign_ip_microservices(gen,  microservices_list):
    microservice_IPs = dict() # assign microservice IPs
    for microservice in microservices_list:
        microservice_IPs[microservice] = next(gen) # assign unique IP to each
    return microservice_IPs

# Assigns a microservice a unique IP
def assign_IPs(ip_gen, list_microservices):
    ip_adds = dict()
    for microservice in list_microservices:
        ip_adds[microservice] = next(ip_gen) # assign unique IP to each
    return ip_adds

# Takes a dict of microservice: IP address and a dict of docker-compose info and builds a new docker-compose.yaml
def make_dockercompose_file(microservices_dict, compose_dict):
    compose_dict.add('services', dict())
    for name, ip_address in microservices_dict.items():
        path = MICROSERVICES_DIR + name
        new_microservice = {name: {"build": {'context': path, 'dockerfile': 'Dockerfile' }, "networks": {"my_network": {"ipv4_address": ip_address}}}}
        if(name == GATEWAY_NAME):
            new_microservice[name]['ports'] = [(DEFAULT_PORT+':'+DEFAULT_PORT)] # api gateway listens on 8080
        compose_dict.add('services', new_microservice)
    compose_dict.write_me_to_file('docker-compose.yaml')


# Main application logic
def main():
    # Load base API
    api = MasterYaml(BASE_API_FILE)
    # Append microservice API data
    api_paths = get_api_yaml_paths(MICROSERVICES_DIR) # search files in the current directory and all sub-directories for api_doc.yaml paths
    for microservice_dir, yaml_path in api_paths.items():
        api.append_yaml(yaml_path)
    api.append_yaml(BASE_API_FILE)
    api.write_me_to_file(OUTPUT_API)
    api.write_me_to_file(SWAGGER_MICROSERVICE_DIR+OUTPUT_API)

    # Gather microservice APIs/IP address/subnet range
    docker_compose = MasterYaml(BASE_DOCKERCOMPOSE)
    config_elements = docker_compose.get('networks').get('my_network').get('ipam').get('config')
    for item in config_elements:
        ip_add, sub_mask = item.get('subnet', DEFAULT_IP_AND_SUBNET).split('/')
        ip_add = ip_add.strip('0')
    subnet = get_subnet_range(sub_mask)

    # Assign IPs
    microservice_ip_dict = assign_IPs(get_ip_generator(ip_add, subnet), get_microservices(MICROSERVICES_DIR))
    
    # Make docker-compose.yaml file
    docker_compose = MasterYaml(BASE_DOCKERCOMPOSE)
    make_dockercompose_file(microservice_ip_dict, docker_compose)

    # Generate server code
    pyeng = PystacheEngine()
    pyeng.convert_yamls_pystache(api_paths, microservice_ip_dict, {'port': ':'+DEFAULT_PORT})
    pyeng.render_write(MUSTACHE, OUTPUT_GATEWAY)

if __name__== '__main__':
    main()