# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes
import pymysql

from models.database import db

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Iniciando a função de rotas init_app passando o Flask como parâmetro
routes.init_app(app)

##Define o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# # Permite ler o diretório absoluto de um determinado arquivo
# dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório para o SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
#se tiver senha f'mysql://root:admin@localhost/{DB_NAME}

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
    # COnecta o MYSQL para criar o banco de dados, se necessário
    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = '',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            #Cria o banco de dados, se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados está criado!")
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")        
    finally:
        connection.close()
        
    # Inicializando a aplicação Flask
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)
