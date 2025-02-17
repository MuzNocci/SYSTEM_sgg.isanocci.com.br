FROM postgres:17-alpine



COPY default.conf /etc/postgresql/postgresql.conf
COPY start.sh /docker-entrypoint-initdb.d/start.sh
COPY .env /docker-entrypoint-initdb.d/.env

RUN chmod +x /docker-entrypoint-initdb.d/start.sh

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]