from api import mongo
from ..models import game_model

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