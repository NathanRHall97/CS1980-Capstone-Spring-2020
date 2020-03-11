import requests
import pytest
import json
import time

# Invoking this fixture: 'function_scoped_container_getter' starts all services
time.sleep(3)
def test_get_ui():
    url = "http://172.16.238.7:8080/ui"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_get_pets():
    url = "http://172.16.238.7:8080/pet"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_post_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = "http://172.16.238.7:8080/pet"
    content = {"id": 0, "name": "gizmo",  "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data = json.dumps(content), headers = headers)

    assert response.status_code == 200

def test_get_pet():
    url = "http://172.16.238.7:8080/pet/0"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_patch_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.7:8080/pet"
    content = {"id": 0, "name": "gizmo",  "status": "SOLD", "species": "dog", "subspecies": "lab"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response)
    assert response.status_code == 200

def test_delete_pet():
    url = "http://172.16.238.7:8080/pet/0"
    # Send a GET request
    response = requests.delete(url)
    print(response)
    assert response.status_code == 200

def test_get_users():
    url = "http://172.16.238.7:8080/user"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_post_user():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = "http://172.16.238.7:8080/user"
    content = {"id": 0, "name": "jerry", "role": "Customer"}

    response = requests.post(url, data = json.dumps(content), headers = headers)

    assert response.status_code == 200

def test_get_user():
    url = "http://172.16.238.7:8080/user/0"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_patch_user():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.7:8080/user"
    content = {"id": 0, "name": "jerry", "role": "BANNED"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response)
    assert response.status_code == 200

def test_delete_user():
    url = "http://172.16.238.7:8080/user/0"
    # Send a GET request
    response = requests.delete(url)
    print(response)
    assert response.status_code == 200