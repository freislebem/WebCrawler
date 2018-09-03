from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
#import novoSite

app = Flask(__name__)
app.config['SECRET_KEY'] = 'galo roberto'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    session['usuario'] = 'Freislebem'
    return render_template('index.html', usuario=session.get('usuario'), titulo = 'WebCrawler PyDenis')

@app.route('/principal')
def principal():
    return render_template('principal.html', titulo = 'WebCrawler PyDenis - Painel de Funções')

@app.route('/forms/formNovoSite', methods=['GET', 'POST'])
def formNovoSite():
    nomeSite = None
    enderecoSite = None
    palavrasChave = None
    form = novoSite()
    if form.validate_on_submit():
        nomeSite = form.nomeSite.data
        enderecoSite = form.enderecoSite.data
        palavrasChave = form.palavrasChave.data
        form.nomeSite.data, form.enderecoSite.data, form.palavrasChave.data = ''
    else: 
        flash('Por favor, preencha todos os campos')
    return render_template('/forms/formNovoSite.html', usuario=session.get('usuario'), titulo='DADOS DO SITE PARA PESQUISA', form=form, nomeSite = nomeSite, enderecoSite=enderecoSite, palavrasChave=palavrasChave)

@app.errorhandler(404)
def pag_nao_encontrada(e):
    return render_template('404.html', titulo='WebCrawler PyDenis - Pagina nao encontrada'), 404

@app.errorhandler(500)
def erro_interno(e):
    return render_template('500.html', titulo='WebCrawler PyDenis - Erro Interno', e=e), 500

class novoSite(FlaskForm):
    nomeSite = StringField('Nome do site', validators = [DataRequired()])
    enderecoSite = StringField('Endereco do site', validators = [DataRequired()])
    palavrasChave = StringField('Palavra-chave', validators = [DataRequired()])
    submit = SubmitField('Enviar')
    bootstrap = Bootstrap(app)

app.run(debug=True)