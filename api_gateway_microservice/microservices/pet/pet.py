from flask import Flask, make_response, abort, request
import os
import json
import psycopg2

app = Flask(__name__)

Pets = {0: {'id': 0, 'name': 'dog', 'status': 'sold'},
        1: {'id': 1, 'name': 'cat', 'status': 'pending'},
        2: {'id': 2, 'name': 'lizard', 'status': 'pending'}
        }


# Function to create a connection and return it
def create_connection():
    connection = psycopg2.connect(
        host='172.16.238.9',  # This is the subnet IP for the Server, declared in docker-compose file.
        port=5432,
        dbname='pet_db',
        user='postgres',
    )
    return connection


# Functions that calls pet_db and returns all the pets
def get_all_pets():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from petTable")
    x = cursor.fetchall()
    cursor.close()
    conn.close()
    return x


# Returns the next free petID to use
def get_next_petID():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute Query that searches through the petIds in petTable and returns the last petID
    cursor.execute("select petid from petTable order by petid desc limit 1")
    petID = cursor.fetchone()[0]

    # increment the petID to get a new one
    next_pet_id = int(petID) + 1

    cursor.close()
    conn.close()

    return next_pet_id


@app.route("/pet", methods=['GET', 'POST', 'PATCH'])
def update_pet():
    if request.method == 'POST':

        # Get species, subspecies, name, and status from form
        petId = get_next_petID()
        species = request.form.get('species')
        subspecies = request.form.get('subspecies')
        name = request.form.get('name')
        status = request.form.get('status')

        # Insert attributes into table
        query = "insert into petTable (petID, petspecies, petsubspecies, petname, petstatus) Values(%s, %s, %s, %s, %s)"
        values = (petId, species, subspecies, name, status)
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        # Return Value inserted
        cursor.execute("Select * from petTable where petID = {}".format(petId))
        x = cursor.fetchall()
        conn.close()
        cursor.close()
        return json.dumps(x)

    # Get all pets
    z = get_all_pets()
    return json.dumps(z)


@app.route("/pet/<petId>", methods=['GET'])
def find_by_id(petId):
    x = int(petId)
    pet_len = get_next_petID()
    if pet_len > x >= 0:
        conn = create_connection()
        cursor = conn.cursor()
        # Return Value
        cursor.execute("Select * from petTable where petID = {}".format(x))
        x = cursor.fetchall()
        conn.close()
        cursor.close()
        return json.dumps(x)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()
