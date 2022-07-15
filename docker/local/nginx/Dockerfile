FROM nginx:1.21.5-alpine
# removing the image taht comes with docker by default
RUN rm /etc/nginx/conf.d/default.conf
# Creat our image named default.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf