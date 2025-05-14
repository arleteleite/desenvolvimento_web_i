# API de Cadastro de Alunos com Flask e MySQL

Este projeto é uma API REST criada com Flask para cadastrar e listar alunos em um banco de dados MySQL.
Projeto criado na disciplina de Programação para WEB I com o Prof. Msc. Bruno Bandeira Fernandes.
Curso: Análise e Desenvolvimento de Sistemas - UNITINS - TOGRADUADO

## Funcionalidades

- Cadastrar aluno via POST `/alunos`
- Listar alunos via GET `/alunos`
- Front-end opcional com HTML para uso da API

## Como executar

1. Clone este repositório
2. Crie um ambiente virtual e instale as dependências:

python -m vevn venv
venv\Scripts\activate
pip install -r requirements.txt

## Configure o banco de dados

1. Atualize com os seus dados

    DB_HOST=localhost
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=escola

## Execute a aplicação

1. No terminal 
    python app.py

## Autor
    Arlete Leite ✨
