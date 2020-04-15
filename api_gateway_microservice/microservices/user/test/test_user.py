import requests
import pytest
import json
import time

def test_get_users():
    url = "http://172.16.238.5:8080/user"
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

    url = "http://172.16.238.5:8080/user"
    content = {"id": 0, "name": "jerry", "role": "Customer"}

    response = requests.post(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#READ USER
def test_get_user():
    url = "http://172.16.238.5:8080/user/0"
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
    url = "http://172.16.238.5:8080/user"
    content = {"id": 0, "name": "jerry", "role": "BANNED"}
    response = requests.patch(url, data = json.dumps(content), headers = headers)
    print(response.json())
    assert response.status_code == 200

#DELETE USER
def test_delete_user():
    url = "http://172.16.238.5:8080/user/0"
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 200
 
# Makes sure that we can't get deleted information for USER
def test_get_deleted_user():
    url = "http://172.16.238.8:8080/user/0"
    # Send a GET request
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# Tests to see if a negative integer will throw an error. In user.py user_len(id) must be > 0.
def test_negative_id_user():
    url = "http://172.16.238.8:8080/user/-1"
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 404

# added edge case test (USER)
# Tests to see if a negative integer will delete or modify anything. In user.py user_len(id) must be > 0.
def test_negative_id_delete_user():
    url = "http://172.16.238.8:8080/user/-1"
    # Send a GET request
    response = requests.delete(url)
    print(response.json())
    assert response.status_code == 404


# added test (USER)
# Makes sure that a header is necessary and throws a 405 error without one.
def test_header_user():
    mimetype = 'application/json'
    headers = { }
    url = "http://172.16.238.8:8080/user"
    content = {"id": 0, "name": "jerry", "role": "Customer"}

    response = requests.post(url, data=json.dumps(content), headers=headers)
    print(response.json())
    assert response.status_code == 405

# added test (USER)
# Makes sure that content is necessary and throws a 405 error without one.
def test_content_user():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "http://172.16.238.8:8080/user"
    content = {}

    response = requests.post(url, data=json.dumps(content), headers=headers)
    print(response.json())
    assert response.status_code == 405
