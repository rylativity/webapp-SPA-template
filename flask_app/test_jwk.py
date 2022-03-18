import jwt
from jwt import PyJWKClient
def testpyjwt():
    token = ""
    url = "http://localhost:8080/auth/realms/myrealm/protocol/openid-connect/certs"
    jwks_client = PyJWKClient(url)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    data = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RSA256"],
        options={"verify_exp": False, "verify_signature":False},
    )
    return data

print(testpyjwt())
