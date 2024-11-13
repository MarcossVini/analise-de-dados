import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Título do aplicativo
st.title("Dashboard Movelaria")
st.write("Os dados exibidos são infográficos referentes a dados estáticos sobre sensor e temperatura.")

# Carregar dados via upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Lendo os dados do arquivo CSV
    data = pd.read_csv(uploaded_file)
    
    # Exibindo as primeiras linhas do arquivo carregado
    st.write(data.head())

    # Verificando se as colunas esperadas estão no arquivo
    if all(col in data.columns for col in ['Data/hora', 'Temperatura(ºC)', 'Umidade %', 'Vibração', 'Estado da Máquina', 'Localização', 'Madeira Processada']):
        # Seleção das métricas para o gráfico
        col1, col2 = st.columns(2)
        with col1:
            metric = st.selectbox('Selecione a métrica:', ['Temperatura(ºC)', 'Umidade %', 'Vibração', 'Madeira Processada'])
        with col2:
            grupo = st.selectbox('Agrupar por:', ['Localização', 'Estado da Máquina', 'Data/hora'])

        # Criando gráfico de linha com Plotly
        fig = px.line(data, x='Data/hora', y=metric, color=grupo, title=f'{metric} ao longo do tempo')
        st.plotly_chart(fig)

        # Gráfico de pizza para o Estado da Máquina e Madeira Processada
        fig_pizza = px.pie(data, names='Estado da Máquina', values='Madeira Processada', title='Distribuição do Estado da Máquina e Madeira Processada')
        st.plotly_chart(fig_pizza)

        # Exemplo de gráfico com Altair
        chart_data = data[['Data/hora', 'Temperatura(ºC)', 'Umidade %']]  # Selecionando algumas colunas para o gráfico
        alt_chart = alt.Chart(chart_data).mark_circle().encode(
            x='Data/hora:T', 
            y='Temperatura(ºC):Q', 
            size='Umidade %:Q', 
            color='Temperatura(ºC):Q', 
            tooltip=['Data/hora', 'Temperatura(ºC)', 'Umidade %']
        ).properties(title="Temperatura vs Umidade")
        
        st.altair_chart(alt_chart, use_container_width=True)
    
    else:
        st.error("O arquivo CSV não contém todas as colunas esperadas. Verifique o arquivo.")
else:
    st.info("Por favor, carregue um arquivo CSV para começar.")

def mostrar_mapa_parintins():
    # Coordenadas de Parintins e outras localizações
    dados = {
        'Latitude': [-2.6305, -2.6320, -2.6280],  # Exemplo com várias localizações
        'Longitude': [-56.7370, -56.7350, -56.7400]
        }
    
    # Criar um DataFrame com as coordenadas
    df = pd.DataFrame(dados)
    
    # Exibir o mapa com múltiplos pontos
    st.map(df)
