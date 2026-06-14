from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.medico import Medico
from app.models.consulta import Consulta
from datetime import datetime

medico = Blueprint(
    "medico",
    __name__,
    url_prefix="/medico"
)

MEDICO_LOGADO = None


# ==========================
# LOGIN
# ==========================

@medico.route("/login", methods=["GET", "POST"])
def login():

    global MEDICO_LOGADO

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        medico_db = Medico.query.filter_by(
            email=email
        ).first()

        if medico_db and medico_db.check_password(senha):

            MEDICO_LOGADO = medico_db.id

            flash("Login realizado com sucesso.")

            return redirect(
                url_for("medico.dashboard")
            )

        flash("Email ou senha incorretos.")

    return render_template(
        "medico/login_medico.html"
    )


# ==========================
# CADASTRO
# ==========================

@medico.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        especialidade = request.form["especialidade"]
        senha = request.form["senha"]

        if Medico.query.filter_by(email=email).first():

            flash("Já existe um médico com este email.")

            return redirect(
                url_for("medico.cadastro")
            )

        novo_medico = Medico(
            nome=nome,
            email=email,
            especialidade=especialidade
        )

        novo_medico.set_password(senha)

        db.session.add(novo_medico)
        db.session.commit()

        flash("Médico cadastrado com sucesso!")

        return redirect(
            url_for("medico.login")
        )

    return render_template(
        "medico/cadastro_medico.html"
    )


# ==========================
# DASHBOARD (SUBSTITUÍDA)
# ==========================

@medico.route("/dashboard")
def dashboard():

    global MEDICO_LOGADO

    if MEDICO_LOGADO is None:
        return redirect(url_for("medico.login"))

    # CORRIGIDO: Indentação ajustada aqui para alinhar com o escopo da função
    consultas = Consulta.query.filter(
        Consulta.status == "Agendada"
    ).order_by(
        Consulta.criado_em.desc()
    ).all()

    retornos = Consulta.query.filter(
        Consulta.status == "Pendente",
        Consulta.retorno == True
    ).order_by(
        Consulta.criado_em.desc()
    ).all()

    print("=" * 50)
    print("CONSULTAS NORMAIS:")
    for c in consultas:
        print(c.id, c.status, c.retorno)

    print("\nRETORNOS:")
    for r in retornos:
        print(r.id, r.status, r.retorno)

    print("=" * 50)

    return render_template(
        "medico/dashboard_medico.html",
        consultas=consultas,
        retornos=retornos
    )


# ==========================
# ATENDER CONSULTA
# ==========================

@medico.route("/consulta/<int:id>", methods=["GET", "POST"])
def editar_consulta(id):

    global MEDICO_LOGADO

    if MEDICO_LOGADO is None:

        return redirect(
            url_for("medico.login")
        )

    consulta = Consulta.query.get_or_404(id)

    if consulta.status != "Agendada":

        flash("Esta consulta já foi encerrada.")

        return redirect(
            url_for("medico.dashboard")
        )

    if request.method == "POST":

        consulta.descricao_paciente = request.form.get(
            "descricao_paciente"
        )

        consulta.diagnostico = request.form.get(
            "diagnostico"
        )

        consulta.medicamentos = request.form.get(
            "medicamentos"
        )

        consulta.exames_solicitados = request.form.get(
            "exames"
        )

        consulta.observacoes_medico = request.form.get(
            "observacoes_medico"
        )

        consulta.status = "Concluída"

        consulta.medico_id = MEDICO_LOGADO

        if request.form.get("atestado") == "sim":

            consulta.atestado_liberado = True

            dias = request.form.get("dias_atestado")

            if dias:
                consulta.dias_atestado = int(dias)
            else:
                consulta.dias_atestado = 1

        else:

            consulta.atestado_liberado = False
            consulta.dias_atestado = None

        db.session.commit()

        flash("Consulta finalizada com sucesso.")

        return redirect(
            url_for("medico.dashboard")
        )

    return render_template(
        "medico/atender_consulta.html",
        consulta=consulta
    )


# ==========================
# LOGOUT
# ==========================

@medico.route("/logout")
def logout():

    global MEDICO_LOGADO

    MEDICO_LOGADO = None

    flash("Logout realizado.")

    return redirect(
        url_for("medico.login")
    )


# ==========================
# RETORNOS (AÇÕES)
# ==========================

@medico.route("/retorno/<int:id>/aceitar")
def aceitar_retorno(id):

    global MEDICO_LOGADO

    if MEDICO_LOGADO is None:
        return redirect(url_for("medico.login"))

    consulta = Consulta.query.get_or_404(id)

    consulta.status = "Agendada"

    consulta.medico_id = MEDICO_LOGADO

    db.session.commit()

    flash("Retorno aceito com sucesso!")

    return redirect(url_for("medico.dashboard"))


@medico.route("/retorno/<int:id>/recusar")
def recusar_retorno(id):

    global MEDICO_LOGADO

    if MEDICO_LOGADO is None:
        return redirect(url_for("medico.login"))

    consulta = Consulta.query.get_or_404(id)

    db.session.delete(consulta)

    db.session.commit()

    flash("Retorno recusado.")

    return redirect(url_for("medico.dashboard"))