import app

class Site(app.db.Model):
    __tablename__ = 'sites'
    db = app.db
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    descricao = db.Column(db.String(64), unique=True)
    enderecoSite = db.Column(db.String(64), unique=True)
    palavrasChave = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Site %r>' % self.descricao

class Usuario(app.db.Model):
    __tablename__ = 'usuarios'
    db = app.db
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    nome = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Usuario %r>' % self.nome

class Cliente(app.db.Model):
    __tablename__ = 'clientes'
    db = app.db
    id = db.Column(db.Integer, primary_key=True)
    id_sites = db.Column(db.Integer)
    nome = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Cliente %r>' % self.nome