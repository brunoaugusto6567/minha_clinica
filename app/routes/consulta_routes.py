import os
from flask import send_file, Blueprint, render_template, request, redirect, url_for, flash
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import tempfile
from datetime import datetime
from app.utils.crypto import criptografar
from flask_login import login_required, current_user

from app import db
from app.models.consulta import Consulta

consulta = Blueprint('consulta', __name__)

ESPECIALIDADES = [
    'Consulta Geral',
    'Pediatria',
    'Ginecologia',
    'Odontologia',
    'Cardiologia',
    'Dermatologia',
    'Ortopedia',
    'Neurologia',
    'Oftalmologia'
]


@consulta.route('/')
def home():
    return render_template(
        'index.html',
        especialidades=ESPECIALIDADES
    )


@consulta.route('/dashboard')
@login_required
def dashboard():
    consultas = Consulta.query.filter_by(
        paciente_id=current_user.id
    ).all()

    return render_template(
        'dashboard.html',
        consultas=consultas
    )


@consulta.route('/marcar-consulta', methods=['GET', 'POST'])
@login_required
def marcar_consulta():
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        cpf = criptografar(request.form['cpf'])
        data_nascimento = request.form['data_nascimento']
        sexo = request.form['sexo']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        especialidade = request.form['especialidade']
        tipo_consulta = request.form['tipo_consulta']
        data = request.form['data']
        horario = request.form['horario']

        try:
            data_consulta = datetime.strptime(data, '%Y-%m-%d')
            if data_consulta.date() < datetime.now().date():
                flash('Não é possível marcar consultas em datas passadas.')
                return redirect(url_for('consulta.marcar_consulta'))
        except ValueError:
            flash('Data da consulta inválida.')
            return redirect(url_for('consulta.marcar_consulta'))

        try:
            nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
            idade = (datetime.now().date() - nascimento.date()).days // 365

            if idade < 0:
                flash('Data de nascimento inválida.')
                return redirect(url_for('consulta.marcar_consulta'))

            if idade > 120:
                flash('Idade superior ao limite permitido.')
                return redirect(url_for('consulta.marcar_consulta'))
        except ValueError:
            flash('Data de nascimento inválida.')
            return redirect(url_for('consulta.marcar_consulta'))

        try:
            hora = int(horario.split(':')[0])
            if hora < 8 or hora > 18:
                flash('A clínica funciona das 08:00 às 18:00.')
                return redirect(url_for('consulta.marcar_consulta'))
        except (ValueError, IndexError):
            flash('Horário inválido.')
            return redirect(url_for('consulta.marcar_consulta'))

        consulta_existente = Consulta.query.filter_by(
            data=data,
            horario=horario,
            status='Agendada'
        ).first()

        if consulta_existente:
            flash('Já existe uma consulta marcada nesse horário.')
            return redirect(url_for('consulta.marcar_consulta'))

        link = None
        if tipo_consulta == 'Teleconsulta':
            link = 'https://meet.jit.si/consulta-clinica-online'

        nova_consulta = Consulta(
            nome_completo=nome_completo,
            cpf=cpf,
            data_nascimento=data_nascimento,
            sexo=sexo,
            telefone=telefone,
            email=email,
            endereco=endereco,
            especialidade=especialidade,
            tipo_consulta=tipo_consulta,
            data=data,
            horario=horario,
            link_teleconsulta=link,
            paciente_id=current_user.id
        )

        db.session.add(nova_consulta)
        db.session.commit()

        flash('Consulta marcada com sucesso!')
        return redirect(url_for('consulta.dashboard'))

    return render_template(
        'marcar_consulta.html',
        especialidades=ESPECIALIDADES
    )


@consulta.route('/historico')
@login_required
def historico():
    consultas = Consulta.query.filter_by(
        paciente_id=current_user.id
    ).all()

    return render_template(
        'historico.html',
        consultas=consultas
    )


@consulta.route('/retorno/<int:id>')
@login_required
def retorno(id):
    consulta_antiga = db.get_or_404(Consulta, id)

    if consulta_antiga.paciente_id != current_user.id:
        flash('Acesso negado!')
        return redirect(url_for('consulta.dashboard'))

    if consulta_antiga.status == 'Cancelada':
        flash('Não é possível solicitar retorno de uma consulta cancelada.')
        return redirect(url_for('consulta.historico'))
    
    if consulta_antiga.status != 'Concluída':
        flash('O retorno só pode ser solicitado após uma consulta concluída.')
        return redirect(url_for('consulta.historico'))

    nova_consulta = Consulta(
        nome_completo=consulta_antiga.nome_completo,
        cpf=consulta_antiga.cpf,
        data_nascimento=consulta_antiga.data_nascimento,
        sexo=consulta_antiga.sexo,
        telefone=consulta_antiga.telefone,
        email=consulta_antiga.email,
        endereco=consulta_antiga.endereco,
        especialidade=consulta_antiga.especialidade,
        tipo_consulta=consulta_antiga.tipo_consulta,
        data=None,
        horario=None,
        status='Pendente',
        retorno=True,
        paciente_id=current_user.id
    )

    db.session.add(nova_consulta)
    db.session.commit()

    flash('Consulta de retorno solicitada!')
    return redirect(url_for('consulta.dashboard'))


