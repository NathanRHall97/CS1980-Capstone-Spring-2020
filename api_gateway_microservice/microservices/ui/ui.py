from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/ui", methods = ['GET'])
def ui():
    return render_template('index.html')

@app.route("/ui-yaml", methods = ['GET'])
def ui_yaml():
    data = open('api_gateway.yaml').read()
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
#    app.run(host='0.0.0.0', port=8080)
#    app.run(debug=True)
