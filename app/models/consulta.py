from app import db
from datetime import datetime


class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)

    # ==========================
    # Dados do paciente
    # ==========================

    nome_completo = db.Column(
        db.String(150),
        nullable=False
    )

    cpf = db.Column(
        db.Text,
        nullable=False
    )

    data_nascimento = db.Column(
        db.String(20)
    )

    sexo = db.Column(
        db.String(20)
    )

    telefone = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(120)
    )

    endereco = db.Column(
        db.String(255)
    )

    # ==========================
    # Dados da consulta
    # ==========================

    especialidade = db.Column(
        db.String(100),
        nullable=False
    )

    tipo_consulta = db.Column(
        db.String(50),
        nullable=False
    )

    data = db.Column(
        db.String(20),
        nullable=True
    )

    horario = db.Column(
        db.String(10),
        nullable=True
    )

    status = db.Column(
        db.String(50),
        default='Agendada'
    )

    retorno = db.Column(
        db.Boolean,
        default=False
    )

    link_teleconsulta = db.Column(
        db.String(255)
    )

    # ==========================
    # Dados preenchidos pelo médico
    # ==========================

    descricao_paciente = db.Column(
        db.Text
    )

    diagnostico = db.Column(
        db.Text
    )

    medicamentos = db.Column(
        db.Text
    )

    exames_solicitados = db.Column(
        db.Text
    )

    observacoes_medico = db.Column(
        db.Text
    )

    atestado_liberado = db.Column(
        db.Boolean,
        default=False
    )

    dias_atestado = db.Column(
        db.Integer
    )

    # ==========================
    # Relacionamentos
    # ==========================

    medico_id = db.Column(
        db.Integer,
        db.ForeignKey('medicos.id')
    )

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id')
    )

    # ==========================
    # Data de criação
    # ==========================

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )