from flask import render_template, request, redirect, flash, Blueprint, url_for
from database.models import Inscricao
from database.database import db, lm
from flask_login import login_user, logout_user, login_required, current_user

bp_inscricao = Blueprint("inscricao", __name__, template_folder='templates')

#CRIAR INSCRIÇÕES
@bp_inscricao.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  if request.method=='GET':
    return render_template('inscricao_create.html')

  if request.method=='POST':
    id_usuario = request.form.get('id_usuario')
    id_edital = request.form.get('id_edital')
    turno = request.form.get('turno')
    
    i = Inscricao(id_usuario, id_edital, turno)
    db.session.add(i) 
    db.session.commit()
    return redirect('/usuarios/dashboard')
    # return redirect(url_for('.recovery'))

#LISTAR INSCRIÇÕES
@bp_inscricao.route('/recovery')
@login_required
def recovery():
  inscricao = Inscricao.query.all()
  return render_template('inscricao_recovery.html', inscricao=inscricao)

#ATUALIZAR INSCRIÇÕES
@bp_inscricao.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if id and request.method=='GET':
    inscricao = Inscricao.query.get(id)
    return render_template('inscricao_update.html', inscricao=inscricao)
  
  if request.method=='POST':
    inscricao = Inscricao.query.get(id)
    inscricao.id_usuario = request.form.get('id_usuario')
    inscricao.id_edital = request.form.get('id_edital')
    inscricao.turno = request.form.get('turno')

  db.session.add(inscricao) 
  db.session.commit()
  return redirect(url_for('.recovery', id=id))

#DELETAR INSCRIÇÕES
@bp_inscricao.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  if not current_user.admin:
    return redirect('/login')
    
  if id==0:
    return 'É preciso definir uma inscrição para ser excluído'
    return redirect(url_for('.recovery'))

  if request.method == 'GET':
    inscricao = Inscricao.query.get(id)
    return render_template('inscricao_delete.html', inscricao = inscricao)

  if request.method == 'POST':
    inscricao = Inscricao.query.get(id)
    db.session.delete(inscricao)
    db.session.commit()
    return redirect(url_for('.recovery'))