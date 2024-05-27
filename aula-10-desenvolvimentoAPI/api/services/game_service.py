from api import mongo
from ..models import game_model
from bson import ObjectId #Usado para ler objetos do Mongo

## O sérvice Contém os métodos de manipulação do banco de dados

def add_game(game):
    mongo.db.games.insert_one({
        'titulo':game.titulo,
        'descricao':game.descricao,
        'ano':game.ano
    })
    
@staticmethod
def get_games():
    return list(mongo.db.games.find())

@staticmethod
def get_game_by_id(id):
    return mongo.db.games.find_one({'_id': ObjectId(id)})

@staticmethod
def update_game(self, id):
    mongo.db.games.update_one({'_id': ObjectId(id)},
                              {'$set':
                                  {
                                      'titulo': self.titulo,
                                      'descricao':self.descricao,
                                      'ano': self.ano
                                  }})

@staticmethod
def delete_game(id):
    mongo.db.games.delete_one({'_id': ObjectId(id)})