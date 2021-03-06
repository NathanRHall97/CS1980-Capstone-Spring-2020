import requests
import json

def test_get_pets():
    url = "http://{}:8080/pet".format(api_ip)
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

    url = "http://{}:8080/pet".format(api_ip)
    content = {"id": 0, "name": "gizmo",  "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#READ PET
def test_get_pet():
    url = "http://{}:8080/pet/0".format(api_ip)
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
    url = "http://{}:8080/pet".format(api_ip)
    content = {"id": 0, "name": "gizmo",  "status": "SOLD", "species": "dog", "subspecies": "lab"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#DELETE PET
def test_delete_pet():
    url = "http://{}:8080/pet/0".format(api_ip)
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 200

# Makes sure that we can't get deleted information for PET
def test_get_deleted_pet():
    url = "http://{}:8080/pet/0".format(pet_ip)
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# added test (PET)
# Makes sure that a header is necessary and throws an error without one.
def test_header_pet():
    mimetype = 'application/json'
    headers = { }
    url = "http://{}:8080/pet".format(pet_ip)
    content = {"id": 0, "name": "gizmo", "status": "available", "species": "dog", "subspecies": "lab"}

    response = requests.post(url, data=json.dumps(content), headers=headers)
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
    url = "http://{}:8080/pet".format(pet_ip)
    content = { }
    response = requests.patch(url, data=json.dumps(content), headers=headers)
    print(response.json())
    assert response.status_code == 405

# Tests to see if a negative integer will throw an error. In pet.py pet_len(id) must be > 0.
def test_negative_id_pet():
    url = "http://{}:8080/pet/-1".format(pet_ip)
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# added edge case test (PET)
# Tests to see if a negative integer will throw an error or modify/delete a pet_len that it shouldn't
def test_negative_id_delete_pet():
    url = "http://{}:8080/pet/-1".format(pet_ip)
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 404