from flask import Flask, request, url_for
from flask_cors import CORS, cross_origin
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
from flask import Response
from app import app
from models import User
from app import db

FlaskJSON(app)
CORS(app)

@app.route('/api/login/', methods=['GET', 'POST'])
@cross_origin()
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = User.query.filter_by(email=username, password=password).first()

    if user is None :
        ret = {
            'message': 'Failure'
        }
        js = json.dumps(ret)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    else :
        ret = {
            'message': 'SUCCESS',
            'username': username,
            'boomarks': user.parsePreferences(user.bookmarks),
        }

        js = json.dumps(ret)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/api/signup/', methods=['GET', 'POST'])
@cross_origin()
def signup():

    print("1")
    data = request.get_json()

    email = data['email']
    username = data['username']
    password = data['password']

    print(data)
    print(User)
    print("2")
    user = User.query.filter_by(username=username, password=password).first()

    print("3")


    if user is None:

        print("4")

        user = User(username, email, password)
        print("5")
        db.session.add(user)
        print("6")
        db.session.commit()

        print("7")

        ret = {
            'message': 'SUCCESS',
            'username': username,
            'boomarks': user.parsePreferences(user.bookmarks),
        }
    else:
        ret = {
            'message': 'FAILURE',
        }
    js = json.dumps(ret)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/api/editPreferences/', methods=['GET', 'POST'])
@cross_origin()
def editPreferences():
    data = request.get_json()

    username = data['username']
    password = data['password']
    bookmarks = data['bookmarks']

    user = User.query.filter_by(username=username, password=password).first()

    if user is None :
        ret = {
            'message': 'FAILURE'
        }
        js = json.dumps(ret)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    else :
        user.editPreferences(bookmarks)
        db.session.commit()
        ret = {
            'message': 'SUCCESS',
        }
        js = json.dumps(ret)
        resp = Response(js, status=200, mimetype='application/json')
        return resp
