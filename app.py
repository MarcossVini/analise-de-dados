import streamlit as st
import pandas as pd


st.title ("Dashboard Movelaria")
st.write("Os dados exibidos são infográficos referentes a dados estáticos sobre sensor e temperatura")

df = pd.DataFrame({
    'Data/hora': [],
    'Temperatura(ºC)':[],
    'Umidade %':[],
    'Vibração':[],
    'Estado da Máquina':[],
    'Localização':[],
    'Madeira Processada':[],
})
st.write()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Carregando os dados (substitua pelo seu caminho)
data = pd.read_csv('dados_maquina.csv')

# Título do aplicativo
st.title('Análise de Dados da Máquina')

# Selecionando os dados para o gráfico
col1, col2 = st.columns(2)
with col1:
    metric = st.selectbox('Selecione a métrica:', ['Temperatura(ºC)', 'Umidade %', 'Vibração', 'Madeira Processada'])
with col2:
    grupo = st.selectbox('Agrupar por:', ['Localização', 'Estado da Máquina'])

# Criando o gráfico
fig = px.line(data, x='Data/hora', y=metric, color=grupo)
st.plotly_chart(fig)

fig_pizza = px.pie(data, names='Estado da Máquina', values='Madeira Processada')
st.plotly_chart(fig_pizza)