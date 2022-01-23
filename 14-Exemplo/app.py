from flask import render_template, request
from models import Postagem
from conf import app

#rotas
#esta aplicação possui apenas selects simples para teste
#digite estas rotas em seu browser para testar
@app.route('/')
def index():
    postagem = Postagem.query.all()
    return render_template('index.html', postagem=postagem)

@app.route('/desc')
def desc():
    postagem = Postagem.query.order_by(Postagem.id.desc()).all()
    return render_template('index.html', postagem=postagem)

@app.route('/primeiro')
def primeiro():
    postagem = Postagem.query.filter(Postagem.titulo == 'primeira postagem').all()
    return render_template('index.html', postagem=postagem)

@app.route('/segundo')
def segundo():
    postagem = Postagem.query.filter(Postagem.id == 2).all()
    return render_template('index.html', postagem=postagem)

@app.route('/busca', methods=['GET', 'POST'])
def busca():
    tag = request.form["titulo"]
    filtro = "%{}%".format(tag)
    postagem = Postagem.query.filter(Postagem.titulo.like(filtro)).all()
    return render_template('index.html', postagem=postagem)

#rodando aplicacao
#a aplicação rada na porta 5000
if __name__ == "__main__":
    app.run(debug=True)