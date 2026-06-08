# Clínica Médica Digital

Sistema web para gerenciamento de consultas médicas desenvolvido em Python utilizando Flask.

## Autores

* Bruno Augusto
* Eduardo Evaristo

---

# Tecnologias

* Python
* Flask
* SQLite
* SQLAlchemy
* Flask-Login
* ReportLab
* Cryptography (Fernet)
* HTML
* CSS

---

# Como Executar

## Clonar o projeto

```bash
git clone https://github.com/brunoaugusto6567/minha_clinica.git
cd minha_clinica
```

## Criar ambiente virtual

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

## Instalar dependências

```bash
pip install -r requirements.txt
```

Caso ocorra o erro:

```bash
ModuleNotFoundError: No module named 'cryptography'
```

execute:

```bash
pip install cryptography
```

## Executar

```bash
python run.py
```

O sistema ficará disponível em:

http://127.0.0.1:5000

---

# Cadastro do Paciente

Endereço:

http://127.0.0.1:5000/cadastro

Usuário de demonstração:

Nome:
Lucas Martins Oliveira

Email:
[lucas.martins2026@gmail.com](mailto:lucas.martins2026@gmail.com)

Senha:
Saude@2026

---

# Login do Paciente

Endereço:

http://127.0.0.1:5000/login

Email:
[lucas.martins2026@gmail.com](mailto:lucas.martins2026@gmail.com)

Senha:
Saude@2026

---

# Cadastro do Médico

Endereço:

http://127.0.0.1:5000/medico/cadastro

Exemplo:

Nome:
Dr. João Silva

Especialidade:
Cardiologia

Email:
[medico@clinica.com](mailto:medico@clinica.com)

Senha:
123456

---

# Login do Médico

Endereço:

http://127.0.0.1:5000/medico/login

Email:
[medico@clinica.com](mailto:medico@clinica.com)

Senha:
123456

---

# Funcionalidades

## Paciente

* Cadastro
* Login
* Marcação de consultas
* Cancelamento de consultas
* Histórico médico
* Solicitação de retorno
* Download de atestados

## Médico

* Login
* Dashboard
* Atendimento médico
* Diagnóstico
* Prescrição de medicamentos
* Solicitação de exames
* Emissão de atestados
* Finalização de consultas

---

# Segurança

O sistema utiliza a biblioteca Cryptography (Fernet) para criptografar informações sensíveis dos pacientes antes do armazenamento no banco de dados, garantindo maior proteção dos dados.

---

# Licença

Projeto acadêmico desenvolvido para fins educacionais.
