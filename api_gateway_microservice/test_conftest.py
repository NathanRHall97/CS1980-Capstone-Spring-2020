import requests
import pytest
import json
# pytest_plugins = ["docker_compose"]
# Invoking this fixture: 'function_scoped_container_getter' starts all services
# @pytest.fixture(scope="function")
def test_get_ui():
#API URL
    url = "http://0.0.0.0:8080/ui"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_get_pets():
    url = "http://0.0.0.0:8080/pet"
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

    url = "http://0.0.0.0:8080/pet"
    content = {"id": 0, "name": "gizmo",  "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data = json.dumps(content), headers = headers)

    assert response.status_code == 200

def test_patch_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://0.0.0.0:8080/pet"
    content = {"id": 6, "name": "gizmo",  "status": "SOLD", "species": "dog", "subspecies": "lab"}
    print(content)
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response)
    assert response.status_code == 200