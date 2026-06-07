from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Medico(UserMixin, db.Model):
    __tablename__ = "medicos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    especialidade = db.Column(
        db.String(100),
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    consultas = db.relationship(
        "Consulta",
        backref="medico",
        lazy=True
    )

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)