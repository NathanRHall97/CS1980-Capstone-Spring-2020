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
    )
    return connection


def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from users")
    x = cursor.fetchall()
    cursor.close()
    return x

def get_next_userID():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute Query that searches through the petIds in petTable and returns the last petID
    cursor.execute("select userid from users order by userid desc limit 1")
    userID = cursor.fetchone()[0]

    # increment the userID to get a new one
    next_user_id = int(userID) + 1

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
    return json.dumps(x)


@app.route("/user/<cid>", methods=['GET'])
def get_user(cid):
    x = int(cid)
    user_len = get_next_userID()
    if user_len > x >= 0:

        conn = create_connection()
        cursor = conn.cursor()

        # Return Value
        cursor.execute("Select * from users where userID = {}".format(x))
        x = cursor.fetchall()
        conn.close()
        cursor.close()

        return json.dumps(x)
    else:
        abort(404)


@app.route("/user", methods=['POST'])
def register_customer():

    #Get post values
    name = request.form.get('name')
    role= request.form.get('role')
    cid = get_next_userID()

    #insert values into DB
    query = "insert into users (userid, username, userrole) Values(%s, %s, %s)"
    values = (cid, name, role)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    #pull the new customer from DB and return it
    cursor.execute("Select * from users where userid = {}".format(cid))
    x = cursor.fetchall()
    conn.close()
    cursor.close()

    return json.dumps(x)  # json.dumps((cid, CUSTOMERS[cid]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()
