from db import get_connection
import hashlib

def create_aluno(data):
    nome = data.get('nome')
    email = data.get('email')
    matricula = data.get('matricula')
    senha = data.get('senha')

    if not all([nome, email, matricula, senha]):
        raise ValueError("Todos os campos são obrigatórios.")

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO aluno (nome, email, matricula, senha)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, email, matricula, senha_hash))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_alunos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, matricula FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return alunos