@consulta.route('/teleconsulta/<int:id>')
@login_required
def teleconsulta(id):
    consulta_obj = db.get_or_404(Consulta, id)

    if consulta_obj.paciente_id != current_user.id:
        flash('Acesso negado!')
        return redirect(url_for('consulta.dashboard'))

    return render_template(
        'teleconsulta.html',
        consulta=consulta_obj
    )


@consulta.route('/cancelar-consulta/<int:id>')
@login_required
def cancelar_consulta(id):
    consulta_obj = db.get_or_404(Consulta, id)

    if consulta_obj.paciente_id != current_user.id:
        flash('Acesso negado!')
        return redirect(url_for('consulta.dashboard'))

    if consulta_obj.status == 'Cancelada':
        flash('Esta consulta já está cancelada.')
        return redirect(url_for('consulta.dashboard'))

    consulta_obj.status = 'Cancelada'
    db.session.commit()

    flash('Consulta cancelada com sucesso!')
    return redirect(url_for('consulta.dashboard'))


@consulta.route('/atestado/<int:id>')
@login_required
def baixar_atestado(id):
    consulta_obj = db.get_or_404(Consulta, id)

    if consulta_obj.paciente_id != current_user.id:
        flash('Acesso negado!')
        return redirect(url_for('consulta.dashboard'))

    if consulta_obj.status != 'Concluída':
        flash('O atestado só pode ser emitido para consultas concluídas.')
        return redirect(url_for('consulta.dashboard'))

    if not consulta_obj.atestado_liberado:
        flash('O médico não liberou atestado para esta consulta.')
        return redirect(url_for('consulta.dashboard'))

    arquivo = tempfile.NamedTemporaryFile(
        delete=False,
        suffix='.pdf'
    )

    pdf = canvas.Canvas(arquivo.name, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(300, 800, "CLÍNICA MÉDICA")

    pdf.setFont("Helvetica", 12)
    pdf.setFillColorRGB(0.3, 0.3, 0.3)
    pdf.drawCentredString(300, 780, "Atendimento Médico Especializado")

    pdf.setStrokeColorRGB(0.8, 0.8, 0.8)
    pdf.setLineWidth(1)
    pdf.line(50, 760, 550, 760)

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, 720, "ATESTADO MÉDICO")

    styles = getSampleStyleSheet()
    estilo_corpo = ParagraphStyle(
        'CorpoTexto',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=22,
        alignment=4
    )

    data_formatada = consulta_obj.data
    if isinstance(data_formatada, datetime):
        data_formatada = data_formatada.strftime('%d/%m/%Y')
    elif isinstance(data_formatada, str) and '-' in data_formatada:
        try:
            data_formatada = datetime.strptime(data_formatada, '%Y-%m-%d').strftime('%d/%m/%Y')
        except ValueError:
            pass

    texto = (
        f"Atestamos para os devidos fins que "
        f"<b>{consulta_obj.nome_completo}</b> "
        f"compareceu a esta clínica na data "
        f"<b>{data_formatada}</b> e deverá permanecer "
        f"afastado(a) de suas atividades por "
        f"<b>{consulta_obj.dias_atestado} dia(s)</b>, "
        f"conforme avaliação médica realizada."
    )

    p = Paragraph(texto, estilo_corpo)
    p.wrapOn(pdf, 500, 200)
    p.drawOn(pdf, 50, 630)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(
        50,
        550,
        f"Emitido em: {datetime.now().strftime('%d/%m/%Y')}"
    )

    # CORREÇÃO: Alinhamento das linhas abaixo com 4 espaços para dentro da função
    assinatura = os.path.join(
        "app",
        "static",
        "assinaturas",
        "dr_joao.png"
    )

    if os.path.exists(assinatura):
        pdf.drawImage(
            assinatura,
            220,
            445,
            width=160,
            height=60,
            mask='auto'
        )

    nome_medico = "Dr. João Silva"

    if consulta_obj.medico:
        nome_medico = consulta_obj.medico.nome

    pdf.drawCentredString(
        300,
        430,
        nome_medico
    )
    
    pdf.setFont("Helvetica", 10)
    pdf.setFillColorRGB(0.5, 0.5, 0.5)
    pdf.drawCentredString(
        300,
        100,
        "Documento emitido eletronicamente pela Clínica Médica"
    )

    pdf.save()
    arquivo.close()

    return send_file(
        arquivo.name,
        as_attachment=True,
        download_name=f'atestado_{consulta_obj.id}.pdf'
    )