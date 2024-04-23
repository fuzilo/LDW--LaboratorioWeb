# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes
import pymysql

from models.database import mongo, Game

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

#Definindo o endereço do MongoDB

app.config['MONGO_URI'] ='mongodb://localhost:27017/games'

# Iniciando a função de rotas init_app passando o Flask como parâmetro
routes.init_app(app)

##Define o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# # Permite ler o diretório absoluto de um determinado arquivo
# dir = os.path.abspath(os.path.dirname(__file__))



## Definindo a Scret Key para as flashed messages
app.config['SECRET_KEY'] = 'thegamessecret'

# Define o tempo de duração da Sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

##Define a pasta que receberá arquivos de upload
app.config['UPLOAD_FOLDER']='static/uploads'

## Defininfo o tamano máximo de um arquivo de upload
app.config['MAX_CONTENT_LENGHT']=16*1024*1024

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
