# OpenResty - Keycloak - Flask
This project requires Docker and docker-compose installed on either Linux or MacOS.  Windows is not currently supported.

## Getting Started
Steps To Start Project with Docker-Compose
1. If you have not installed Docker and docker-compose, do so now.
2. Modify the values in the .env file.  You can leave all of the defaults for running locally if you follow all the steps below. (If you use a different keycloak realm name, modify that in your .env file)
3. `cd certs` to change into the certs directory
4. `chmod +x ./generate_sample_certs.sh` to make the generate_sample_certs.sh file executable.
5. `./generate_sample_certs.sh` to generate sample CA, keys, and certificates.  This script uses values from the .env to generate certificates based on your frontend hostname.
6. `cd ..` to get back to the project root
7. `docker-compose up -d` to start the project
8. Create a realm called "myrealm" in Keycloak through the admin console at https://localhost/auth (you have to wait for Keycloak to start; login information can be found in the docker-compose.yml).  If you changed the realm name in the .env file, use that as the realm name instead, and make sure to update the realm name in the main.js file in the vue_app/src folder.
9. Create client called "vue-app" in "myrealm" realm. .If you are using a different client name, make sure to update it in the main.js file in the vue_app/src folder.
11. Create a new user in the realm and assign them a password.
12. Navigate to https://localhost/api/hello to access your flask app directly through an unprotetected API endpoint
13. Navigate to https://localhost/home and login to see the Vue app, protected by Keycloak, which can also connect to the Flask API. Use the button at the top of the app to make a protected API call to the Flask API through the Vue app.

The main.js file passes the Keycloak instance as a prop to the App.vue component.  Open the App.vue file to see how the Keycloak prop and its tokens are used by the application.
