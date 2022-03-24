FROM openresty/openresty:alpine-fat

RUN mkdir /var/log/nginx
RUN apk add --no-cache openssl-dev
RUN apk add --no-cache git
RUN apk add --no-cache gcc
RUN luarocks install lua-resty-openidc

COPY ./proxy.conf /etc/nginx/proxy.conf
COPY ./nginx.conf /etc/nginx/nginx.conf


ARG KEYCLOAK_REALM_NAME
COPY ./default.conf /etc/nginx/conf.d/default.conf
#COPY ./access.lua.template /etc/nginx/access.lua.template
#RUN ["/bin/bash", "-c", "envsubst '$$FRONTEND_URL $$KEYCLOAK_REALM_NAME' < /etc/nginx/access.lua.template > /etc/nginx/access.lua"]

ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx", "-g", "daemon off;"]
