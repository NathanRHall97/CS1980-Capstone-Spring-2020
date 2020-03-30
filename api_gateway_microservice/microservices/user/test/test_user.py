import requests
import pytest
import json
import time

def test_get_users():
    url = "http://172.16.238.7:8080/user"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200

#CREATE USER
def test_post_user():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = "http://172.16.238.7:8080/user"
    content = {"id": 0, "name": "jerry", "role": "Customer"}

    response = requests.post(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#READ USER
def test_get_user():
    url = "http://172.16.238.7:8080/user/0"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200

#UPDATE USER
def test_patch_user():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.7:8080/user"
    content = {"id": 0, "name": "jerry", "role": "BANNED"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#DELETE USER
def test_delete_user():
    url = "http://172.16.238.7:8080/user/0"
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 200