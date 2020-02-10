from flask import Flask
from flask_restful import abort, Api, Resource, request
import json
import psycopg2

app = Flask(__name__)

CUSTOMERS = {0: 'Amy', 1: 'Bill', 2: 'Caroline'} #should be replaced by proper db

#Function to create a connection and return it
def create_connection():
    connection = psycopg2.connect(
        host='172.16.238.9', #This is the subnet IP for the Server, declared in docker-compose file.
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

@app.route('/')
def aa():
	return 'hi from user'

@app.route("/user", methods=['GET'])
def get():
	if request.args.get('cid'):
		cid = int(request.args.get('cid'))
		return json.dumps((cid, CUSTOMERS[cid]))
	x = get_all_users()
	return json.dumps(x)

@app.route("/user/<int:cid>", methods=['GET'])
def get_user(cid):
	return json.dumps((cid, CUSTOMERS[cid]))


@app.route("/user", methods=['POST'])
def register_customer():
	name = request.form.get('name')
	cid = len(CUSTOMERS)
	CUSTOMERS.update({cid: name})
	return json.dumps(request.form) #json.dumps((cid, CUSTOMERS[cid]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    #app.run()