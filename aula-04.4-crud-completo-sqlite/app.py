from flask import Flask, render_template
from controllers import routes
from models.database import mongo, Game
import pymysql

app = Flask(__name__, template_folder='views')



app.config['MONGO_URI'] ='mongodb://localhost:27017/games'

routes.init_app(app)

DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# Se for executado diretamente pelo interpretador (arquivo principal)
if __name__ == '__main__': 
    mongo.init_app(app=app)

    with app.app_context():
        if 'games' not in mongo.db.list_collection_names():
            #Insere um documento para cria a coleção
            game = Game(
                titulo ='',
                ano =0,
                categoria='', 
                plataforma='',
                preco=0,
                quantidade=0
            )
            game.save()
            

    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)