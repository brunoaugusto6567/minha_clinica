from flask import Blueprint, render_template, request, redirect, url_for, flash
def dashboard():
    consultas = Consulta.query.filter_by(paciente_id=current_user.id).all()

    return render_template('dashboard.html', consultas=consultas)


@consulta.route('/marcar-consulta', methods=['GET', 'POST'])
@login_required
def marcar_consulta():
    if request.method == 'POST':
        especialidade = request.form['especialidade']
        tipo_consulta = request.form['tipo_consulta']
        data = request.form['data']
        horario = request.form['horario']

        link = None

        if tipo_consulta == 'Teleconsulta':
            link = 'https://meet.jit.si/consulta-clinica-online'

        nova_consulta = Consulta(
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
    consultas = Consulta.query.filter_by(paciente_id=current_user.id).all()

    return render_template('historico.html', consultas=consultas)


@consulta.route('/retorno/<int:id>')
@login_required
def retorno(id):
    consulta_antiga = Consulta.query.get_or_404(id)

    nova_consulta = Consulta(
        especialidade=consulta_antiga.especialidade,
        tipo_consulta=consulta_antiga.tipo_consulta,
        data='A definir',
        horario='A definir',
        retorno=True,
        paciente_id=current_user.id
    )

    db.session.add(nova_consulta)
    db.session.commit()

    flash('Consulta de retorno solicitada!')

    return redirect(url_for('consulta.dashboard'))