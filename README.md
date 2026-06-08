# 🏥 Minha Clínica

Sistema web para gerenciamento de consultas médicas desenvolvido em Python com Flask.

## Funcionalidades

* Cadastro e login de pacientes
* Cadastro e login de médicos
* Agendamento de consultas
* Cancelamento de consultas
* Histórico de atendimentos
* Consultas de retorno
* Teleconsulta
* Emissão de atestados em PDF
* Dashboard para médicos
* Dashboard para pacientes

## Tecnologias Utilizadas

* Python 3
* Flask
* SQLAlchemy
* Flask-Login
* SQLite
* ReportLab
* Cryptography
* HTML5
* CSS3

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/brunoaugusto6567/minha_clinica.git
cd minha_clinica
```

### 2. Criar ambiente virtual

Linux:

```bash
python3 -m venv .clinica
source .clinica/bin/activate
```

Windows:

```bash
python -m venv .clinica
.clinica\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

```bash
python criar_banco.py
```

### 5. Criar um médico para testes

```bash
python criar_medico.py
```

### 6. Executar o sistema

```bash
python run.py
```

### 7. Acessar no navegador

```text
http://127.0.0.1:5000
```

## Estrutura do Projeto

```text
minha_clinica/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── static/
│   ├── templates/
│   └── utils/
│
├── instance/
├── config.py
├── criar_banco.py
├── criar_medico.py
├── requirements.txt
├── run.py
└── README.md
```

## Desenvolvedores

* Bruno Augusto
* Eduardo Evaristo

Projeto acadêmico desenvolvido para a disciplina de Programação Orientada a Objetos.
