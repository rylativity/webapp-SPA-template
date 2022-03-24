import jwt
from flask import Response
from jwt import PyJWKClient
def testpyjwt():
    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVRXh0X2JhMGtQTjc4Z3ZTZ3hjdnhPTWVsWFNFX0RRMnR5WWJhcTRLX2QwIn0.eyJleHAiOjE2NDc2NjAxNTIsImlhdCI6MTY0NzY1OTg1MiwiYXV0aF90aW1lIjoxNjQ3NjU5ODUxLCJqdGkiOiI5OThmMGVkMy0yZDdjLTQwNzMtYjllMi00YjE5MzQ1NzEzZWQiLCJpc3MiOiJodHRwczovL2xvY2FsaG9zdC9hdXRoL3JlYWxtcy9teXJlYWxtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjFjMzkzNDk2LTkyMTEtNDU3MS1hNWM0LThhMjkwNzEyMGNkOSIsInR5cCI6IkJlYXJlciIsImF6cCI6Im9wZW5yZXN0eSIsIm5vbmNlIjoiZTYwNDVhMWU3ZDVlNzA5ZDc4OGQ5OGQ1MDQxMjNiM2YiLCJzZXNzaW9uX3N0YXRlIjoiZDIwMTE1NzctMGVlMi00NTYyLWJjZGYtNTRiZjQ0MTk0OWE1IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW15cmVhbG0iLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6ImQyMDExNTc3LTBlZTItNDU2Mi1iY2RmLTU0YmY0NDE5NDlhNSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoicnN0ZXdhcnQifQ.eVgK8kU9IAbgOi1Dkw36tr79_HNeKuyl3cJON102gcTIdEFxCmcUBm7JM5uR-eG6vIksdJ2mDtLJ1ius8a0BBAcfAW66r8_QpaIw-fLbGKjD_rPVBXKVg1oj73vWuUonTAk0FvwpBjMkNEWMcsJ6kihmIyAtfoTZXYnkt8JOzkfKWQBx0Sk-BJCJcdJ5f-hRI2QzctovkftZBNPl0Q1grLpeLQ1wc97R3wJ_GOiHRLrsVSkXfaRvSm01LB5mQ1qTPNt8PRruJ2H6qjncR0rGBUrzYCG0hBg7ipHcbaN6kpzp8u0_xs6kAuLGvSUmUhD-adUyACjrFRoxubBNsNeHtw"
    url = "http://localhost:8080/auth/realms/myrealm/protocol/openid-connect/certs"
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
        return Response(response = {"status_code":401, "message":"Expired Token"},status=401, content_type="application/json")

res = testpyjwt()
print(res.response)
