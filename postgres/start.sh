set -e
set -a

ENV_FILE="/docker-entrypoint-initdb.d/.env"

if [ -f "$ENV_FILE" ]; then
    echo "Carregando variáveis do $ENV_FILE..."
    set -o allexport
    source "$ENV_FILE"
    set +o allexport
else
    echo "Arquivo .env não encontrado em $ENV_FILE"
    exit 1
fi

set +a

echo "Aguardando PostgreSQL..."
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -p "$DB_PORT" -c '\q' 2>/dev/null; do
  >&2 echo "PostgreSQL ainda não está pronto - esperando..."
  sleep 2
done

echo "PostgreSQL está pronto!"

echo "Criando usuário e banco de dados (se ainda não existirem)..."
PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U postgres -p "$DB_PORT" <<EOSQL
DO \$\$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '$DB_USER') THEN
        CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
    END IF;

    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DB_NAME') THEN
        CREATE DATABASE $DB_NAME OWNER $DB_USER;
        GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
    END IF;
END
\$\$;
EOSQL