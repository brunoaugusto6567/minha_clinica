Clínica Médica Digital
Sistema web para gerenciamento de consultas médicas desenvolvido em Python utilizando Flask.
Autores
Bruno Augusto
Eduardo Evaristo
Tecnologias
Python 3
Flask
SQLite
SQLAlchemy
Flask-Login
Flask-Migrate
Flask-WTF
ReportLab
Cryptography
HTML5
CSS3
Como baixar o projeto
1. Clonar o repositório
git clone https://github.com/brunoaugusto6567/minha_clinica.git
c

2. Trocar para a branch do projeto
git checkout -b 2.0 origin/2.0

3. Criar o ambiente virtual
Linux
python3 -m venv .clinica
source .clinica/bin/activate

Windows
python -m venv .clinica
.clinica\Scripts\activate

4. Instalar as dependências
pip install -r requirements.txt

Caso ocorra erro relacionado ao módulo cryptography:
pip install cryptography

5. Criar o banco de dados
python criar_banco.py

6. Executar o sistema
python run.py

A aplicação ficará disponível em:
http://127.0.0.1:5000

Cadastro do Paciente
Endereço:
http://127.0.0.1:5000/cadastro

Usuário de demonstração
Nome: Lucas Martins Oliveira
Email: lucas.martins2026@gmail.com
Senha: Saude@2026
Login do Paciente
Endereço:
http://127.0.0.1:5000/login

Email: lucas.martins2026@gmail.com
Senha: Saude@2026
Cadastro do Médico
Endereço:
http://127.0.0.1:5000/medico/cadastro

Exemplo
Nome: Dr. João Silva
Especialidade: Cardiologia
Email: medico@clinica.com
Senha: 123456
Login do Médico
Endereço:
http://127.0.0.1:5000/medico/login

Email: medico@clinica.com
Senha: 123456
Funcionalidades
Paciente
Cadastro
Login
Agendamento de consultas
Cancelamento de consultas
Histórico de consultas
Solicitação de consulta de retorno
Download do atestado em PDF
Médico
Cadastro
Login
Dashboard
Atendimento das consultas
Registro do diagnóstico
Prescrição de medicamentos
Solicitação de exames
Emissão de atestado médico
Finalização da consulta
Licença
Projeto desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.

