#!/usr/bin/env python
from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_index():
    return 'You have reached the API-Gateway index page'


@app.route('/ui', methods=['get'])
def ui():
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.5:8080/ui".format(), data=content)
    return microservice_response.content
@app.route('/ui-yaml', methods=['get'])
def ui_yaml():
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.5:8080/ui-yaml".format(), data=content)
    return microservice_response.content
@app.route('/user', methods=['post'])
def register_customer():
    content = request.get_json()
    microservice_response = requests.post("http://172.16.238.7:8080/user".format(), data=content)
    return microservice_response.content
@app.route('/user', methods=['get'])
def get():
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.7:8080/user".format(), data=content)
    return microservice_response.content
@app.route('/user/<customerId>', methods=['get'])
def get_user(customerId):
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.7:8080/user/{}".format(customerId), data=content)
    return microservice_response.content
@app.route('/pet', methods=['post'])
def update_pet():
    content = request.get_json()
    microservice_response = requests.post("http://172.16.238.8:8080/pet".format(), data=content)
    return microservice_response.content
@app.route('/pet', methods=['get'])
def update_pets():
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.8:8080/pet".format(), data=content)
    return microservice_response.content
@app.route('/pet/<petId>', methods=['get'])
def find_by_id(petId):
    content = request.get_json()
    microservice_response = requests.get("http://172.16.238.8:8080/pet/{}".format(petId), data=content)
    return microservice_response.content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)