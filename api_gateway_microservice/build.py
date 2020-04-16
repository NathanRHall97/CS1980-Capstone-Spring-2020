#!/usr/bin/env python
from os import path, walk
from master_yaml import MasterYaml, yaml_to_dict, merge_dicts
from yaml import dump
from pystache_engine import PystacheEngine
from sys import exit
import yaml
import os

# INPUT FILE PATHS
MICROSERVICE_IP_ADDRESS = 'ip_address.json'
BASE_API_FILE = 'config/api.yaml'
BASE_DOCKERCOMPOSE = 'config/dockercompose.yaml'
MUSTACHE = "microservices/api_gateway/templates/gateway.mustache"
DB_MUSTACHE = 'database/Templates/PYSQL.mustache'
BASH_MUSTACHE = 'database/Templates/Bash.mustache'
SQL_MUSTACHE = 'database/Templates/SQL.mustache'

# OUTPUT FILE PATHS
OUTPUT_API = 'api_gateway.yaml'
SWAGGER_MICROSERVICE_DIR = 'microservices/ui/'
OUTPUT_GATEWAY = 'microservices/api_gateway/api_gateway.py'
OUTPUT_SQL = './SQLFiles/'
OUTPUT_PYSQL = './'
OUTPUT_BASH = 'dbsetup'
OUTPUT_WIN_BASH = 'database/Scripts/Windows_dbsetup'
OUTPUT_TEST_FILE = '/test/test.py'

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

#Returns a dynamic IP for the database service
#Gets the last microservice off the dict, reads the ip, adds one to it, and returns that ip for the db ip
def get_db_ip(microservice_ip_dict):
    last_item = microservice_ip_dict.popitem()
    last_ip = list(last_item[1])
    ip_to_add = int(last_ip[-1])
    ip_to_add += 1
    ip_to_place = str(ip_to_add)
    last_ip[-1] = ip_to_place
    return_ip = ''.join(last_ip)
    microservice_ip_dict[last_item[0]] = last_item[1]
    return return_ip


def assign_test_ips(ip_dict):
    api_ip = ip_dict['api_gateway']
    pet_ip = ip_dict['pet']
    user_ip = ip_dict['user']
    test_file = open('./microservices/test/test.py', "a")
    test_file.write('\n')
    test_file.write('api_ip = \'' + api_ip + '\'')
    test_file.write('\n')
    test_file.write('pet_ip = \'' + pet_ip + '\'')
    test_file.write('\n')
    test_file.write('user_ip = \'' + user_ip + '\'')
    test_file.close()

# Takes a dict of microservice: IP address and a dict of docker-compose info and builds a new docker-compose.yaml
def make_dockercompose_file(microservices_dict, compose_dict):
    compose_dict.add('services', dict())
    for name, ip_address in microservices_dict.items():
        path = MICROSERVICES_DIR + name
        new_microservice = {name: {"build": {'context': path, 'dockerfile': 'Dockerfile' }, "networks": {"my_network": {"ipv4_address": ip_address}}}}
        if(name == GATEWAY_NAME):
            new_microservice[name]['ports'] = [(DEFAULT_PORT+':'+DEFAULT_PORT)] # api gateway listens on 8080
        compose_dict.add('services', new_microservice)

    # Database service written in
    new_dict = microservices_dict
    #print(microservices_dict)
    db_ip = get_db_ip(new_dict)
    assign_test_ips(microservices_dict)
    database_service = {"db_server": {'image': "postgres", 'container_name': "my_postgres", "networks": {"my_network": {"ipv4_address": db_ip}}, "ports": [("54320:5432")], "environment":{"POSTGRES_PASSWORD": "postgres", "POSTGRES_USER":"postgres"}, "volumes":[("my_dbdata:/var/lib/postgresql/data")]}}
    compose_dict.add('services', database_service)

    compose_dict.write_me_to_file('docker-compose.yaml')

