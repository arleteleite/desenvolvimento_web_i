from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config.from_object('app.config.config.Config') # Carrega as configurações do banco de dados (config.py)

    db.init_app(app)

    # Importar e registrar rotas
    from app.routes.aluno_routes import db_alunos

    # Registro do Blueprint
    app.register_blueprint(db_alunos, url_prefix='/aluno')

    return app
