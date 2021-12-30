from flask import Flask, request, Response
import json
import socket

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    headers = str(request.headers)
    hostname = socket.gethostname()
    resp = f'''<h1>Hello, from the Flask App in Docker!</h1>\n
    This App is Running on Host: {hostname}
    #<p>{headers}</p>'''
    return Response(resp, status=200)
