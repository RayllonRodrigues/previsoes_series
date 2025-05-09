# 🌦️ Sistema de Previsão Climática com Inteligência Artificial

Este sistema permite realizar **previsões climáticas inteligentes** utilizando dados reais da internet, fornecidos pela API pública **Open-Meteo**, e algoritmos de aprendizado de máquina com o modelo **Facebook Prophet**.

---

## 📌 Funcionalidades

- ✅ Coleta automática de dados meteorológicos dos **últimos 30 dias**
- ✅ Escolha do **local** (ex: Tocantinópolis, Palmas, São Paulo, Manaus)
- ✅ Seleção da **variável climática a ser prevista**:
  - Temperatura máxima (°C)
  - Temperatura mínima (°C)
  - Precipitação (mm)
  - Umidade relativa (%)
  - Velocidade do vento (km/h)
  - Evapotranspiração (mm)
- ✅ Treinamento do modelo Prophet localmente
- ✅ Visualização de gráfico com **intervalo de confiança**
- ✅ Exportação da previsão em **formato CSV**
- ✅ Interface leve e interativa via **Streamlit**

---

## 🧠 Tecnologias Utilizadas

- **Python** – Lógica e processamento
- **Streamlit** – Interface web local
- **Facebook Prophet** – Previsão de séries temporais
- **Open-Meteo API** – Fonte de dados climáticos
- **Matplotlib** – Geração de gráficos
- **Pandas** – Manipulação de dados
- **Joblib** – Salvamento do modelo treinado

---

## 🎯 Objetivo

Oferecer uma ferramenta inteligente de previsão climática com base em dados reais da internet e IA, voltada para:

- 🌱 Produtores rurais
- 🌤️ Técnicos agrícolas e meteorologistas
- 🎓 Projetos acadêmicos e de extensão
- 🏙️ Defesa civil e planejamento urbano
- 👨‍👩‍👧‍👦 Cidadãos que desejam monitorar o clima local

---

## ▶️ Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
