export VAULT_ADDR=http://127.0.0.1:8200

vault init -address=${VAULT_ADDR} > keys.txt
export VAULT_TOKEN=$(grep 'Initial Root Token:' keys.txt | awk '{print substr($NF, 1, length($NF))}')

vault unseal -address=${VAULT_ADDR} $(grep 'Key 1:' keys.txt | awk '{print $NF}')
vault unseal -address=${VAULT_ADDR} $(grep 'Key 2:' keys.txt | awk '{print $NF}')
vault unseal -address=${VAULT_ADDR} $(grep 'Key 3:' keys.txt | awk '{print $NF}')

vault auth -address=${VAULT_ADDR} ${VAULT_TOKEN}

vault policy write user scripts/policy.hcl
