from api import ma
from marshmallow import Schema, fields

class GameSchema(ma.Schema):
    class Meta:
        fields=("_id", "titulo", "descricao", "ano")
    
    _id = fields.Str()
    titulo = fields.Str(required= True)
    descricao = fields.Str(required= True)
    ano = fields.Str(required= True)    