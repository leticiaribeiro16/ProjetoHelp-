from flask import Flask, render_template, redirect, Blueprint
from database.database import db
from flask_migrate import Migrate
from database.models import Usuario
from controllers.usuario import bp_usuarios
from database.database import db, lm
from flask_login import login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

#banco de dados
conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def principal(): 
  return render_template('login.html')

@app.route('/usuarios/dashboard')
def index():
	if current_user.is_authenticated:
		return render_template('index.html')
	else:
		return redirect('/login')
  
@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(401)
def acesso_negado(e):
    return render_template('error_401.html'), 404

app.run(host='0.0.0.0', port=81)
