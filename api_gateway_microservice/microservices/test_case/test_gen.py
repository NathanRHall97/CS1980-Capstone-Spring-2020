import requests
import json
import pytest
# 1
def test_get_api():
    url = "http://localhost:8080/"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 2
def test_get_ui():
    url = "http://localhost:8080/ui#/"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 3
def test_get_pet():
    url = "http://localhost:8080/ui#/pet/find_by_id"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 4
def test_get_pets():
    url = "http://localhost:8080/ui#/pet/update_pets"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 5
def test_get_swagger():
    url = "http://localhost:8080/ui#/swagger/ui"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 6
def test_get_user():
    url = "http://localhost:8080/ui#/user/get_user"
    # Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200
# 7
def test_get_users():
    url = "http://localhost:8080/ui#/user/get"
# Send a GET request
    response = requests.get(url)
    print(response)
    assert response.status_code == 200

def test_post_users():
    BASE_URL = "http://localhost:8080/user"
    # Read Input JSON file
    file = open('C:\\Users\\12675\\Desktop\\API\\CreateUser.json', 'r')  #
    json_input = file.read()  # reads the complete content of json file
    request_json = json.loads(json_input)  # json loads will pass the data into json format (file.read() is a string).
    print(request_json)  # Checks if you can read / pass json file.
    # Make POST request with Json input
    response = requests.post(BASE_URL, request_json)
    print(response.content)
    # print(response.status_code)
    assert response.status_code == 201
    #Fetch Header from response
    #print(response.headers.get('Content Length'))
    #
    #response_json = json.loads(response.text)

    #id = jsonpath.jsonpath(response_json, 'id')
    #print(id[0])

def test_post_pets():
    BASE_URL = "http://localhost:8080/pet"
    # Read Input JSON file
    file = open('C:\\Users\\12675\\Desktop\\API\\CreatePet.json', 'r')  #
    json_input = file.read()  # reads the complete content of json file
    request_json = json.loads(json_input)  # json loads will pass the data into json format (file.read() is a string).
    print(request_json)  # Checks if you can read / pass json file.
    # Make POST request with Json input
    response = requests.post(BASE_URL, request_json)
    ## print(response.content)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201





