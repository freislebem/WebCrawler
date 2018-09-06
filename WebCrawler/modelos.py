import app
import os
from flask_sqlalchemy import SQLAlchemy

app = app(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Site(app.db.Model):
    __tablename__ = 'sites'
    db = app(db)
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(64), unique=True)
    enderecoSite = db.Column(db.String(64), unique=True)
    palavrasChave = db.Column(db.String(64), unique=True)

    id_usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id'))#conferir relacionamento
    id_clientes = db.Column(db.Integer, db.ForeignKey('clientes.id'))#conferir relacionamento

    def __repr__(self):
        return '<Site %r>' % self.descricao

class Usuario(app.db.Model):
    __tablename__ = 'usuarios'
    db = app(db)
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)

    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))#conferir relacionamento

    def __repr__(self):
        return '<Usuario %r>' % self.nome

class Cliente(app.db.Model):
    __tablename__ = 'clientes'
    db = app.db
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)

    usuarios = db.relationship('Usuario', backref='usuario')#conferir relacionamento

    def __repr__(self):
        return '<Cliente %r>' % self.nome