#Importando o flask na aplicação
from flask import Flask, render_template
from controllers import routes

#Carregando o flask na variável app
app = Flask(__name__, template_folder='views')

#Iniciando a função de Rotas init_app, passando o flask como parâmetro
routes.init_app(app)


if __name__ == "__main__":
    ##Rodando a aplicação no localhost, na porta 5000, com debugg ligado pra atualizar automaticamente
    app.run(host='localhost', port=5000, debug=True)
