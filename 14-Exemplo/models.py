from conf import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#classe de modelo para o banco
class Postagem(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    titulo = db.Column(db.String(50))
    conteudo = db.Column(db.Text())

    def __init__(self, id, titulo, conteudo):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo