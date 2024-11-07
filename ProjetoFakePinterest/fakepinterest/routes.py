#criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user #restricao de login
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename #transformar nomes de arquivos enviados 


@app.route('/', methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first() #encontrando o usuario no banco de dados
        if usuario and bcrypt.check_password_hash(usuario.senha.encode('utf-8'), formlogin.senha.data): #se usuario existe e senha correta cryptografada
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)


@app.route('/criarconta', methods=["GET", "POST"])
def criar_conta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(FormCriarConta.senha.data).decode('utf-8')
        usuario = Usuario(username=FormCriarConta.username.data, 
                          email=FormCriarConta.email.data, 
                          senha=senha
                          )
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True) #faz o login automaticamente
        return redirect(url_for('perfil', id_usuario=usuario.id)) #redirecionando para o perfil do novo usuario
    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<id_usuario>', methods=["GET", "POST"]) #mudando o link conforme cada usuario
@login_required #restrito apenas a usuarios logados
def perfil(id_usuario): #mudando o link conforme cada usuario
    if int(id_usuario) == int(current_user.id):
        #o usuario vera o perfil dele
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename) #tranformar o nome do arquivo para n haver problemas com o codigo
            #salvar o arquivo na pasta fotos_posts
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), #caminho onde esse codigo esta escrito
                                   app.config['UPLOAD_FOLDER'], 
                                   nome_seguro
                                   )
            arquivo.save(caminho)
            #registrar arquivo no banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all() #para limitar quantidade de fotos colocar tbm [:200] #max 200 fotos
    return render_template('feed.html', fotos=fotos)
