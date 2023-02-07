from flask import Flask, render_template, redirect, Blueprint
from database.database import db
from flask_migrate import Migrate
from controllers.usuario import bp_usuarios
from controllers.edital import bp_edital
from controllers.demanda import bp_demanda
from controllers.inscricao import bp_inscricao
from controllers.aprovacao import bp_aprovacao
from database.database import db, lm
from flask_login import login_user, logout_user, login_required, current_user
from database.models import Usuario
from database.models import Edital
from database.models import Demanda
from database.models import Inscricao
from database.models import Aprovacao

app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_edital, url_prefix='/edital')
app.register_blueprint(bp_demanda, url_prefix='/demanda')
app.register_blueprint(bp_inscricao, url_prefix='/inscricao')
app.register_blueprint(bp_aprovacao, url_prefix='/aprovacao')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

#banco de dados
conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

@app.route('/')
def principal(): 
  if current_user.is_authenticated:
    edital = Edital.query.all()
    return render_template('index.html', edital=edital)
  else:
    return redirect('/login')

@app.route('/usuarios/dashboard')
def index():
  if current_user.is_authenticated:
    edital = Edital.query.all()
    return render_template('index.html', edital=edital)
  else:
    return redirect('/login')
  
@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(401)
def acesso_negado(e):
    return render_template('error_401.html'), 404

@app.errorhandler(404)
def error_404(e):
    return render_template('error_404.html'), 404

app.run(host='0.0.0.0', port=81)
