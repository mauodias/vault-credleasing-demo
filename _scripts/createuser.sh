export VAULT_ADDR=http://127.0.0.1:8200

vault auth enable userpass
vault write auth/userpass/users/app password=app policies=user
vault policy write user scripts/policy.hcl 
