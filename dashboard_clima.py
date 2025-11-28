import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import streamlit as st

load_dotenv()

url_banco = os.getenv("DATABASE_URL")

@st.cache_resource
def init_connection():
  print("📡 Conectando ao Neon PostgreSQL...")
  return psycopg2.connect(url_banco)

st.set_page_config(page_title="Dados Climaticos", layout="centered")

st.title("💸 Registro de Dados")
st.write("Visão geral dos dados importados do Banco de Dados SQL.")

try:
  conn = init_connection()
  query = "SELECT * FROM clima_historico ORDER BY data_hora DESC"
  df = pd.read_sql(query, conn)
  st.dataframe(df)
except Exception as e:
    st.error(f"❌ Erro ao conectar no banco: {e}")
