from fastapi import FastAPI, Response, Request
from fastapi.logger import logger

from datetime import datetime
from io import BytesIO
import logging
import socket
import jwt
from jwt import PyJWKClient

### https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/issues/19
gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)
# DEBUG > INFO > WARN > ERROR > CRITICAL > FATAL

app = FastAPI(debug=True)

def verify_user(request):
    headers = dict(request.headers)
    auth: str = headers.get("authorization")
    token = auth.replace("Bearer","").strip()
   
    url = "http://keycloak:8080/auth/realms/master/protocol/openid-connect/certs"
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
        return Response(content = {"status_code":401, "message":"Expired Token"},status_code=401)

@app.get("/")
async def root():
    logger.warn("LOGGING WORKS!!")

    return {"message":"Goodbye"}

@app.get('/api/hello')
def hello_world(request: Request):
    headers = str(request.headers)
    hostname = socket.gethostname()
    resp = f'''<h1>Hello, from the Flask App in Docker!</h1>\n
    This App is Running on Host: {hostname}
    #<p>{headers}</p>'''
    return Response(resp, status=200)

@app.get('/api/headers')
def return_headers(request:Request):
    headers = dict(request.headers)
    return headers

@app.get('/api/protected')
def test_token(request:Request):
    print(request.headers)
    token_data = verify_user(request=request)
    response = {"Result":"Success", "response_timestamp": datetime.now().isoformat(), "request_token":token_data}
    return response

