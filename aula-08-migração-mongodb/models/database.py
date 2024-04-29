# Importando o PyMongo
from flask_pymongo import PyMongo
# Importando o ObjectId
from bson import ObjectId

mongo = PyMongo()

# Classe responsável por criar a entidade "Games" com seus atributos.
class Game():
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
        
    def save(self):
        mongo.db.games.insert_one({
            'titulo': self.titulo,
            'ano': self.ano,
            'categoria' : self.categoria,
            'plataforma' : self.plataforma,
            'preco' : self.preco,
            'quantidade' : self.quantidade
        })
     
    @staticmethod   
    def get_all():
        return list(mongo.db.games.find())
    
    @staticmethod
    def delete(id):
        mongo.db.games.delete_one({'_id': ObjectId(id)})
        
    @staticmethod
    def get_by_id(id):
        return mongo.db.games.find_one({'_id': ObjectId(id)})    
    
    @staticmethod
    def update(self, id):
        mongo.db.games.update_one({'_id':ObjectId(id)}, 
             {'$set':
                 {
                     'titulo': self.titulo,
                     'ano': self.ano,
                     'categoria': self.categoria,
                     'plataforma':self.plataforma,
                     'preco': self.preco,
                     'quantidade': self.quantidade
                 }
                 })