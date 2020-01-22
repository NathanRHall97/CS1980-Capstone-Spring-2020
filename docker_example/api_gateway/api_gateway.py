# api_gateway.py
from flask import Flask
import requests

app = Flask(__name__)

INTERNAL_MICROSERVICE_ADDRESS = '172.16.238.3'
INTENRAL_MICROSERVICE_PORT = '8080'

@app.route('/')
def ground_control():
    # we will begin by constructing a response message in the API gateway
    msg = 'Ground Control to Major Tom...commencing countdown, engines on!\n'
    msg += '10, 9, 7, 6, 5, 4, 3, 2, 1...lift-off!\n'
    # We will make a request to our internal microservice, and extend our message with the response
    internal_response = requests.get('http://' + INTERNAL_MICROSERVICE_ADDRESS + ':' + INTENRAL_MICROSERVICE_PORT + '/')  # this is a request to 'http://172.16.238.3:8080/'
    # assuming the rquest was successful...
    # we now have requests.Response object from our internal microservice
    msg += "\nINCOMING MESSAGE FROM MAJOR TOM: " + internal_response.text + "\n"
    # finish the message
    msg += "\nControl to Major Tom: your circuits dead, there's something wrong! Can your hear me Major Tom?...\n"
    # and return our message
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
