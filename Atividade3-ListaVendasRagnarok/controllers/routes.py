from flask import render_template, request, url_for, redirect, flash, session
from markupsafe import Markup
from models.database import db, #(importar as classes do banco)
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






    @app.route('/')
    def home():
        return render_template('index.html')
    
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