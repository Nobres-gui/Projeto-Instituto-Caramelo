from app import app, db;
from models import Usuarios, Animais;
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory;
from helpers import FormularioUsuarios, FormularioAnimais, recupera_imagem, deletaCapa;
from flask_bcrypt import check_password_hash, generate_password_hash;
import time;



@app.route("/")
def index():
    return render_template("index.html");

@app.route("/cadastro")
def cadastro():
    form = FormularioUsuarios();
    return render_template("cadastro.html", titulo = "Cadastro", form=form);

@app.route("/criarUsuario", methods=["POST", ])
def criarUsuario():
    form = FormularioUsuarios(request.form);
    funcionarioEmail = "ong.com"
    nome = form.nome.data;
    email  = form.email.data;
    senha = generate_password_hash(form.senha.data).decode("utf-8");
    
    if funcionarioEmail in email: 
        novo_Usuario = Usuarios(nome=nome, email=email, senha=senha,funcionario="sim") # type: ignore
    else:    
        novo_Usuario = Usuarios(nome=nome, email=email, senha=senha) # type: ignore
    
    
    db.session.add(novo_Usuario); 
    db.session.commit();
    return redirect(url_for("login", proxima = url_for("index")));

@app.route("/login")
def login():
    proxima = request.args.get("proxima");
    print(proxima)
    form = FormularioUsuarios();
    return render_template("login.html", titulo = "Login", proxima=proxima, form = form);

@app.route("/autenticar", methods=["POST",])
def autenticar():
    form = FormularioUsuarios(request.form);
    usuario = Usuarios.query.filter_by(email=form.email.data).first();
    senha = check_password_hash(usuario.senha, form.senha.data);
    session["Funcionario?"] = usuario.funcionario;
    if usuario and senha:
        session["usuario_logado"] = usuario.nome;
        proxima = request.form["proxima"];  
        return redirect(url_for("adocao", funcionario=session["Funcionario?"]));
    else:
        proxima = request.form["proxima"];  
        # form.aviso.data = "Usuário ou senha inválidos";
        return redirect(url_for("login", proxima=proxima))
    
@app.route("/adocao")
def adocao():
    form = FormularioAnimais();
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        return redirect(url_for("login", proxima=url_for("adocao")));
    animais_lista = Animais.query.order_by(Animais.idAnimal)
       
    for animais in animais_lista:
        animaisLista = Animais.query.order_by(Animais.idAnimal).first()
        listaAnimais = { 
        "nome" : animaisLista.nome , 
        "idade" : animaisLista.idade , 
        "tipo" : animaisLista.tipo , 
        "sexo" : animaisLista.sexo , 
        "descricao" : animaisLista.descricao
        }
        
        
    
    return render_template("adocao.html", animais=animais_lista , funcionario=session["Funcionario?"], listaAnimais=listaAnimais, form=form)


@app.route("/novoAnimal", methods=["POST",])
def novoAnimal():
    form = FormularioAnimais(request.form);
    if not form.validate_on_submit():
        return redirect("novoAnimal");
    
    
    nome = form.nome.data;
    idade = form.idade.data;
    tipo = form.tipo.data;
    sexo = form.sexo.data;
    descricao = form.descricao.data;
    
    novo_Animal = Animais(nome=nome, idade=idade, tipo=tipo,sexo=sexo, descricao=descricao); # type: ignore
    db.session.add(novo_Animal); 
    db.session.commit();
    
    arquivo = request.files["Img-arq"];
    
    upload_path = app.config["UPLOAD_PATH"]
    timestamp = time.time();
    deletaCapa(novo_Animal.idAnimal);
    arquivo.save(f"{upload_path}/capa{novo_Animal.idAnimal}-{timestamp}.jpg" );
    return redirect(url_for('adocao'));

@app.route("/uploads/<nome_arquivo>")
def imagem(nome_arquivo):
    return send_from_directory("uploads", nome_arquivo)

@app.route("/logout")
def logout():
    session["usuario_logado"] = None;
    flash("Logout efetuado com sucesso!!!");
    return redirect(url_for("index"));