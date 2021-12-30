#!/bin/bash
if [ -f ../.env ]; then
  export $(grep -v '^#' ../.env | xargs)
fi

#Generate Root Key
openssl genrsa -out "root-ca.key" 4096

#Generate a CSR for a root certificate using the root key
openssl req -new -key "root-ca.key" -out "root-ca.csr" -sha256 -subj '/C=US/ST=Virginia/L=Falls Church/O=MYORG/CN=Sample CA'

#Sign the root Certificate (using the "root-ca.cnf" file for config)
openssl x509 -req -days 3650 -in "root-ca.csr" -signkey "root-ca.key" -sha256 -out "root-ca.crt" -extfile "root-ca.cnf" -extensions root_ca

#Generate the Site Key
openssl genrsa -out "site.key" 4096

#Generate the certificate signing request for the site key
openssl req -new -key "site.key" -out "site.csr" -sha256 -subj "/C=US/ST=Virginia/L=Falls Church/O=MYORG/CN=${FRONTEND_HOSTNAME}"

#Sign the site certificate (using the "site.cnf" file for config which constrains the certificate so that it can only be used to authenticate a server and not to sign certificates)
openssl x509 -req -days 750 -in "site.csr" -sha256 -CA "root-ca.crt" -CAkey "root-ca.key" -CAcreateserial -out "site.crt" -extfile "site.cnf" -extensions server