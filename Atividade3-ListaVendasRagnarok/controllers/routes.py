from flask import render_template, request, url_for, redirect, flash, session
from markupsafe import Markup
from models.database import db, Usuario #(importar as classes do banco)
from werkzeug.security import generate_password_hash, check_password_hash

import urllib
import json 
import uuid
import os


interesse=[]
itens =[{'Item': 'Colar do Rei Salomão', 'Data': '11/03/2024', 'Valor':'150.000.000','Ultima':'01/02/2024'}]

def init_app(app):
    #Função middleware para verificar a autenticação do usuário

    def check_auth():
        routes = ['login', 'caduser', 'home']
        #Se a rota atual não requer autenticação, permite o acesso
        if request.endpoint in routes or request.path.startswith('/static/'):
            return
        #Se o usuário não estiver autenticado, redireciona-o para a página de login
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
    #Rota Principal
    @app.route('/')
    def home():
        return render_template('index.html')
    
    #Rota de Login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = Usuario.query.filter_by(email=email).first()
            #senha = Usuario.query.filter_by(password=password).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.mail
                nickname = user.email.split('@')
                flash(f'Logado com sucesso! Bem vindo {nickname[0]}','success')
                return redirect(url_for('home'))
            else: 
                   
                flash('Falha no login. Verifique seu nome de usuário e Senha', 'danger')

        return render_template('login.html')        

    #Rota de Logout
    @app.route('/logout', methods=['GET','POST'])
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
                msg = Markup("Usuário já cadastrado. Faça <a href='/login'>Login</a>")
                flash(msg,'danger')
                return redirect(url_for('caduser'))
            else:
                hashed_passsword = generate_password_hash(password, method='scrypt')
                new_user = Usuario(email=email, password=hashed_passsword)
                db.session.add(new_user)
                db.sesseion.commit()

                flash('Registro realizado com sucesso! Faça o login', 'success')
                return redirect(url_for('login')) 
            
        return render_template('caduser.html')

    
    @app.route('/maisprocurados', methods=['GET', 'POST'])
    def procurados():
        if request.method == 'POST':
            if request.form.get('item'):
                interesse.append(request.form.get('item'))
            
        return render_template('items.html', interesse=interesse)
    
    @app.route('/catalogo', methods=['GET', 'POST'])
    @app.route('/catalogo/delete/<int:id>')
    
    def catalogo():
        #Excluindo um registro
        if id:
            item = catalogo.query.get(id)
            db.session.delete(item)
            db.session.commit()
            return redirect(url_for('catalogo'))
        
        #Incluindo novo registro
        if request.method =='POST':
            novo_item = catalogo(request.form['item'], request.form['data'], request.form['valor'],request.form['ultima'])
            db.sesseion.add(novo_item)
            db.session.commit()
            return redirect(url_for('catalogo'))
        else:
            #Armazenando em 'lista_itens' todos os registro da tabela catalogo
            #Captura o valor de 'page' que foi passado pelo método GET
            #Define o padrão, valor 1 e Int
            page = request.args.get('page', 1, type=int)

            #Valor padrão de registro por página
            per_page=10

            itens_page = catalogo.query.paginate(page=page, per_page=per_page)
            return render_template('estoque.html', itens_catalogo=itens_page)
        
    #Crud - Edição de Dados
    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
            g=catalogo.query.get(id)

            #Editando o jogo com as informações do formulário
            if request.method =='POST':
                g.item = request.form['item']
                g.data = request.form['data']
                g.valor = request.form['valor']
                g.ultima = request.form['ultima']
                db.session.commit()
                return redirect(url_for('catalogo'))
            return render_template('editcatalogo.html', g=g)


