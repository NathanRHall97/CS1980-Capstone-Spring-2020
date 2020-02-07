#!/usr/bin/env python
from flask import Flask
import requests
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_index():
    return 'You have reached the API-Gateway index page'

@app.route('/pet', methods=['post'])
def update_pet(body,):
    microservice_response = requests.post("http://172.16.238.6:8080/pet",
        body,
    )
    return microservice_response.content
@app.route('/pet', methods=['get'])
def update_pets():
    microservice_response = requests.get("http://172.16.238.6:8080/pet",
        
    )
    return microservice_response.content
@app.route('/pet/{petId}', methods=['get'])
def find_by_id(petId,):
    microservice_response = requests.get("http://172.16.238.6:8080/pet/{petId}",
        petId,
    )
    return microservice_response.content
@app.route('/ui', methods=['get'])
def ui():
    microservice_response = requests.get("http://172.16.238.7:8080/ui",
        
    )
    return microservice_response.content
@app.route('/ui-yaml', methods=['get'])
def ui_yaml():
    microservice_response = requests.get("http://172.16.238.7:8080/ui-yaml",
        
    )
    return microservice_response.content
@app.route('/user', methods=['post'])
def register_customer(body,):
    microservice_response = requests.post("http://172.16.238.8:8080/user",
        body,
    )
    return microservice_response.content
@app.route('/user', methods=['get'])
def get():
    microservice_response = requests.get("http://172.16.238.8:8080/user",
        
    )
    return microservice_response.content
@app.route('/user/{customerId}', methods=['get'])
def get_user(customerId,):
    microservice_response = requests.get("http://172.16.238.8:8080/user/{customerId}",
        customerId,
    )
    return microservice_response.content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)