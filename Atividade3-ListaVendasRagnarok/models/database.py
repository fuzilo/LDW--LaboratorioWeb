from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Catalogo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(150))
    data = db.Column(db.String(10))
    valor = db.Column(db.String(20))
    ultima = db.Column(db.String(10))
    
    def __init__(self,item,data,valor,ultima):
        self.item = item
        self.data = data
        self.valor = valor
        self.ultima = ultima

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True, nullable= False)
    password = db.Column(db.String(120), nullable= False)
    
    def __init__(self, email, password):
        self.email=email
        self.password = password