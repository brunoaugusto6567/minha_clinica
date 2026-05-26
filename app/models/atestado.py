from app import db
from datetime import datetime


class Atestado(db.Model):
    __tablename__ = 'atestados'

    id = db.Column(db.Integer, primary_key=True)

    texto = db.Column(db.Text, nullable=False)

    data_emissao = db.Column(db.DateTime, default=datetime.utcnow)

    consulta_id = db.Column(db.Integer)