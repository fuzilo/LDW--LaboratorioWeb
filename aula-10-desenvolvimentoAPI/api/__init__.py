from flask import Flask
from flask_restful import Api

app = Flask(__name__)
#pip install flask-restful

api = Api(app)

#Aqui embaixo mesmo, pois ele precisa carregar as importações antes de puxar as views
from .views import games_views