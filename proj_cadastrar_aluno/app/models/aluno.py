from flask_sqlalchemy import SQLAlchemy

# Instanciando o objeto do SQLAlchemy
db = SQLAlchemy()

# Modelo de Aluno, que corresponde à tabela 'aluno' no banco de dados
class Aluno(db.Model):
    __tablename__ = 'aluno'  # Nome da tabela no banco de dados

    # Definindo os campos da tabela com base no esquema do banco
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id_aluno como chave primária e auto-increment
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, matricula, senha):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha

    def __repr__(self):
        return f'<Aluno {self.nome}>'
