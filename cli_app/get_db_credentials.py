#!/usr/bin/env python3

import json
import requests
import sys

VAULT_URL = 'http://127.0.0.1:8200/v1/database/creds/{}'

def get_creds(token, role):
    headers = {'X-Vault-Token': token}
    response = requests.get(VAULT_URL.format(role), headers=headers)
    response_json = json.loads(response.text)
    db_user = response_json["data"]["username"]
    db_pass = response_json["data"]["password"]
    return json.dumps({'username': db_user, 'password': db_pass})

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        print('Incorrect syntax')
        sys.exit(1)
    role = sys.argv[1]
    token = sys.argv[2]
    if role not in ['read', 'write']:
        print('Roles accepted: read, write')
        sys.exit(1)
    print(get_creds(token, role))
