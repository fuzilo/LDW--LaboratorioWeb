from flask_restful import Resource
from api import api
from ..schemas import game_schemas
from .. models import game_model
from ..services import game_service
from flask import make_response, jsonify, request


class GameList(Resource):
    def get(self):
        games = game_service.get_games()
        g = game_schemas.GameSchema(many=True)
        
        return make_response(g.jsonify(games), 200)
    ##código 200 (ok), requisição bem sucedida
    
#instalar extensão do postman


class RecursosAPI(Resource):
    def get(self):
        return "Requisição GET - Responsável por recuperar informações da API"
    
    def post(self):
        return "Requisição POST - Resposável po criar novos recursos na API"
    
    def put(self):
        return "Requisição PUT - Responsável por alterar recursos na API"
    
    def delete(self):
        return "Requisição Delete - Responsável por excluir recursos na API"

api.add_resource(GameList, '/games')    
#api.add_resource(RecursosAPI, '/recursos')


