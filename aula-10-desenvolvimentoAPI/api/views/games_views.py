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
        
        return make_response(g.jsonify(games), 200)#código 200 (OK), requisição bem sucedida
    
    def post(self):
        g = game_schemas.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400) #Codigo 400, BAD_REQUEST: Solicitação Inválida
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            ano = request.json["ano"]
            
            new_game = game_model.Game(titulo=titulo, 
                                       descricao=descricao,
                                       ano=ano)
            result = game_service.add_game(new_game)
            res = g.jsonify(result)
            return make_response(res, 201)#Código 201, CREATED: criação bem sucedida
    
    
    
class GameDetails(Resource):    
    def get(self,id):
        game = game_service.get_game_by_id(id)
        if game is None:
            return make_response(jsonify(("Game não foi encontrado"),404))#Código 404, NOT FOUND: rescuso requisistado, não encontrado
        g=game_schemas.GameSchema()
        return make_response(g.jsonify(game),200)
    
    def put(self,id):
        game_bd = game_service.get_game_by_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não encontrado"), 404)
        g = game_schemas.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate),404)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            ano = request.json["ano"]
            new_game = game_model.Game(titulo=titulo,
                                       descricao=descricao,
                                       ano=ano)
            game_service.update_game(new_game, id)
            updated_game = game_service.get_game_by_id(id)
            return make_response(g.jsonify(updated_game),200)
    
    def delete(self, id):                    
        game_bd = game_service.get_game_by_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não encontrado"), 404)
        game_service.delete_game(id)
        return make_response(jsonify("Game escluído com sucesso!", 204))#NO CONTENT, indica que a requisição foi bem sucedida, mas não há conteúdo para ser exibido
        
        
        
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
api.add_resource(GameDetails, '/games/<id>')    

