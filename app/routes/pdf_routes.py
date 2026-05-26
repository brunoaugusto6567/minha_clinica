from flask import Blueprint, send_file
from flask_login import login_required, current_user

from app.services.gerar_pdf import criar_pdf


pdf = Blueprint('pdf', __name__)


@pdf.route('/atestado')
@login_required
def gerar_atestado():
    caminho = 'atestado.pdf'

    texto = 'O paciente deverá permanecer em repouso por 2 dias.'

    criar_pdf(current_user.nome, texto, caminho)

    return send_file(caminho, as_attachment=True)