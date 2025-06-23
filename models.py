from app import db;

class Usuarios(db.Model):
    email = db.Column(db.String(30), primary_key=True);
    nome = db.Column(db.String(50), nullable=False);
    senha = db.Column(db.String(100), nullable=False); 
    funcionario = db.Column(db.String(3), nullable=False); 

    def __repr__(self):
        return "<Name %r>" % self.nome;
    
    
class Animais(db.Model):
    idAnimal = db.Column(db.Integer, primary_key=True, autoincrement=True);
    nome = db.Column(db.String(20), nullable=False);
    tipo = db.Column(db.String(10), nullable=False);
    idade = db.Column(db.Integer(), nullable=False);
    sexo = db.Column(db.String(10), nullable=False);
    descricao = db.Column(db.String(200), nullable=False);
    # dataInclusao = db.Column(db.String(), nullable=False);
    
    def __repr__(self):
        return "<Name %r>" % self.nome;
    
    
