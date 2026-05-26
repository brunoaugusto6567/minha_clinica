from app import db
from datetime import datetime


class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)

    especialidade = db.Column(db.String(100), nullable=False)

    tipo_consulta = db.Column(db.String(50), nullable=False)

    data = db.Column(db.String(20), nullable=False)

    horario = db.Column(db.String(10), nullable=False)

    status = db.Column(db.String(50), default='Agendada')

    retorno = db.Column(db.Boolean, default=False)

    link_teleconsulta = db.Column(db.String(255))

    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    paciente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))