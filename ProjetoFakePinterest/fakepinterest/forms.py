#formularios do nosso site
from flask_wtf import FlaskForm #formularios
from wtforms import StringField, PasswordField, SubmitField, FileField #campos de texto, senha, botao submit e enviar arquivos
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError #validacoes de preenchimento necessario, checar se é um email valido, comparacao para caso da confirmacao da senha, tamanho necessario de caracteres para senha, e mostrar erros de preenchimento de formulario
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')
      
    def validate_email(self, email): #validate_'nome do campo validando'
        usuario = Usuario.query.filter_by(email=email.data).first() #email da classe usuario = email da classe FormLogin
        if not usuario:
            raise ValidationError('E-mail não cadastrado, cadastre-se para continuar')


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Criar Conta')
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() #email da classe usuario = email da classe FormCriarConta
        if usuario:
            raise ValidationError('E-mail já cadastrado, faça login para continuar')
        

class FormFoto(FlaskForm):
    foto = FileField('Imagem', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Upload Foto')