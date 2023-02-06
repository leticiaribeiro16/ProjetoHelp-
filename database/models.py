from database.database import db
from flask_login import UserMixin

# USUÁRIO
class Usuario(db.Model, UserMixin):
  __tablename__= "usuario"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  matricula = db.Column(db.String(100))
  senha = db.Column(db.String(100))
  admin = db.Column(db.Boolean)
  professor = db.Column(db.Boolean)

  def __init__(self, nome, email, matricula, senha, admin, professor):
    self.nome = nome
    self.email = email
    self.matricula = matricula
    self.senha = senha
    self.admin = admin
    self.professor = professor
  
  def __repr__(self):
    return "<Usuario {}>".format(self.nome)

# EDITAL
class Edital(db.Model):
  __tablename__= "edital"
  id = db.Column(db.Integer, primary_key = True)
  titulo = db.Column(db.String(100))
  paragrafo = db.Column(db.String(100))
  link = db.Column(db.String(100))

  def __init__(self, titulo, paragrafo, link):
    self.titulo = titulo
    self.paragrafo = paragrafo
    self.link = link
  
  def __repr__(self):
    return "<Edital {}>".format(self.titulo)

# DEMANDA
class Demanda(db.Model):
  __tablename__= "demanda"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  materia = db.Column(db.String(100))
  observacoes = db.Column(db.Text)
  requisitos = db.Column(db.Text)
  conteudo = db.Column(db.Text)
  orientadores = db.Column(db.Text)
  id_edital = db.Column(db.Integer, db.ForeignKey('edital.id'))
  modalidade = db.Column(db.Text)
  validacao = db.Column(db.Boolean)
  vagas_matutino = db.Column(db.Float)
  vagas_vespertino = db.Column(db.Float)
  vagas_noturno = db.Column(db.Float)
  vagas_flexivel = db.Column(db.Float)
  bolsas = db.Column(db.Float)

  edital = db.relationship('Edital', foreign_keys=id_edital)

  def __init__(self, materia, observacoes, requisitos, conteudo, orientadores, id_edital, modalidade, validacao, vagas_matutino, vagas_vespertino, vagas_noturno, vagas_flexivel, bolsas):
    self.materia = materia
    self.observacoes = observacoes
    self.requisitos = requisitos
    self.conteudo = conteudo
    self.orientadores = orientadores
    self.id_edital = id_edital
    self.modalidade = modalidade
    self.validacao = validacao
    self.vagas_matutino = vagas_matutino
    self.vagas_vespertino = vagas_vespertino
    self.vagas_noturno = vagas_noturno
    self.vagas_flexivel = vagas_flexivel
    self.bolsas = bolsas
    
    def __repr__(self):
      return "<Demanda {} - {} >".format(self.materia, self.edital.titulo)

# INSCRIÇÃO
class Inscricao(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.matricula'))
  id_edital = db.Column(db.Integer, db.ForeignKey('edital.id'))
  turno = db.Column(db.String(100))
  
  usuario = db.relationship('Usuario', foreign_keys=id_usuario)
  edital = db.relationship('Edital', foreign_keys=id_edital)
  
  def __init__(self, id_usuario, id_edital, turno):
    self.id_usuario = id_usuario
    self.id_edital = id_edital
    self.turno = turno

  def __repr__(self):
    return "<Inscricao {} - {} - {} - {} - {} ".format(self.usuario.nome, self.usuario.email, self.usuario.matricula, self.edital.titulo, self.turno)

# APROVAÇÃO
class Aprovacao(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.matricula'))
  nota = db.Column(db.Float)
  aprovacao = db.Column(db.Boolean)
  
  usuario = db.relationship('Usuario', foreign_keys=id_usuario)
  
  def __init__(self, id_usuario, nota, aprovacao):
    self.id_usuario = id_usuario
    self.nota = nota
    self.aprovacao = aprovacao

  def __repr__(self):
    return "<Aprovacao {} - {} - {} - {} - {}".format(self.usuario.nome, self.usuario.email, self.usuario.matricula, self.nota, self.aprovacao)