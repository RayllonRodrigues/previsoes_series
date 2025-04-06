
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from previsao.previsao import prever, atualizar_dados
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Previsão Climática Inteligente", layout="centered")

st.title("🌦️ Previsão Climática com IA + Open-Meteo")

st.markdown("Escolha o local, a variável climática e o intervalo de previsão. O sistema usa IA para prever os próximos dias com base nos dados dos últimos 30 dias.")

# Escolha de localização
locais = {
    "Tocantinópolis - TO": (-6.3254, -47.4227),
    "Palmas - TO": (-10.1844, -48.3336),
    "São Paulo - SP": (-23.5505, -46.6333),
    "Manaus - AM": (-3.1190, -60.0217)
}
local = st.selectbox("📍 Escolha o local:", list(locais.keys()))
latitude, longitude = locais[local]

# Escolha da variável climática
variaveis = {
    "Temperatura Máxima (°C)": "temperature_2m_max",
    "Temperatura Mínima (°C)": "temperature_2m_min",
    "Precipitação (mm)": "precipitation_sum",
    "Umidade Relativa (%)": "relative_humidity_2m_mean",
    "Velocidade do Vento (km/h)": "windspeed_10m_max",
    "Evapotranspiração (mm)": "et0_fao_evapotranspiration"
}
variavel_nome = st.selectbox("🌡️ Escolha a variável:", list(variaveis.keys()))
variavel_api = variaveis[variavel_nome]

# Botão de atualização
if st.button("🔄 Atualizar dados da internet e treinar modelo"):
    atualizar_dados(latitude, longitude, variavel_api)
    st.success("✅ Dados atualizados e modelo treinado com sucesso!")

dias = st.slider("Quantos dias deseja prever?", 1, 30, 15)
previsao = prever(dias)

# Gráfico
st.subheader("📈 Gráfico de previsão")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(previsao['ds'], previsao['yhat'], label="Previsão", color="#1f77b4", linewidth=2)
ax.fill_between(previsao['ds'], previsao['yhat_lower'], previsao['yhat_upper'], color="#aec7e8", alpha=0.4, label="Intervalo de confiança")
ax.set_xlabel("Data", fontsize=12)
ax.set_ylabel(variavel_nome, fontsize=12)
ax.set_title(f"{variavel_nome} - Previsão para os próximos {dias} dias em {local}", fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc="best")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Download do CSV
st.subheader("📥 Baixar previsão")
csv = previsao[['ds', 'yhat']].rename(columns={"ds": "Data", "yhat": f"{variavel_nome} Previsto"}).to_csv(index=False)
st.download_button("📤 Baixar como CSV", csv, file_name="previsao.csv", mime="text/csv")
