from flask import render_template, request

interesse=[]
itens =[{'Nome': 'Colar do Rei Salomão', 'Data': '11/03/2024', 'Valor':'150.000.000','Última Aparição na loja':'01/02/2024'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/maisprocurados', methods=['GET', 'POST'])
    def procurados():
        if request.method == 'POST':
            if request.form.get('procurados'):
                interesse.append(request.form.get('procurados'))
            
    return render_template('items.html', itens=itens, interesse=interesse)
    
    @app.route('catalogo', methods=['GET', 'POST'])
    def catalogo():
        if request.method =='POST':
            if request.form.get('item') and request.form.get('data') and request.form.get('valor') and request.form.get('ultima'):
                itens.append({'Item':request.form.get('item'),'Data':request.form.get('data'),'Valor':request.form.get('valor'),'Última Aparição na loja':request.form.get('ultima')})
        return render_template('catalogo.html', itens=itens)