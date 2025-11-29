# 🌩️ Clima Tracker (Pipeline de Dados em Nuvem)

## 📝 Sobre o Projeto

Um sistema de Engenharia de Dados _end-to-end_ que monitora condições climáticas em múltiplas cidades em tempo real.
O diferencial deste projeto é a arquitetura **100% em Nuvem**: o script não roda na minha máquina, mas sim em containers automatizados, e os dados persistem em um servidor PostgreSQL remoto.

## 🏗️ Arquitetura

1.  **Ingestão:** Script Python consome a API da **Open-Meteo**.
2.  **Armazenamento:** Banco de Dados **PostgreSQL** hospedado na **Neon Tech** (Serverless).
3.  **Segurança:** Credenciais protegidas via Variáveis de Ambiente e GitHub Secrets.
4.  **Automação (CI/CD):** Pipeline configurado no **GitHub Actions** para rodar a coleta automaticamente a cada hora (Cron Job).
5.  **Visualização:** Dashboard interativo em **Streamlit**.

## 🛠 Tech Stack

- **Python 3.12**
- **GitHub Actions** (Orquestração)
- **PostgreSQL / Neon** (Database)
- **Streamlit** (Frontend)
- **Pandas & Psycopg2** (Manipulação e Conexão)

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python instalado
- Git instalado

### Passo a Passo

```bash
# 1. Clone e entre
git clone https://github.com/KelvinSousaDev/Projeto-Clima-SQL.git
cd Projeto-Clima-SQL

# 2. Configure o .env
# Crie um arquivo .env e adicione: DATABASE_URL="sua_string_postgres"

# 3. Instale e Rode
pip install -r requirements.txt
streamlit run dashboard_clima.py
```

## Autor

Feito por **Kelvin Sousa** durante sua jornada para Engenharia de Dados.
[LinkedIn](https://www.linkedin.com/in/okelvinsousa)
