from flask import render_template

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/game')
    def game():
        game = {'Titulo': 'CS-GO',
            'Ano' : 2012,
            'Categoria' : 'FPS-Online'
            }
    jogadores=['Fabio', 'Sequela', 'Tiriça', '3ovo']
    return render_template('games.html', game = game, players = jogadores)
