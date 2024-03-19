#Impostando biblioteca de Banco de dados embarcado SQL Alchemy

from flask_sqlalchemy import SQLAlchemy

#Caargando o SQL Alchemy na variável db
db = SQLAlchemy()

#Classe responsável por criar a entidade games com seus atributos:
class Game(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco =db.Column(db.String(150))
    quantidade =db.Column(db.Integer)

    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade) :
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade

