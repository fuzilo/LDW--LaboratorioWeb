from flask import render_template, request, url_for, redirect
from models.database import Game
import urllib
import json

jogadores = []
gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                                game=game,
                                jogadores=jogadores)
        
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        
        return render_template('cadgames.html',
                                gamelist=gamelist)
    
    @app.route('/apigames', methods=['GET', 'POST'])
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):
        url = 'https://www.freetogame.com/api/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)
        if id:
            ginfo = []
            for g in gamesjson:
                if g['id'] == id:
                    ginfo=g
                    break
            if ginfo:
                return render_template('gameinfo.html', ginfo=ginfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gamesjson=gamesjson)
    
    # CRUD - LISTAGEM, CADASTRO E EXCLUSÃO     
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<id>')
    def estoque(id=None):
        if id:
            # Deleta o cadastro pelo ID
            Game.delete(id)
            return redirect(url_for('estoque'))
        # Cadastra um novo jogo
        if request.method == 'POST':
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'], request.form['plataforma'], request.form['preco'], request.form['quantidade'])
            Game.save(newgame)
            return redirect(url_for('estoque'))
        else:
            gamesestoque = Game.get_all()
            return render_template('estoque.html', gamesestoque=gamesestoque)
    
    #Crud - Rota de Edição
    
    @app.route('/edit/<id>', methods=['GET', 'POST'])
    def edit(id):
        #Selecionando um Registro pelo ID
        g = Game.get_by_id(id)
        # Edita o jogo com as informações do Formulário
        
        if request.method == 'POST':
            editedgame = Game(request.form['titulo'],
                              request.form['ano'],
                              request.form['categoria'],
                              request.form['plataforma'],
                              request.form['preco'],
                              request.form['quantidade'])
            print (editedgame)
            Game.update(editedgame, id)
            return redirect(url_for('estoque'))
        return render_template('editgame.html', g=g)