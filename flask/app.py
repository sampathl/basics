from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world", 200

@app.route('/new')
def new_route():
    return json.dumps('message':'this is new '), 200 


if __name__ == "__main__":
    app.run()


