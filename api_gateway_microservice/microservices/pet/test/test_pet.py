import requests
import json

def test_get_pets():
    url = "http://172.16.238.7:8080/pet"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200

#CREATE PET
def test_post_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = "http://172.16.238.7:8080/pet"
    content = {"id": 0, "name": "gizmo",  "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#READ PET
def test_get_pet():
    url = "http://172.16.238.7:8080/pet/0"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200

#UPDATE PET
def test_patch_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.7:8080/pet"
    content = {"id": 0, "name": "gizmo",  "status": "SOLD", "species": "dog", "subspecies": "lab"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#DELETE PET
def test_delete_pet():
    url = "http://172.16.238.7:8080/pet/0"
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 200
