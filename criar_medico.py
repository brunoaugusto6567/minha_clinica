from app import create_app, db
from app.models.medico import Medico

app = create_app()

with app.app_context():

    db.create_all()

    medico = Medico.query.filter_by(
        email="medico@clinica.com"
    ).first()

    if medico:

        print("Médico já cadastrado.")

    else:

        novo_medico = Medico(
            nome="Dr. João Silva",
            email="medico@clinica.com",
            especialidade="Clínico Geral"
        )

        novo_medico.set_password("123456")

        db.session.add(novo_medico)
        db.session.commit()

        print("Médico criado com sucesso!")