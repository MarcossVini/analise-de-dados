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