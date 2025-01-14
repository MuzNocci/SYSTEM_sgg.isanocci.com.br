FROM nginx:1.27.3-alpine

RUN touch /etc/nginx/conf.d/default.conf
RUN chmod 777 /etc/nginx/conf.d/default.conf

COPY ./default.conf.tpl /etc/nginx/conf.d/default.conf