from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from config import DB_CONFIG

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

mysql = MySQL(app)

# Rota de cadastro (POST)
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.json
    nome = dados['nome']
    email = dados['email']
    matricula = dados['matricula']
    senha = dados['senha']
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO aluno (nome, email, matricula, senha) VALUES (%s, %s, %s, %s)",
                   (nome, email, matricula, senha))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'}), 201

# Rota de listagem (GET)
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, nome, email, matricula FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()

    resultado = []
    for a in alunos:
        resultado.append({
            'id': a[0],
            'nome': a[1],
            'email': a[2],
            'matricula': a[3]
        })

    return jsonify(resultado)

# Front-end simples (opcional)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nome, email, matricula FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()
    return render_template('listar.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)
