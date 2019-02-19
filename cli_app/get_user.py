#!/usr/bin/env python3

import json
import requests
import sys

VAULT_URL = 'http://127.0.0.1:8200/v1/auth/userpass/login/{}'

def get_user(username, password):
    body = {"password": password}
    response = requests.post(VAULT_URL.format(username), data=json.dumps(body))
    response_json = json.loads(response.text)
    user_token = response_json["auth"]["client_token"]
    print(user_token)

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        print('Incorrect syntax')
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    get_user(username, password)
