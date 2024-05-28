from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
#pip install flask-restful
#pip install flask-marshmallow

api = Api(app)

#definir o endereço do banco, antes de iniciar o mongo

app.config["MONGO_URI"] = 'mongodb://localhost:27017/apigames'

mongo =  PyMongo(app)
ma = Marshmallow(app)
CORS(app)


#Aqui embaixo mesmo, pois ele precisa carregar as importações antes de puxar as views
from .views import games_views