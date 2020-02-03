#!/usr/bin/env python
from flask import Flask
import requests
app = Flask(__name__)

@app.route('/gremlinz/mogwai')
def addMogwai(body,):
    microservice_response = requests.post(
        body,
    )
    return microservice_response


@app.route('/gremlinz/mogwai')
def getMogwai():
    microservice_response = requests.get(
        
    )
    return microservice_response


@app.route('/gremlinz/mogwai/{mogwaiId}')
def getMogwaiById(mogwaiId,):
    microservice_response = requests.get(
        mogwaiId,
    )
    return microservice_response


@app.route('/gremlinz/mogwai/{mogwaiId}')
def deleteMogwaiById(mogwaiId,):
    microservice_response = requests.delete(
        mogwaiId,
    )
    return microservice_response




if __name__ == "__main__":
    app.run()
