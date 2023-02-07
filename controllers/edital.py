from flask import render_template, request, redirect, flash, Blueprint, url_for
from database.models import Edital
from database.database import db
from flask_login import login_user, logout_user, login_required, current_user

bp_edital = Blueprint("edital", __name__, template_folder='templates')

#LISTAR EDITAL
@bp_edital.route('/recovery')
@login_required
def recovery():
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')
  
  edital = Edital.query.all()
  return render_template('edital_recovery.html', edital = edital)

#CRIAR EDITAL
@bp_edital.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')
    
  if request.method=='GET':
    return render_template('edital_create.html')

  if request.method=='POST':
    titulo = request.form.get('titulo')
    paragrafo = request.form.get('paragrafo')
    link = request.form.get('link')
    edital = Edital(titulo, paragrafo, link)
    db.session.add(edital)
    db.session.commit()

    return redirect(url_for('.recovery'))
  
#EDITAR EDITAL
@bp_edital.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')

  if id and request.method=='GET':
    edital = Edital.query.get(id)
    return render_template('edital_update.html', edital=edital)
  
  if request.method=='POST':
    edital = Edital.query.get(id)
    edital.titulo = request.form.get('titulo')
    edital.paragrafo = request.form.get('paragrafo')
    edital.link = request.form.get('link')

  db.session.add(edital) 
  db.session.commit()
  return redirect(url_for('.recovery', id=id))

#EXCLUIR EDITAL
@bp_edital.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  if not current_user.admin:
    return redirect('/login')
    
  if id==0:
    return 'É preciso definir um edital para ser excluído'
    return redirect(url_for('.recovery'))

  if request.method == 'GET':
    edital = Edital.query.get(id)
    return render_template('edital_delete.html', edital = edital)

  if request.method == 'POST':
    edital = Edital.query.get(id)
    db.session.delete(edital)
    db.session.commit()
    return redirect(url_for('.recovery'))