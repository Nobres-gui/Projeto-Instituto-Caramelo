import os;
from app import app;
from flask_wtf import FlaskForm;
from wtforms import StringField, validators, SubmitField;


class FormularioUsuarios(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1 ,max=30)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=1 ,max=50)]) 
    senha = StringField('Senha', [validators.DataRequired(), validators.Length(min=1 ,max=100)])
    

class FormularioAnimais(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1 ,max=20)])
    tipo = StringField('Tipo', [validators.DataRequired(), validators.Length(min=1 ,max=10)]) 
    idade = StringField('Idade', [validators.DataRequired(), validators.Length(min=1 ,max=50)])
    sexo = StringField('Sexo', [validators.DataRequired(), validators.Length(min=1 ,max=10)])
    descricao = StringField('Descrição', [validators.DataRequired(), validators.Length(min=1 ,max=200)])
    
    adicionar = SubmitField("Adicionar");
    
    
def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo;
        
    return "capa_padrao.jpg"

def deletaCapa(id):
    arquivo = recupera_imagem(id);
    if arquivo != "capa_padrao.jpg":
        os.remove(os.path.join(app.config["UPLOAD_PATH"], arquivo));