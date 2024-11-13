import pandas as pd
import random

# Função para gerar dados aleatórios dentro de um intervalo
def gerar_dados_aleatorios(minimo, maximo):
    return random.uniform(minimo, maximo)

# Criando um DataFrame vazio
df = pd.DataFrame(columns=['Data/hora', 'Temperatura(ºC)', 'Umidade %', 'Vibração', 'Estado da Máquina', 'Localização', 'Madeira Processada'])

# Simulando 500 linhas de dados
for i in range(500):
    df.loc[i] = [
        pd.Timestamp.now() - pd.Timedelta(days=i),
        gerar_dados_aleatorios(20, 40),  # Temperatura entre 20 e 40 graus
        gerar_dados_aleatorios(40, 80),  # Umidade entre 40% e 80%
        gerar_dados_aleatorios(0, 10),   # Vibração entre 0 e 10 unidades
        random.choice(['Operando', 'Parada', 'Manutenção']),
        random.choice(['Movelaria Castro', 'San Rafael Movelaria']),
        random.randint(100, 500)      # Madeira processada entre 100 e 500 unidades
    ]

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados_estaticos.csv', index=False)