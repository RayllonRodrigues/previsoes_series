
import pandas as pd
from prophet import Prophet
import joblib
import requests
from datetime import datetime, timedelta
import os

def coletar_dados_online(latitude, longitude, variavel_api):
    hoje = datetime.today()
    inicio = hoje - timedelta(days=30)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": variavel_api,
        "timezone": "America/Sao_Paulo",
        "start_date": inicio.strftime('%Y-%m-%d'),
        "end_date": hoje.strftime('%Y-%m-%d')
    }

    response = requests.get(url, params=params)
    dados = response.json()

    chave = variavel_api
    df = pd.DataFrame({
        "ds": dados['daily']['time'],
        "y": dados['daily'][chave]
    })

    return df

def atualizar_dados(latitude, longitude, variavel_api):
    df = coletar_dados_online(latitude, longitude, variavel_api)
    modelo = Prophet()
    modelo.fit(df)
    os.makedirs("modelos", exist_ok=True)
    joblib.dump(modelo, 'modelos/modelo_prophet.pkl')

def prever(dias=15):
    modelo = joblib.load('modelos/modelo_prophet.pkl')
    futuro = modelo.make_future_dataframe(periods=dias)
    previsao = modelo.predict(futuro)
    return previsao
