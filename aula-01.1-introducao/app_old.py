#Importando o flask na aplicação
from flask import Flask, render_template


#Carregando o flask na variável app
app = Flask(__name__, template_folder='views')


##Criar Rotas, definindo a rota principal
@app.route('/')
#Função que será executada ao acessar a arota
def home():
    #Retorno que será exibido na rota
    #return '<h1> Esta é a homePage</h1>'
    return render_template('index.html')


@app.route('/game')
def game():
    game = {'Titulo': 'CS-GO',
            'Ano' : 2012,
            'Categoria' : 'FPS-Online'
            }
    jogadores=['Fabio', 'Sequela', 'Tiriça', '3ovo']
    return render_template('games.html', game = game, players = jogadores)

    #return '<h1>Bem vindo à página de Games</h1>'
    # titulo = 'CS-GO'
    # ano = 2012
    # categoria = 'FPS Online'
    

    # return render_template('games.html', title = titulo, year = ano, category =  categoria, players = jogadores)

#se for executado diretamente pelo interpretador

if __name__ == "__main__":
    ##Rodando a aplicação no localhost, na porta 5000, com debugg ligado pra atualizar automaticamente
    app.run(host='localhost', port=5000, debug=True)
