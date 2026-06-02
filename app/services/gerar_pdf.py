from reportlab.pdfgen import canvas


def criar_pdf(nome_paciente, texto, arquivo):
    pdf = canvas.Canvas(arquivo)

    pdf.setFont('Helvetica-Bold', 18)
    pdf.drawString(180, 800, 'ATESTADO MÉDICO')

    pdf.setFont('Helvetica', 12)

    pdf.drawString(100, 740, f'Paciente: {nome_paciente}')

    pdf.drawString(100, 700, texto)

    pdf.drawString(100, 650, 'Assinatura do Médico')

    pdf.save()