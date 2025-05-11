# 📘 Pseudocódigo e Explicações — API Flask + MySQL (Cadastro e Listagem de Alunos)

Este documento explica o funcionamento da aplicação **API RESTful com Flask e MySQL**, desenvolvida para cadastrar (`POST`) e listar (`GET`) alunos.

---

## 🧠 Visão Geral

A aplicação é estruturada para:

1. Receber requisições via HTTP (`POST` e `GET`).
2. Conectar-se a um banco de dados MySQL.
3. Executar comandos SQL para armazenar e recuperar dados.
4. Retornar respostas JSON apropriadas.

---

## 📁 Estrutura de Diretórios

flask_alunos_api/
├── app.py # Arquivo principal Flask
├── db.py # Conexão com o banco de dados MySQL
├── models.py # Operações de banco (Create e List)
├── .env # Variáveis de ambiente (segurança)
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
└── schema.sql # Script de criação da tabela aluno


---

## ⚙️ Pseudocódigo Comentado

### 1. app.py (rotas Flask)

```python
Importar Flask e os métodos request e jsonify
Importar as funções do arquivo models.py
Importar a biblioteca dotenv para carregar configurações do .env

Inicializar a aplicação Flask

Definir rota POST "/alunos":
    Receber dados JSON da requisição
    Chamar a função create_aluno com os dados
    Retornar mensagem de sucesso ou erro em JSON

Definir rota GET "/alunos":
    Chamar a função get_all_alunos
    Retornar lista de alunos em formato JSON

Iniciar o servidor Flask

## db.py (conexão com o banco de dados)

Importar mysql.connector
Importar os dados de conexão do arquivo .env (host, user, password, database)

Criar função get_connection():
    Retornar um objeto de conexão com o banco MySQL

(Obs: Essa função será usada em models.py para se conectar ao banco)

### models.py (operações no banco de dados)

Importar get_connection de db.py

Definir função create_aluno(dados):
    Extrair nome, email, matrícula e senha dos dados
    (Opcional: hash da senha para segurança)
    Abrir conexão com o banco
    Executar comando INSERT INTO aluno
    Confirmar a operação com commit
    Fechar conexão

Definir função get_all_alunos():
    Abrir conexão com o banco
    Executar SELECT * FROM aluno
    Recuperar os dados com fetchall()
    Organizar os dados em uma lista de dicionários
    Retornar a lista

### schema.sql (criação da tabela)

CREATE TABLE aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    matricula VARCHAR(100),
    senha VARCHAR(255)
);

🚀 Como rodar o projeto
Instalar dependências:

    pip install -r requirements.txt

Criar banco de dados no MySQL:

    CREATE DATABASE flask_api_alunos;
    USE flask_api_alunos;
    Executar o script schema.sql.

Rodar o servidor Flask:

    python app.py

