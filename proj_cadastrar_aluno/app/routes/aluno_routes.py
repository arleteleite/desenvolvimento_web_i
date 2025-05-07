from flask import Blueprint, request, jsonify
from app import db
from app.models.aluno import Aluno
from sqlalchemy.exc import SQLAlchemyError

db_alunos = Blueprint('aluno', __name__)


@db_alunos.route('/aluno', methods=['POST'])
def cadastrar_aluno():
    try:
        data = request.json

         # Verificar se todos os campos foram enviados
        if not all(key in data for key in ['nome', 'email', 'matricula', 'senha']):
            return jsonify({'mensagem': 'Todos os campos são obrigatórios'}), 400
        
        # Verificar se o e-mail já existe
        if Aluno.query.filter_by(email=data['email']).first():
            return jsonify({'mensagem': 'E-mail já cadastrado'}), 400
        
        aluno = Aluno(
            nome=data['nome'],
            email=data['email'],
            matricula=data['matricula'],
            senha=data['senha']
        )

        #adiciona o aluno ao banco
        db.session.add(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno cadastrado com sucesso'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Faz o rollback em caso de erro
        return jsonify({'mensagem': 'Erro ao cadastrar aluno', 'erro': str(e)}), 500


@db_alunos.route('/aluno', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    resultado = [{
        'nome': aluno.nome,
        'email': aluno.email,
        'matricula': aluno.matricula
    } for aluno in alunos]
    return jsonify(resultado), 200

