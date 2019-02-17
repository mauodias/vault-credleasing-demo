# vault-credleasing-demo

Este repositório serve de prova de conceito para a funcionalidade de `credential leasing` do Vault. A implementação é diretamente inspirada na implementação demonstrada nesse link: https://www.marcolancini.it/2017/blog-vault/.

## Requisitos

- docker
- docker-compose

## Instalação

Para inicializar os containers, basta clonar o repositório e rodar o comando `docker-compose up -d`. Três containers serão criados, um com vault, um com consul e um com postgres. As credenciais do usuário do postgres estão explícitas no arquivo docker-compose.yml.
Apesar de estar recebendo conexões normalmente, o vault não estará inicializado. 
