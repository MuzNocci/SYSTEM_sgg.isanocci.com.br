#!/bin/sh



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

echo "Aguardando PostgreSQL iniciar..."
sleep 5

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<EOF
DO \$\$ 
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = "$POSTGRES_USER") THEN
      CREATE USER $POSTGRES_USER WITH PASSWORD "$POSTGRES_PASSWORD";
   END IF;
END \$\$;

GRANT CONNECT ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
EOF
echo "Configuração concluída!"