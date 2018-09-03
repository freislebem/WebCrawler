from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class novoSite:
    def __init__(self, FlaskForm):
        self.nomeSite = StringField('Nome do site', validators = [DataRequired()])
        self.enderecoSite = StringField('Endereco do site', validators = [DataRequired()])
        self.palavrasChave = StringField('Palavra-chave', validators = [DataRequired()])
        self.submit = SubmitField('Enviar')
