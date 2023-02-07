from flask import render_template, request, redirect, flash, Blueprint, url_for
from database.models import Aprovacao
from database.database import db
from flask_login import login_user, logout_user, login_required, current_user

bp_aprovacao = Blueprint("aprovacao", __name__, template_folder='templates')

# LISTAR APROVADOS
@bp_aprovacao.route('/recovery')
@login_required
def recovery():
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')
  
  aprovacao = Aprovacao.query.all()
  return render_template('aprovacao_recovery.html', aprovacao = aprovacao)

# CREATE APROVADOS
@bp_aprovacao.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  if not current_user.admin:
    return redirect('/login')
    
  if request.method=='GET':
    aprovacao = Aprovacao.query.all()
    return render_template('aprovacao_create.html', aprovacao=aprovacao)

  if request.method=='POST':
    if request.form.get('aprovacao') == 'True':
      aprovacao = True
    else:
      aprovacao = False
    id_usuario = request.form.get('id_usuario')
    nota = request.form.get('nota')
    aprovacao = aprovacao
    resultado = Aprovacao(id_usuario, nota, aprovacao)
    db.session.add(resultado)
    db.session.commit()

    return redirect(url_for('.recovery'))
  

# ATUALIZAR APROVADOS
@bp_aprovacao.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')
    
  resultado = Aprovacao.query.get(id)
  if id and request.method=='GET':
    return render_template('aprovacao_update.html', resultado=resultado)
    
  if request.method=='POST':
    id_usuario = request.form.get('id_usuario')
    nota = request.form.get('nota')
    aprovacao = request.form.get('aprovacao')
    
    resultado.id_usuario = id_usuario
    resultado.nota = nota
    resultado.aprovacao = eval(aprovacao)

    db.session.add(resultado) 
    db.session.commit()
    return redirect(url_for('.recovery', id=id))

# DELETE APROVADOS
@bp_aprovacao.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  if not current_user.admin:
    return redirect('/login')
    
  if id==0:
    return 'É preciso definir um resultado para ser excluído'
    return redirect(url_for('.recovery'))

  if request.method == 'GET':
    resultado = Aprovacao.query.get(id)
    return render_template('aprovacao_delete.html', resultado = resultado)

  if request.method == 'POST':
    resultado = Aprovacao.query.get(id)
    db.session.delete(resultado)
    db.session.commit()
    return redirect(url_for('.recovery'))