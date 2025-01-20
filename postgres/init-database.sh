#!/bin/bash


if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo "Arquivo .env não encontrado!"
    exit 1
fi


set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

    CREATE USER $POSTGRES_USER WITH PASSWORD $POSTGRES_PASSWORD;
    CREATE DATABASE $POSTGRES_DB;

    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

    ALTER USER $POSTGRES_USER CREATEDB;
    ALTER DATABASE $POSTGRES_DB OWNER TO $POSTGRES_USER;

EOSQL