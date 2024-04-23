# Importando o pymongo
from flask_pymongo import PyMongo
from bson import ObjectId

#ObjectId(id)

mongo = PyMongo()
# Classe responsável por criar a entidade "Games" com seus atributos
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
            'titulo' : self.titulo,
            'ano': self.ano,
            'categoria': self.categoria,
            'plataforma': self.plataforma,
            'preco': self.preco,
            'quantidade': self.quantidade
        })
    
    #método estático que não precisa criar uma instância do objeto
    @staticmethod
    def get_all():
        return list(mongo.db.games.find())       
         
    @staticmethod
    def delete(id):
        mongo.db.delete_one({'_id': ObjectId(id)})



        
    