#Uses a psytache template to create the python-init file
def make_pysql(service):
    my_dict = {'val': service.lower()}
    pysql_engine = PystacheEngine()
    pysql_engine.load_dict(my_dict)
    pysql_engine.render_write(DB_MUSTACHE, OUTPUT_PYSQL+service.lower()+"-init.py")

#Uses a psytache template to create the bash file
def make_bash(list_of_keys):
    #Convert our list to a dictionary of keys to use with pystache engine
    db_dict = dict()
    db_dict = {'services':list_of_keys}
    #print(db_dict)
    bash_engine = PystacheEngine()
    bash_engine.load_dict(db_dict)
    bash_engine.render_write(BASH_MUSTACHE, OUTPUT_BASH)

def make_SQL(service, list_of_attributes):
    db_dict = dict()
    db_dict = {'service': service.lower(), 'attributes': list_of_attributes}
    #print(db_dict)
    SQL_Engine = PystacheEngine()
    SQL_Engine.load_dict(db_dict)
    SQL_Engine.render_write(SQL_MUSTACHE, OUTPUT_SQL+service.lower()+"-init.sql")


def make_db_files(get_yaml_file):
    #Load yaml file
    with open(get_yaml_file) as file:
        info = yaml.full_load(file)
        for item, inf in info.items():
            #Microservice needs a DB
            if item == 'definitions':
                list_of_keys = list(inf.keys())
                for i in range(len(list_of_keys)):
                    service = list_of_keys[i]
                    #create a dictionary of details/type/..
                    dict_to_use = inf[service]['properties']
                    list_of_attributes = []
                    #Create key, type pairs and insert them into a list
                    for x, dict in dict_to_use.items():
                        ks = list(dict_to_use.keys())
                        temp = {}
                        temp['key'] = x
                        #Since were creating an SQL file string -> varchar(20)
                        if dict['type'] == 'string':
                            #if its not the last value, we use a comma
                            if x != ks[-1]:
                                temp['type'] = 'varchar(20)'
                                temp['comma'] = ','
                                list_of_attributes.append(temp)
                            #last value, dont add a comma into the dict so that SQL parses correctly
                            else:
                                temp['type'] = 'varchar(20)'
                                list_of_attributes.append(temp)
                        else:
                            if x != ks[-1]:
                                temp['type'] = dict['type']
                                temp['comma'] = ','
                                # check to see if its id, if so make it primary key
                                if x == 'id':
                                    temp['pk'] = 'PRIMARY KEY'
                                list_of_attributes.append(temp)
                            else:
                                temp['type'] = dict['type']
                                if x == 'id':
                                    temp['pk'] = 'PRIMARY KEY'
                                list_of_attributes.append(temp)

                    #Create .SQL Files
                    make_SQL(service, list_of_attributes)

                    #Create Python Files to execute SQL Files
                    make_pysql(service)

                #Create Bash Script for easy Database Initialization
                #simple loop to make all keys lowercase
                for key in range(len(list_of_keys)):
                    k = list_of_keys[key]
                    list_of_keys[key] = k.lower()
                make_bash(list_of_keys)


#Gets the individual microservice test file passed in, appends it to the test container and returns
def write_into_test(microservice_test):
    reader = open(microservice_test, "r")
    #print(reader.read())
    test_file = open('../../test/test.py', "a")
    test_file.write('\n')
    test_file.write(reader.read())
    test_file.close()
    reader.close()

def make_master_test_file():
    #print(os.getcwd())
    #Go into microservices
    os.chdir('microservices')

    #loop through each service in microservices
    for service in os.listdir():
        #Go into the microservice directory
        os.chdir(service)

        #loop through files in the directory
        for d in os.listdir():
            #check for test directory
            if d == 'test':
                os.chdir('test')

                #List the test directory and write the test files
                for test_file in os.listdir():
                    cwd = os.getcwd()
                    test_ = cwd + '/' + test_file
                    write_into_test(test_)
                os.chdir('..')
        os.chdir('..')

    #Leave Microservice Directory and return function.
    os.chdir('..')



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

    make_db_files(OUTPUT_API)
    make_master_test_file()




if __name__== '__main__':
    main()
    Cool_function()