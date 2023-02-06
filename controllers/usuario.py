from flask import render_template, request, redirect, flash, Blueprint, url_for
from database.models import Usuario
from database.database import db, lm
from flask_login import login_user, logout_user, login_required, current_user

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

#LISTAR TODOS OS USUÁRIOS
@bp_usuarios.route('/recovery')
@login_required
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuarios_recovery.html', usuarios = usuarios)

#CRIAR USUÁRIOS
@bp_usuarios.route('/create', methods=['POST', 'GET'])
def cadastro():
  if request.method=='GET':
    return render_template('login.html')
  
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')
    
    usuario = Usuario(nome, email, matricula, senha)
    db.session.add(usuario)
    db.session.commit()

    return redirect('/login')

#ATUALIZAR USUÁRIOS
@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    
  usuario = Usuario.query.get(id)
  if id and request.method=='GET':
    return render_template('usuarios_update.html', usuario=usuario)
    
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')
    
    usuario.nome = nome
    usuario.email = email
    usuario.matricula = matricula
    usuario.senha = senha

    db.session.add(usuario) 
    db.session.commit()
    return redirect(url_for('.recovery', id=id))

#DELETAR USUÁRIOS
@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  if id==0:
    return 'É preciso definir um usuário para ser excluído'
    return redirect(url_for('usuarios'))

  if request.method == 'GET':
    usuario = Usuario.query.get(id)
    return render_template('usuarios_delete.html', usuario = usuario)

  if request.method == 'POST':
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('.recovery'))

#AUTENTICAÇÃO
@lm.user_loader
def load_user(id):
  usuario = Usuario.query.filter_by(id=id).first()
  return usuario

@bp_usuarios.route('/dashboard', methods=['POST'])
def login():
  matricula = request.form.get('matricula')
  senha = request.form.get('senha')
  usuario = Usuario.query.filter_by(matricula = matricula).first()
  print(usuario)
  if usuario and (senha == usuario.senha):
    login_user(usuario)
    return render_template('index.html', usuario = usuario)
  else:
    return 'dados incorretos'
    return redirect('/')

@bp_usuarios.route('/logoff')
@login_required
def logoff():
  logout_user()
  return redirect('/')