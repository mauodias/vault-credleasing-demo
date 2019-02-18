export VAULT_ADDR=http://127.0.0.1:8200

vault secrets enable database

vault write -address=$VAULT_ADDR database/config/postgres \
    plugin_name=postgresql-database-plugin \
    allowed_roles="read_only" \
    connection_url="postgresql://{{username}}:{{password}}@postgres:5432?sslmode=disable" \
    username="postgres" \
    password="securepassword"
