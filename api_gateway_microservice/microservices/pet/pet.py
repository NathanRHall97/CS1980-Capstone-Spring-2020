from flask import Flask, make_response, abort, request
import os
import json
import psycopg2

app = Flask(__name__)

Pets = {0: {'id':0, 'name': 'dog', 'status':'sold'},
    1: {'id':1, 'name': 'cat', 'status':'pending'},
    2: {'id':2, 'name': 'lizard', 'status':'pending'}
    }

#Function to create a connection and return it
def create_connection():
    connection = psycopg2.connect(
        host='172.16.238.9', #This is the subnet IP for the Server, declared in docker-compose file.
        port=5432,
        dbname='pet_db',
        user='postgres',
    )
    return connection

#Functions that calls pet_db and returns all the pets
def get_all_pets():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from petTable")
    x = cursor.fetchall()
    cursor.close()
    return x


@app.route("/pet", methods = ['GET','POST','PATCH'])
def update_pet():
    if request.method == 'POST':
        # content = request.get_json()

        petId = len(Pets)
        name = request.form.get('name')
        status = request.form.get('status')
        d = {"id": petId, "name": name, "status": status}
        Pets[petId] = d

        #Testing to get all pets
        x = get_all_pets()
        return json.dumps(x)
        #return get_all_pets()

    #Testing to get all pets
    z = get_all_pets()
    return json.dumps(z)

@app.route("/pet/<petId>", methods = ['GET'])
def find_by_id(petId):
    if int(petId) < len(Pets) and int(petId) >= 0:
        return json.dumps(Pets[int(petId)])
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    #app.run()