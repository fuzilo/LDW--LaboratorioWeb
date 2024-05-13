from flask_restful import Resource
from api import api

class GameList(Resource):
    def get(self):
        return "Olá, Mundo API rodando"
    
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
api.add_resource(RecursosAPI, '/recursos')


