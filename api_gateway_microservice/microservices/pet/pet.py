from flask import Flask, make_response, abort, request
import os
import json
import psycopg2

app = Flask(__name__)

#HTTP RETURN CODES
HTTP_Successful = 200
HTTP_Created = 201
HTTP_NotFound = 404
HTTP_MethodNotAllowed = 405


# Function to create a connection and return it
def create_connection():
    connection = psycopg2.connect(
        host='172.16.238.10',  # This is the subnet IP for the Server, declared in docker-compose file.
        port=5432,
        dbname='pet_db',
        user='postgres',
        password='postgres',
    )
    return connection

#Takes tuple results as an input, maps each row to its key, and returns the correct json object
def tuple_to_json(tuple):
    keys = ('id', 'name', 'status', 'species', 'subspecies', 'status')
    results = []
    for row in tuple:
        results.append(dict(zip(keys, row)))
    return results

# Functions that calls pet_db and returns all the pets
def get_all_pets():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from petTable")
    x = cursor.fetchall()
    results = tuple_to_json(x)
    cursor.close()
    conn.close()
    return results


# Returns the next free petID to use
def get_next_petID():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute Query that searches through the petIds in petTable and returns the last petID
    cursor.execute("select id from petTable order by id desc limit 1")
    petID = cursor.fetchone()
    if petID is None:
        next_pet_id = 0
        # increment the petID to get a new one
    else:
        get_id = petID[0]
        next_pet_id = int(get_id) + 1

    cursor.close()
    conn.close()

    return next_pet_id


@app.route("/pet", methods=['GET', 'POST'])
def update_pet():
    if request.method == 'POST':
        # Get species, subspecies, name, and status from form
        petId = get_next_petID()
        species = request.form.get('species')
        subspecies = request.form.get('subspecies')
        name = request.form.get('name')
        status = request.form.get('status')

        if species is None or subspecies is None or name is None or status is None:
            return json.dumps('Method Not Allowed'), HTTP_MethodNotAllowed

        # Insert attributes into table
        query = "insert into petTable (id, name, status, species, subspecies) Values(%s, %s, %s, %s, %s)"
        values = (petId, name, status, species, subspecies)
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        # Return Value inserted
        cursor.execute("Select * from petTable where id = {}".format(petId))
        x = cursor.fetchall()
        results = tuple_to_json(x)
        conn.close()
        cursor.close()
        return json.dumps(results, indent=1), HTTP_Created

    # Get all pets
    z = get_all_pets()
    return json.dumps(z, indent=1), HTTP_Successful

@app.route("/pet", methods=['PATCH'])
def patch_pet():
    if request.method == 'PATCH':

        petId = request.form.get('id')
        species = request.form.get('species')
        subspecies = request.form.get('subspecies')
        name = request.form.get('name')
        status = request.form.get('status')

        if species is None or subspecies is None or name is None or status is None:
            return json.dumps('Method Not Allowed'), HTTP_MethodNotAllowed

        query = "update petTable set name = %s, status = %s, species = %s, subspecies = %s where id = %s"
        values = (name, species, status, subspecies, petId)

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        # Return Value inserted
        cursor.execute("Select * from petTable where id = {}".format(petId))
        x = cursor.fetchall()
        results = tuple_to_json(x)
        conn.close()
        cursor.close()
        return json.dumps(results, indent=1), HTTP_Created




@app.route("/pet/<petId>", methods=['GET'])
def find_by_id(petId):
    x = int(petId)
    pet_len = get_next_petID()
    if pet_len > x >= 0:
        conn = create_connection()
        cursor = conn.cursor()
        # Return Value
        cursor.execute("Select * from petTable where id = {}".format(x))
        x = cursor.fetchall()
        if not x:
            return json.dumps('Object does not exist'), HTTP_NotFound
        results = tuple_to_json(x)
        conn.close()
        cursor.close()
        return json.dumps(results, indent=1), HTTP_Successful
    else:
        return json.dumps("ID not found"), HTTP_NotFound

@app.route("/pet/<petId>", methods=['DELETE'])
def delete_pet(petId):
    x = int(petId)
    pet_len = get_next_petID()
    if pet_len > x >= 0:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from petTable where id = {}".format(x))
        get_pet = cursor.fetchall()
        results = tuple_to_json(get_pet)

        cursor.execute("Delete from petTable where id = {}".format(x))
        conn.commit()

        conn.close()
        cursor.close()
        return json.dumps(results, indent=1), HTTP_Successful
    else:
        return json.dumps("ID not found"), HTTP_NotFound


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
    # app.run()
