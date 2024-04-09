from flask import render_template, request, url_for, redirect, flash, session
from markupsafe import Markup
from models.database import db, Game, Usuario
from werkzeug.security import generate_password_hash, check_password_hash

import urllib
import json

jogadores = []
jogos = []
gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

def init_app(app):
    
    
    #Função de Middleware para verificar a autenticação do usuário
    @app.before_request
    def check_auth():
        routes = ['login', 'caduser', 'home']
        #Se a rota atual não requer autenticação, permite o acesso
        if request.endpoint in routes or request.path.startswith('/static/'):
            return
        #Se o ususário não estiver autenticado, rediciona-o para a página de login
        if 'user_id' not in session:
            return redirect(url_for('login'))
            
            
    
    # Definindo a rota principal
    @app.route('/')
    # Função que será executada ao acessar a rota
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')
    
    #Rota Login
    @app.route('/login', methods=['GET', 'POST'])
   
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = Usuario.query.filter_by(email =email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.email
                nickname = user.email.split('@')
                flash(f'Login em sucedido! Bem vindo {nickname[0]}','success')
                return redirect(url_for('home'))
            else:
                flash('Falha no login. Verifique seu nome de usuário e Senha', 'danger')
            
        return render_template('login.html')
    
    #Rota de Logout
    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session.clear()
        return redirect(url_for('login'))
    
    #Rota de Cadastro de Usuário
    @app.route('/caduser', methods=['GET', 'POST'])
    def caduser():
        if request.method =='POST':
            email = request.form['email']
            password = request.form['password']
            user = Usuario.query.filter_by(email=email).first()
            if user:
                msg = Markup("Usuário já cadastrado. Faça <a href='/login'> Login</a>")
                flash(msg, 'danger')
                return redirect(url_for('caduser'))
            
            else:
                hashed_password = generate_password_hash(password, method='scrypt')
                new_user = Usuario(email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                
                flash('Registro realizado com sucesso! Faça o login', 'success')
                return redirect(url_for('login'))
            
        
            
        return render_template('caduser.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                
            if request.form.get('jogo'):
                jogos.append(request.form.get('jogo'))
                
        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        return render_template('cadgames.html', gamelist=gamelist)
    
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
                    ginfo = g
                    break
            if ginfo:
                return render_template('gamesinfo.html', ginfo=ginfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:                       
            return render_template('apigames.html', gamesjson=gamesjson)
    
    # CRUD - Listagem de dados
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<int:id>')
    def estoque(id=None):
        # Excluindo um jogo
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        # Cadastrando um novo jogo
        if request.method == 'POST':
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'], request.form['plataforma'], request.form['preco'], request.form['quantidade'])
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoque'))
        else:
            # Armazenando em "gamesestoque" todos os registros da tabela Game.
            # Captura o valor de 'page ' que foi passado pelo método GET
            # Define como padrão o valor 1 e o tipo inteiro
            page = request.args.get('page', 1, type=int )
            
            #valor padrão de registros por página(definimos 3)
            
            per_page = 3
            ## Faz um Select no Banco a partir da página informada(page)
            ##Filtra os registros de 3 em 3
            
            games_page = Game.query.paginate(page=page, per_page=per_page)
            return render_template('estoque.html', gamesestoque=games_page)
    
    #Crud- Edição de dados
    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
        g= Game.query.get(id)
        
        #Editando o jogo com as informações do formulário
        
        if request.method == 'POST':
            g.titulo = request.form['titulo']
            g.ano = request.form['ano']
            g.categoria = request.form['categoria']
            g.plataforma = request.form['plataforma']
            g.preco = request.form['preco']
            g.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
            
        return render_template('editgame.html', g=g)