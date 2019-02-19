export VAULT_ADDR=http://127.0.0.1:8200

DEFAULT_TTL=${1-30}

vault secrets enable database

vault write -address=$VAULT_ADDR database/config/postgres \
    plugin_name=postgresql-database-plugin \
    connection_url="postgresql://{{username}}:{{password}}@postgres:5432?sslmode=disable" \
    allowed_roles="*" \
    username="postgres" \
    password="securepassword"

vault write -address=$VAULT_ADDR database/roles/read \
    db_name=postgres \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl=$DEFAULT_TTL

vault write -address=$VAULT_ADDR database/roles/write \
    db_name=postgres \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
        GRANT INSERT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl=$DEFAULT_TTL
