# internal_microservice.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def major_tom():
    return "This is Major Tom to Ground Control, I'm floating in a most particular way... and the stars look very different today!"

if __name__ == '__main__':
    app.run(host='172.16.238.3', port=8080)
