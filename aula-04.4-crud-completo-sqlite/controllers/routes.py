from flask import render_template, request, url_for, redirect
from models.database import Game
import urllib
import json
from bson import ObjectId


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
    
    # CRUD - LISTAGEM, CADASTRO      
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<id>')
        #Cadastro de um novo Jogo
    def estoque(id=None):
        if id:
            #deleta o cadastro deplo ID
            Game.delete(id)
            return redirect(url_for('estoque'))
            
        if request.method == 'POST':
            newgame = Game(
                            request.form['titulo'],
                            request.form['ano'],
                            request.form['categoria'],
                            request.form['plataforma'],
                            request.form['preco'],
                            request.form['quantidade']
            )
            Game.save(newgame)
            return redirect(url_for('estoque'))
        else:
            gamesestoque = Game.get_all()
            return render_template('estoque.html', gamesestoque=gamesestoque)
       

        
        
        
    # # CRUD - EDIÇÃO
    # @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    # def edit(id):
    #     g =  Game.query.get(id)
    #     # Edita o jogo com as informações do formulário
    #     if request.method == 'POST':
    #         g.titulo = request.form['titulo']
    #         g.ano = request.form['ano']
    #         g.categoria = request.form['categoria']
    #         g.plataforma = request.form['plataforma']
    #         g.preco = request.form['preco']
    #         g.quantidade = request.form['quantidade']
    #         db.session.commit()
    #         return redirect(url_for('estoque'))
    #     return render_template('editgame.html', g=g)