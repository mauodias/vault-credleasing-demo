# vault-credleasing-demo

Este repositório serve de prova de conceito para a funcionalidade de `credential leasing` do Vault. A implementação é diretamente inspirada na implementação demonstrada nesse link: https://www.marcolancini.it/2017/blog-vault/.

## Requisitos

- docker
- docker-compose
- python3

## Execução

Para rodar a demo, clone o repositório e siga os seguintes passos:

- `docker-compose up -d` para inicializar os containers
- `docker exec vault /bin/ash -c "/scripts/fullsetup.sh 180"` para inicializar o vault e configurar o tempo de vida das credenciais para 180 segundos
- `source cli_app/.venv/bin/activate` ativa o virtualenv
- `python cli_app/menu.py`

A aplicação deve ser bem auto-explicativa, mas o fluxo esperado é um dos seguintes:
1. Autenticação no vault para gerar um token
2. Solicitar credenciais do banco de dados
  - Leitura ou escrita
3. Atuar no banco de dados de acordo com as credenciais solicitadas

Pull requests são extremamente bem vindos!
