#arquivo apenas para criacao do banco de dados
from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()