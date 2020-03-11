from flask import Flask
from flask_restful import abort, Api, Resource, request
import json
import psycopg2

app = Flask(__name__)

CUSTOMERS = {0: 'Amy', 1: 'Bill', 2: 'Caroline'}  # should be replaced by proper db


# Function to create a connection and return it
def create_connection():
    connection = psycopg2.connect(
        host='172.16.238.9',  # This is the subnet IP for the Server, declared in docker-compose file.
        port=5432,
        dbname='user_db',
        user='postgres',
        password='postgres',
    )
    return connection

#Takes tuple results as an input, maps each row to its key, and returns the correct json object
def tuple_to_json(tuple):
    keys = ('id', 'name', 'role')
    results = []
    for row in tuple:
        results.append(dict(zip(keys, row)))
    return results



def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from userTable")
    x = cursor.fetchall()
    results = tuple_to_json(x)
    cursor.close()
    return results

def get_next_userID():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute Query that searches through the petIds in petTable and returns the last petID
    cursor.execute("select id from userTable order by id desc limit 1")
    userID = cursor.fetchone()
    # increment the userID to get a new one
    if userID is None:
        next_user_id = 0
    else:
        get_id = userID[0]
        next_user_id = int(get_id) + 1

    cursor.close()
    conn.close()

    return next_user_id


@app.route('/')
def aa():
    return 'hi from user'


@app.route("/user", methods=['GET'])
def get():
    #don't really know where this if statement comes into play?
    if request.args.get('cid'):
        cid = int(request.args.get('cid'))
        return json.dumps((cid, CUSTOMERS[cid]))
    x = get_all_users()
    return json.dumps(x, indent=1)


@app.route("/user/<cid>", methods=['GET'])
def get_user(cid):
    x = int(cid)
    user_len = get_next_userID()
    if user_len > x >= 0:

        conn = create_connection()
        cursor = conn.cursor()

        # Return Value
        cursor.execute("Select * from userTable where id = {}".format(x))
        x = cursor.fetchall()
        result = tuple_to_json(x)
        conn.close()
        cursor.close()

        return json.dumps(result, indent=1)
    else:
        abort(404)

@app.route("/user/<cId>", methods=['DELETE'])
def delete_pet(cId):
    x = int(cId)
    user_len = get_next_userID()
    if user_len > x >= 0:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from userTable where id = {}".format(x))
        get_user = cursor.fetchall()
        results = tuple_to_json(get_user)

        cursor.execute("Delete from userTable where id = {}".format(x))
        conn.commit()

        conn.close()
        cursor.close()
        return json.dumps(results, indent=1)
    else:
        abort(404)


@app.route("/user", methods=['POST'])
def register_customer():

    #Get post values
    name = request.form.get('name')
    role= request.form.get('role')
    cid = get_next_userID()

    #insert values into DB
    query = "insert into userTable (id, name, role) Values(%s, %s, %s)"
    values = (cid, name, role)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    #pull the new customer from DB and return it
    cursor.execute("Select * from userTable where id = {}".format(cid))
    x = cursor.fetchall()
    result = tuple_to_json(x)
    conn.close()
    cursor.close()

    return json.dumps(result, indent=1)  # json.dumps((cid, CUSTOMERS[cid]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()