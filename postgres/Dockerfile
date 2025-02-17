FROM postgres:17-alpine

COPY default.conf /etc/postgresql/postgresql.conf
COPY start.sh /docker-entrypoint-initdb.d/start.sh

RUN chmod +x /docker-entrypoint-initdb.d/start.sh

ENTRYPOINT ["sh", "-c", "/docker-entrypoint-initdb.d/start.sh"]

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]