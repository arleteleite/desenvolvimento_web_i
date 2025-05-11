from flask import Flask, request, jsonify
from dotenv import load_dotenv
from models import create_aluno, get_all_alunos
from db import get_connection
import os

print(">>> app.py está rodando")
print(f"__name__: {__name__}")

# Carrega variáveis do .env
load_dotenv()

# Testa conexão com o banco (sem try)
conn = get_connection()
conn.close()
print("✅ Conexão com banco estabelecida com sucesso.")

# Inicializa o app Flask
app = Flask(__name__)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    create_aluno(data)
    return jsonify({"mensagem": "Aluno cadastrado com sucesso!"}), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = get_all_alunos()
    return jsonify(alunos), 200

if __name__ == '__main__':
    print("🔥 Iniciando servidor Flask...", flush=True)
    app.run(debug=True)

