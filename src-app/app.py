#!/usr/local/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    user_agent_info = request.headers.get('User-Agent')
    return f'Welcome to 2022!<br><br>User Agent: {user_agent_info}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
