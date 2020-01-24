from flask import Flask, request
import json

app=Flask(__name__)


@app.route('/')
def default_():
    return 'this is default '



@app.route('/parameters')
def prarmeters():
    name=request.args.get('name')
    age=request.args.get('age')
    return json.dumps({'name':name, 'age':age})



@app.route('/arguments/<string:username>/<int:age>')
def arguments(username, age):
    return json.dumps({'name':username,'age':age})




if __name__== '__main__':
    app.run()
