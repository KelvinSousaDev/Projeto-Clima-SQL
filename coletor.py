import requests
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
url_banco = os.getenv("DATABASE_URL")

conexao = psycopg2.connect(url_banco)
cursor = conexao.cursor()

cidades = [
    {'nome': 'São Paulo', 'lat': -23.5475, 'lon': -46.6361},
    {'nome': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729},
    {'nome': 'Curitiba', 'lat': -25.4284, 'lon': -49.2733}
]

for cidade in cidades:
  url = f"https://api.open-meteo.com/v1/forecast?latitude={cidade['lat']}&longitude={cidade['lon']}&current=temperature_2m,relative_humidity_2m&timezone=America%2FSao_Paulo"

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados = resposta.json()
    
    temp_atual = dados['current']['temperature_2m']
    umidade_atual = dados['current']['relative_humidity_2m']
    data_hora_atual = dados['current']['time']
    
    comando = 'INSERT INTO clima_historico (cidade, temperatura, umidade, data_hora) VALUES (%s, %s, %s, %s)'

    cursor.execute(comando, (cidade['nome'], temp_atual, umidade_atual, data_hora_atual))

  else:
    print(f"Erro na conexão: {resposta.status_code}")

conexao.commit()
conexao.close()
print(f'Dados Salvos!')