from flask import Flask,render_template, request,redirect

app = Flask(__name__)

class cadInfluencer:
    def __init__(self,nome,social,seguidor,area):
        self.nome = nome
        self.social = social
        self.seguidor = seguidor
        self.area = area

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
lista = []

@app.route('/Influencer')
def Influencer():
    return render_template('Influencer.html',Titulo = "Influencers Iniciais:",ListaInfluencer = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Influencer")

@app.route("/criar", methods= ["POST"])
def criar():
    nome = request.form["nome"]
    social = request.form["social"]
    seguidor = request.form["Seguidor"]
    area = request.form["Area"]
    obj = cadInfluencer(nome, social, seguidor, area)
    lista.append(obj)
    return redirect('/Influencer')

if __name__ == '__main__':
    app.run()