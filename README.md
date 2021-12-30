# OpenResty - Keycloak - Flask
This project requires Docker and docker-compose installed on either Linux or MacOS.  Windows is not currently supported.

## Getting Started
Steps To Start Project with Docker-Compose
1. If you have not installed Docker and docker-compose, do so now.
2. Modify the values in the .env file.  You can leave all of the defaults for running locally with one major exception: If you are using MacOS, you must uncomment the relevant line in the "Docker" section of the .env file.
3. `cd certs` to change into the certs directory
4. `chmod +x ./generate_sample_certs.sh` to make the generate_sample_certs.sh file executable.
5. `./generate_sample_certs.sh` to generate sample CA, keys, and certificates.  This script uses values from the .env to generate certificates based on your frontend hostname.
6. `cd ..` to get back to the project root
7. `docker-compose up -d` to start the project
8. Create a realm called "myrealm" in Keycloak through the admin console at https://localhost/auth (you have to wait for Keycloak to start; login information can be found in the docker-compose.yml).  If you changed the realm name in the .env file, use that as the realm name instead
9. Create client called "openresty" in "myrealm" realm
10. Set client to "confidential" and copy the client id and secret under "credentials" tab in Keycloak to nginx_conf/default.conf in access.lua.template script.
11. Create a new user in the realm and assign them a password.
11. Return to your terminal and run `docker-compose build && docker-compose up -d` to rebuild and restart the openresty container with your keycloak realm information configured.
12. Navigate to https://localhost/hello to access your flask app protected by keycloak.

Note that the access.lua.template script is configured to add the OpenID Connect access_token to the "Authorization" header and id_token to the "Id-Token" header.  These tokens can be parsed (base64 decoded) and used by the flask app or any other upstream applications.