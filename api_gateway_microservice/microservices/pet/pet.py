from flask import Flask, make_response, abort, request
import os
import json

app = Flask(__name__)

Pets = {0: {'id':0, 'name': 'dog', 'status':'sold'},
    1: {'id':1, 'name': 'cat', 'status':'pending'}
    }

@app.route("/pet", methods = ['GET','POST','PATCH'])
def update_pet():
    if request.method == 'POST':
        #        content = request.get_json()
        petId = len(Pets)
        name = request.form.get('name')
        status = request.form.get('status')
        d = {"id": petId, "name": name, "status": status}
        Pets[petId] = d
        return json.dumps(d)
    return json.dumps(Pets)

@app.route("/pet/<petId>", methods = ['GET'])
def find_by_id(petId):
    if int(petId) < len(Pets) and int(petId) >= 0:
        return json.dumps(Pets[int(petId)])
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    #app.run()