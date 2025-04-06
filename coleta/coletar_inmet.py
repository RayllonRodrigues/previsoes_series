
import requests
import pandas as pd
from datetime import datetime

def coletar_dados():
    # Exemplo fictício de coleta - INMET requer login, isso seria adaptado para uma API real ou scraping autorizado
    dados = {
        'data': pd.date_range(start='2024-01-01', end='2024-01-31'),
        'temperatura': [25 + (x % 5) for x in range(31)]
    }
    df = pd.DataFrame(dados)
    df.to_csv('dados/dados_raw.csv', index=False)
    print("Dados coletados e salvos em dados_raw.csv")

if __name__ == "__main__":
    coletar_dados()
