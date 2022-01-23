from flask import redirect, render_template, request, url_for
from models import Postagem, db
from conf import app

#rotas
@app.route('/')
def index():
    postagem = Postagem.query.order_by(Postagem.id.desc()).all()
    return render_template('index.html', postagem=postagem)

@app.route('/busca', methods=['GET', 'POST'])
def busca():
    tag = request.form["titulo"]
    filtro = "%{}%".format(tag)
    postagem = Postagem.query.filter(Postagem.titulo.like(filtro)).all()
    return render_template('index.html', postagem=postagem)

@app.route('/add', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form["titulo"]
        conteudo = request.form["conteudo"]
        postagem = Postagem(titulo, conteudo)
        db.session.add(postagem)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    postagem = Postagem.query.get(id)
    if request.method == 'POST':
        postagem.titulo = request.form['titulo']
        postagem.conteudo = request.form['conteudo']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', postagem=postagem)

@app.route("/delete/<int:id>")
def delete(id):
    postagem = Postagem.query.get(id)
    db.session.delete(postagem)
    db.session.commit()
    return redirect(url_for('index'))

#roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)