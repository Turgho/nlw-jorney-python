# NLW-PROJECT-PYTHON
App de planejamento de viagens feito durante o evento NLW da RocketSeat.

Criação de um sistema de planejamentos de viagens feito em python, usando Flask e PyTest para teste unitários.

# Requisitos

- Python 3.0 ou Superior
- pip (gerenciador de pacotes do Python)
- VirtualEnvironment

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento e instalar as dependências do projeto.

### 1. Clonar o Repositório

```bash
git clone https://github.com/Turgho/nlw-jorney-python.git
cd nlw-jorney-python
```

### 2. Instalar VENV

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

Ou

**Win**
```bash
py -3 -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

# Rodar o servidor interno

**Linux/Mac**
```bash
python3 run.py
```

Ou

**Win**
```bash
py -3 run.py
```

# Teste unitários

Com o servidor ligado, digite no prompt:

```bash
pytest -s -v src/models/repositories/<nome_repositório_test>.py
```