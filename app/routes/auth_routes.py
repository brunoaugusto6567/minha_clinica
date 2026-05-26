from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app import db
from app.models.usuario import Usuario


auth = Blueprint('auth', __name__)


@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']

        usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone
        )

        usuario.set_senha(senha)

        db.session.add(usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso!')

        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.verificar_senha(senha):
            login_user(usuario)
            return redirect(url_for('consulta.dashboard'))

        flash('Email ou senha inválidos')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))