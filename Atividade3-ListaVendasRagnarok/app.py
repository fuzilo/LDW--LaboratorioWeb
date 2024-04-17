from flask import Flask, render_template
from controllers import routes
import os
from models.database import db

#Carregando flask na variável app
app = Flask(__name__, template_folder='views')

#Inicia a função de rotas tendo Flask como parâmetro
routes.init_app(app)

#ler diretórios
dir= os.path.abspath(os.path.dirname(__file__))

#passando o diretório para o SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/ragnarok.sqlite3')

#Definir a secretKey para as flashed messages
app.config['SECRET_KEY'] = 'ATNAD'

#Definindo timeout
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

#Definindo a pasta que receberá arquivos de upload
app.config['UPLOAD_FOLDER'] = 'static/uploads'

#Definindo o tamanho máximo de um arquivo de upload
app.config['MAX_CONTENT_LENGHT']=16*1024*1024

#Se for executado diretamente pelo interpretador
if __name__ == '__main__':
    #Veririca no início da aplicação, se o banco já existe, se não, cria-o
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()

    #Aplicação roda na porta 5000 do localhost, com debug ativado
    app.run(host='localhost', port=5000, debug=True)
