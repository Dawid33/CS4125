FROM nginx:latest
ADD . /
COPY nginx.conf /etc/nginx/nginx.conf
