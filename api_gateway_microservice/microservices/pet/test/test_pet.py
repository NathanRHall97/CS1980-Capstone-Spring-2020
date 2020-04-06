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
    
# Makes sure that we can't get deleted information for PET
def test_get_deleted_pet():
    url = "http://172.16.238.9:8080/pet/0"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# added test (PET)
# Makes sure that a header is necessary and throws an error without one.
def test_header_pet():
    mimetype = 'application/json'
    headers = { }
    url = "http://172.16.238.9:8080/pet"
    content = {"id": 0, "name": "gizmo", "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data=json.dumps(content), headers=headers)
    print(response.json())
    assert response.status_code == 405

# added test (PET)
# Makes sure that the URL is a necessary parameter and throws an error without one.
def test_url_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = " "
    content = {"id": 0, "name": "gizmo",  "status": "SOLD", "species": "dog", "subspecies": "lab"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 405
# added test (PET)
# Makes sure that the content is a necessary parameter and throws an error without one.
def test_content_pet():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.9:8080/pet"
    content = { }
    response = requests.patch(url, data=json.dumps(content), headers=headers)
    print(response.json())
    assert response.status_code == 405

# Tests to see if a negative integer will throw an error. In pet.py pet_len(id) must be > 0.
def test_negative_id_pet():
    url = "http://172.16.238.9:8080/pet/-1"
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# added edge case test (PET)
# Tests to see if a negative integer will throw an error or modify/delete a pet_len that it shouldn't
def test_negative_id_delete_pet():
    url = "http://172.16.238.9:8080/pet/-1"
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 404

# added edge case test (USER)
# added test (USER)

# Makes sure that we can't get deleted information for USER
def test_get_deleted_user():
    url = "http://172.16.238.9:8080/user/0"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404
