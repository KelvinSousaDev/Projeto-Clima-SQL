import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

url_banco = os.getenv("DATABASE_URL")

print("📡 Conectando ao Neon PostgreSQL...")

try:
    conexao = psycopg2.connect(url_banco)
    cursor = conexao.cursor()
    
    comando_sql = """
    CREATE TABLE IF NOT EXISTS clima_historico (
        id SERIAL PRIMARY KEY,
        cidade VARCHAR(50) NOT NULL,
        temperatura DECIMAL(5,2),
        umidade INTEGER,
        data_hora TIMESTAMP
    );
    """
    
    cursor.execute(comando_sql)
    
    conexao.commit()
    conexao.close()
    
    print("✅ Sucesso! Tabela 'clima_historico' criada na nuvem.")

except Exception as e:
    print(f"❌ Erro ao conectar: {e}")