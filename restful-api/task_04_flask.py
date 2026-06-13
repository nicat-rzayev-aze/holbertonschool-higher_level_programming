#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():

    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the server status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
 
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():

    user_data = request.json

    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
