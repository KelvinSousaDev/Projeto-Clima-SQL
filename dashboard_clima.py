import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Clima Tracker Global", layout="wide")

load_dotenv()
url_banco = os.getenv("DATABASE_URL")

@st.cache_resource
def init_connection():
  print("📡 Conectando ao Neon PostgreSQL...")
  return psycopg2.connect(url_banco)

st.title("🌍 Monitoramento Climático em Tempo Real")
st.markdown("Dados coletados via API e armazenados no Neon PostgreSQL (Cloud).")

try:
  conn = init_connection()

  query = "SELECT * FROM clima_historico ORDER BY data_hora DESC"
  df = pd.read_sql(query, conn)

  if not df.empty:
     ultimos = df.drop_duplicates(subset=['cidade'], keep='first')

     cols = st.columns(len(ultimos))

     for i, (index, linha) in enumerate(ultimos.iterrows()):
            cidade = linha['cidade']
            temp = f"{linha['temperatura']}°C"
            hora = linha['data_hora'].strftime('%H:%M')

            cols[i].metric(label=cidade, value=temp, delta=f"às {hora}")
  else:
        st.warning("Aguardando dados...")

  st.divider()

  aba_grafico, aba_dados = st.tabs(["📈 Histórico Visual", "📋 Dados Brutos"])

  with aba_grafico:
        if not df.empty:
            st.subheader("Evolução da Temperatura")
            
            df_chart = df.pivot_table(index='data_hora', columns='cidade', values='temperatura')
            
            st.line_chart(df_chart)
        else:
            st.info("O gráfico aparecerá assim que houver dados.")

  with aba_dados:
      st.dataframe(df, use_container_width=True)

  if st.button("🔄 Atualizar Dados"):
      st.cache_resource.clear()
      st.rerun()

except Exception as e:
    st.error(f"❌ Erro ao conectar: {e}")
