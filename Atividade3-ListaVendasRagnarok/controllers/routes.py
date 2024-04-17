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
            senha = Usuario.query.filter_by(password=password).first()
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


    
    @app.route('/maisprocurados', methods=['GET', 'POST'])
    def procurados():
        if request.method == 'POST':
            if request.form.get('item'):
                interesse.append(request.form.get('item'))
            
        return render_template('items.html', interesse=interesse)
    
    @app.route('/catalogo', methods=['GET', 'POST'])
    def catalogo():
        if request.method =='POST':
            if request.form.get('item') and request.form.get('data') and request.form.get('valor') and request.form.get('ultima'):
                itens.append({'Item':request.form.get('item'),'Data':request.form.get('data'),'Valor':request.form.get('valor'),'Ultima':request.form.get('ultima')})
        return render_template('catalogo.html', itens=itens)