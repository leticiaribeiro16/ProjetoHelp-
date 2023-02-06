from flask import Blueprint
from flask import render_template, request, redirect, url_for
from database.models import Demanda
from database.database import db
from flask_login import login_required, current_user

bp_demanda = Blueprint("demanda", __name__, template_folder="templates")

#CRIAR DEMANDA
@bp_demanda.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('demanda_create.html')

  if request.method=='POST':
    materia = request.form.get('materia')
    observacoes = request.form.get('observacoes')
    requisitos = request.form.get('requisitos')
    conteudo = request.form.get('conteudo')
    orientadores = request.form.get('orientadores')
    id_edital = request.form.get('id_edital')
    modalidade = request.form.get('modalidade')
    validacao = request.form.get('validacao')
    vagas_matutino = request.form.get('vagas_matutino')
    vagas_vespertino = request.form.get('vagas_vespertino')
    vagas_noturno = request.form.get('vagas_noturno')
    vagas_flexivel = request.form.get('vagas_flexivel')
    
    demanda = Demanda(materia, observacoes, requisitos, conteudo, orientadores, id_edital, modalidade, validacao, vagas_matutino, vagas_vespertino, vagas_noturno, vagas_flexivel, 0)
    db.session.add(demanda) 
    db.session.commit()
    return redirect('/demanda/recovery')

#LISTAR DEMANDAS
@bp_demanda.route('/recovery')
def recovery():
  demanda = Demanda.query.all()
  return render_template('demanda_recovery.html', demanda=demanda)

#ATUALIZAR DEMANDA
@bp_demanda.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if not current_user.professor:
    return 'Acesso não permitido'
    return redirect('/login')
    
  if id and request.method=='GET':
    demanda = Demanda.query.get(id)
    return render_template('demanda_update.html', demanda=demanda)

  if request.method=='POST':
    demanda = Demanda.query.get(id)
    demanda.materia = request.form.get('materia')
    demanda.observacoes = request.form.get('observacoes')
    demanda.requisitos = request.form.get('requisitos')
    demanda.conteudo = request.form.get('conteudo')
    demanda.orientadores = request.form.get('orientadores')
    demanda.id_edital = request.form.get('id_edital')  
    demanda.modalidade = request.form.get('modalidade')
    demanda.validacao = request.form.get('validacao')
    demanda.vagas_matutino = request.form.get('vagas_matutino')
    demanda.vagas_vespertino = request.form.get('vagas_vespertino')
    demanda.vagas_noturno = request.form.get('vagas_noturno')
    demanda.vagas_flexivel = request.form.get('vagas_flexivel')
    demanda.bolsas = request.form.get('bolsas')

  db.session.add(demanda) 
  db.session.commit()
  return redirect(url_for('.recovery', id=id))

#DELETAR DEMANDA
@bp_demanda.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  if not current_user.professor:
    return 'Acesso não permitido'
    return redirect('/login')
    
  if request.method == 'GET':
    demanda = Demanda.query.get(id)
    return render_template('demanda_delete.html', demanda = demanda)

  if request.method == 'POST':
    demanda = Demanda.query.get(id)
    db.session.delete(demanda)
    db.session.commit()
    return redirect('/demanda/recovery')