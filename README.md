#  Clínica Médica Digital

Sistema web para gerenciamento de consultas médicas desenvolvido em **Python** utilizando **Flask**.

---

#  Autores

* Bruno Augusto
* Eduardo Evaristo

---

#  Tecnologias Utilizadas

* Python 3
* Flask
* SQLite
* SQLAlchemy
* Flask-Login
* Flask-Migrate
* Flask-WTF
* ReportLab
* Cryptography
* HTML5
* CSS3

---

#  Como baixar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/brunoaugusto6567/minha_clinica.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd minha_clinica
```

---

## 3. Escolher a versão desejada

Para listar todas as versões (branches) disponíveis:

```bash
git branch -a
```

Depois, troque para a versão desejada.

Exemplo utilizando a versão **2.2**:

```bash
git checkout 2.2
```

---

## 4. Criar o ambiente virtual

### Linux

```bash
python3 -m venv .clinica
source .clinica/bin/activate
```

### Windows

```powershell
python -m venv .clinica
.clinica\Scripts\activate
```

---

## 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso ocorra erro relacionado ao pacote **cryptography**:

```bash
pip install cryptography
```

---

## 6. Criar o banco de dados

```bash
python criar_banco.py
```

---

## 7. Executar o sistema

```bash
python run.py
```

A aplicação ficará disponível em:

```
http://127.0.0.1:5000
```

---

#  Cadastro do Paciente

### Endereço

```
http://127.0.0.1:5000/cadastro
```

### Usuário de demonstração

**Nome**

```
Lucas Martins Oliveira
```

**Email**

```
lucas.martins2026@gmail.com
```

**Senha**

```
Saude@2026
```

---

#  Login do Paciente

### Endereço

```
http://127.0.0.1:5000/login
```

**Email**

```
lucas.martins2026@gmail.com
```

**Senha**

```
Saude@2026
```

---

#  Cadastro do Médico

### Endereço

```
http://127.0.0.1:5000/medico/cadastro
```

### Exemplo

**Nome**

```
Dr. João Silva
```

**Especialidade**

```
Cardiologia
```

**Email**

```
medico@clinica.com
```

**Senha**

```
123456
```

---

#  Login do Médico

### Endereço

```
http://127.0.0.1:5000/medico/login
```

**Email**

```
medico@clinica.com
```

**Senha**

```
123456
```

---

#  Funcionalidades

## Paciente

* Cadastro
* Login
* Agendamento de consultas
* Cancelamento de consultas
* Histórico de consultas
* Solicitação de consultas de retorno
* Download de atestados em PDF

## Médico

* Cadastro
* Login
* Dashboard administrativo
* Atendimento das consultas
* Registro de diagnóstico
* Prescrição de medicamentos
* Solicitação de exames
* Emissão de atestados médicos
* Aprovação e recusa de consultas de retorno
* Finalização de consultas

---

#  Novidades da versão 2.2

* Correção completa das rotas de solicitação de retorno.
* Aprovação e recusa de retornos diretamente pelo médico.
* Novo fluxo de agendamento de retorno.
* Melhorias no Dashboard do Médico.
* Polimento geral do CSS e da interface.
* Ajustes nas validações e correções de bugs.

---

#  Licença

Projeto desenvolvido para fins acadêmicos na disciplina de **Programação Orientada a Objetos (POO)**.
