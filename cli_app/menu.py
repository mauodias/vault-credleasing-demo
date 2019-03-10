#!/usr/bin/env python3

import psycopg2
import sys
import os
import requests
import json
import time
import threading

class Tools:
    @staticmethod
    def log_delay(count, message):
        def function(count, message):
            f = open('log.txt', 'a+')
            time.sleep(count)
            f.write(f'{message}\n')
        t = threading.Thread(target=function, args=(count, message, ))
        t.start()

    @staticmethod
    def clear_log():
        f = open('log.txt', 'w')
        f.write('')
        f.close()

class Database:
    DB_HOST='localhost'
    DB_PORT='2345'
    DB_NAME='demodb'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        return psycopg2.connect(user=self.username,
                                password=self.password,
                                host=self.DB_HOST,
                                port=self.DB_PORT,
                                dbname=self.DB_NAME)
    def read_table(self):
        try:
            self.connection = self.connect()
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM public.touch;')
            results = cursor.fetchall()
            for result in results:
                print(result)
            print('\n')
            cursor.close()
        except:
            print(f'Erro ao executar a transação')
        finally:
            self.connection.close()

    def write_table(self):
        try:
            self.connection = self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO touch VALUES ('{self.username}');")
            self.connection.commit()
            print('Done!')
        except psycopg2.Error as e:
            print(f'Erro ao executar a transação: {e.pgerror}')
        finally:
            cursor.close()
            self.connection.close()

class Vault:
    VAULT_ADDR='http://127.0.0.1:8200'

    def get_user(self, username, password):
        body = {"password": password}
        url = '{}{}'.format(self.VAULT_ADDR, '/v1/auth/userpass/login/{}'.format(username))
        response = requests.post(url, data=json.dumps(body))
        response_json = json.loads(response.text)
        self.VAULT_TOKEN = response_json["auth"]["client_token"]
        print(f'------\n{json.dumps(response_json, indent=4)}\n------')

    def get_creds(self, role):
        if not self.VAULT_TOKEN:
            print('Solicite um token antes.')
            return
        headers = {'X-Vault-Token': self.VAULT_TOKEN}
        url = '{}{}'.format(self.VAULT_ADDR, '/v1/database/creds/{}'.format(role))
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        self.DB_USER = response_json["data"]["username"]
        self.DB_PASS = response_json["data"]["password"]
        lease_duration = response_json["lease_duration"]
        Tools.log_delay(0, f'{self.DB_USER} criado com a role {role}')
        Tools.log_delay(int(lease_duration), f'Permissão {role} expirou para o usuário {self.DB_USER}')
        print(f'------\n{json.dumps(response_json, indent=4)}\n------')

def menu():
    vault = Vault()
    db = {}
    Tools.clear_log()

    while True:
        opts = '''Escolha uma opção abaixo:
[1] Solicitar token de usuário do Vault
[2] Solicitar credenciais de leitura do banco
[3] Solicitar credenciais de escrita do banco
[4] Ler do banco de dados
[5] Escrever no banco de dados
[X] Sair

'''
        os.system('clear')
        print(opts)
        opt = input('> ')

        if opt == '1':
            username = input('Username: ')
            password = input('Password: ')
            vault.get_user(username, password)
        elif opt == '2':
            vault.get_creds('read')
            db = Database(vault.DB_USER, vault.DB_PASS)
        elif opt == '3':
            vault.get_creds('write')
            db = Database(vault.DB_USER, vault.DB_PASS)
        elif opt == '4':
            if not db:
                print('Gere credenciais de leitura primeiro')
            else:
                db.read_table()
        elif opt == '5':
            if not db:
                print('Gere credenciais de escrita primeiro')
            else:
                db.write_table()
        elif opt.upper() == 'X':
            print('Adeus.')
            sys.exit(0)

        input()

if __name__ == "__main__":
    menu()
