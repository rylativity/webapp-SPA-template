from lib2to3.pgen2 import token
from flask import Flask, request, Response
import socket
import jwt
from jwt import PyJWKClient

from datetime import datetime

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def verify_user(req):
    headers = dict(req.headers)
    auth: str = headers.get("Authorization")
    token = auth.replace("Bearer","").strip()
   
    url = "http://keycloak:8080/auth/realms/myrealm/protocol/openid-connect/certs"
    jwks_client = PyJWKClient(url)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    try:
        data = jwt.decode(
            token,
            signing_key.key,
            audience="account",
            algorithms=["RS256"]
        )
        return data
    except jwt.ExpiredSignatureError:
        return Response(response = {"status_code":401, "message":"Expired Token"},status=401)

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    headers = str(request.headers)
    hostname = socket.gethostname()
    resp = f'''<h1>Hello, from the Flask App in Docker!</h1>\n
    This App is Running on Host: {hostname}
    #<p>{headers}</p>'''
    return Response(resp, status=200)

@app.route('/api/headers')
def return_headers():
    headers = dict(request.headers)
    return headers

@app.route('/api/protected')
def test_token():
    token_data = verify_user(req=request)
    response = {"Result":"Success", "response_timestamp": datetime.now().isoformat(), "request_token":token_data}
    return response