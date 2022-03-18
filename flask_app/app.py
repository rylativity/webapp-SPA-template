from flask import Flask, request, Response
import socket
import jwt
from jwt import PyJWKClient

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

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

@app.route('/api/testtoken')
def test_token():
    headers = dict(request.headers)
    auth: str = headers.get("Authorization")
    token = auth.replace("Bearer","").strip()
   
    url = "http://keycloak:8080/auth/realms/myrealm/protocol/openid-connect/certs"
    jwks_client = PyJWKClient(url)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    data = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        options={"verify_exp": False},
    )
    return data