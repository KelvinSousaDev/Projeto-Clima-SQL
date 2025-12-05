import requests
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

class ClimaETL:
    
    def __init__(self):
        print("🔧 Inicializando o Robô...")
        load_dotenv()
        self.url_banco = os.getenv("DATABASE_URL")
        
        self.cidades = [
            {'nome': 'São Paulo', 'lat': -23.5475, 'lon': -46.6361},
            {'nome': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729},
            {'nome': 'Curitiba', 'lat': -25.4284, 'lon': -49.2733}
        ]
        self.conexao = None
        self.cursor = None

    def conectar_banco(self):
        try:
            self.conexao = psycopg2.connect(self.url_banco)
            self.cursor = self.conexao.cursor()
            print("✅ Banco conectado.")
        except Exception as e:
            print(f"Erro de conexão: {e}")

    def extrair_dados(self, cidade):
        lat = cidade['lat']
        lon = cidade['lon']
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&timezone=auto"
        
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            return resposta.json()
        else:
            print(f"Erro na API para {cidade['nome']}")
            return None

    def salvar_no_banco(self, cidade_nome, temp, umid, data):
        sql = "INSERT INTO clima_historico (cidade, temperatura, umidade, data_hora) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (cidade_nome, temp, umid, data))

    def executar(self):
        self.conectar_banco()
        
        for cidade in self.cidades:
            print(f"Processando {cidade['nome']}...")
            
            dados = self.extrair_dados(cidade)
            
            if dados:
                temp = dados['current']['temperature_2m']
                umid = dados['current']['relative_humidity_2m']
                data = dados['current']['time']
                
                self.salvar_no_banco(cidade['nome'], temp, umid, data)
                print(f"--> Salvo: {temp}°C")
        
        if self.conexao:
            self.conexao.commit()
            self.conexao.close()
            print("🏁 Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    robo = ClimaETL()
    robo.executar()