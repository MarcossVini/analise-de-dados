# Dashboard Movelaria - Análise de Dados

Um dashboard interativo desenvolvido em Streamlit para análise de dados de sensores em fábricas de móveis, permitindo o monitoramento de temperatura, umidade, vibração e produção de madeira processada.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para auxiliar no monitoramento e análise de dados de produção em movelarias. O dashboard permite visualizar métricas importantes como:

- **Temperatura** (°C)
- **Umidade** (%)
- **Vibração** das máquinas
- **Estado das Máquinas** (Operando, Parada, Manutenção)
- **Localização** das fábricas
- **Madeira Processada** (unidades)

## 🚀 Funcionalidades

- **Upload de Arquivos CSV**: Carregue seus próprios dados de produção
- **Visualizações Interativas**: Gráficos de linha, pizza e scatter plots
- **Filtros Dinâmicos**: Agrupe dados por localização, estado da máquina ou data
- **Mapa de Localização**: Visualização geográfica das fábricas em Parintins
- **Gerador de Dados**: Script para criar dados de exemplo para testes

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **Streamlit** - Framework para criação do dashboard
- **Pandas** - Manipulação e análise de dados
- **Plotly Express** - Criação de gráficos interativos
- **Altair** - Visualizações estatísticas avançadas

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/MarcossVini/analise-de-dados.git
cd analise-de-dados
```

### 2. Instale as dependências
```bash
pip install streamlit pandas plotly altair
```

Ou crie um arquivo `requirements.txt` com:
```
streamlit>=1.25.0
pandas>=1.5.0
plotly>=5.15.0
altair>=5.0.0
```

E instale com:
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

### Executando o Dashboard

1. **Inicie o aplicativo Streamlit:**
```bash
streamlit run app.py
```

2. **Acesse o dashboard:**
   - O aplicativo abrirá automaticamente no seu navegador
   - URL padrão: `http://localhost:8501`

3. **Carregue seus dados:**
   - Use o botão "Escolha um arquivo CSV" para fazer upload dos seus dados
   - O arquivo deve conter as colunas obrigatórias (veja formato abaixo)

### Gerando Dados de Exemplo

Para testar o dashboard com dados simulados:

```bash
python gerar_dados.py
```

Este script criará um arquivo `dados_estaticos.csv` com 500 registros de exemplo.

## 📊 Formato dos Dados

O arquivo CSV deve conter as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `Data/hora` | DateTime | Data e hora da coleta |
| `Temperatura(ºC)` | Float | Temperatura em graus Celsius |
| `Umidade %` | Float | Percentual de umidade |
| `Vibração` | Float | Nível de vibração da máquina |
| `Estado da Máquina` | String | Operando, Parada ou Manutenção |
| `Localização` | String | Nome da fábrica/localização |
| `Madeira Processada` | Integer | Quantidade de madeira processada |

### Exemplo de dados:
```csv
Data/hora,Temperatura(ºC),Umidade %,Vibração,Estado da Máquina,Localização,Madeira Processada
2024-11-13 11:53:35,27.73,48.35,2.11,Operando,San Rafael Movelaria,497
2024-11-12 11:53:35,22.90,62.71,3.75,Operando,Movelaria Castro,314
```

## 📁 Estrutura do Projeto

```
analise-de-dados/
├── app.py                 # Aplicação principal do dashboard
├── gerar_dados.py         # Script para gerar dados de exemplo
├── dados_estaticos.csv    # Dados gerados automaticamente
├── dados_maquina.csv      # Dados de máquinas
└── README.md             # Este arquivo
```

## 📈 Visualizações Disponíveis

### 1. Gráfico de Linha Temporal
- Mostra a evolução das métricas ao longo do tempo
- Permite agrupar por localização, estado da máquina ou data
- Métricas disponíveis: Temperatura, Umidade, Vibração, Madeira Processada

### 2. Gráfico de Pizza
- Distribuição do estado das máquinas vs madeira processada
- Visualização clara da produtividade por estado operacional

### 3. Scatter Plot (Altair)
- Correlação entre temperatura e umidade
- Tamanho dos pontos baseado na umidade
- Cores baseadas na temperatura

### 4. Mapa de Localização
- Visualização geográfica das fábricas
- Focado na região de Parintins, Amazonas

## 🔧 Personalização

Para adaptar o dashboard às suas necessidades:

1. **Modifique as localizações** em `gerar_dados.py`
2. **Ajuste os ranges de dados** nas funções de geração
3. **Adicione novas métricas** modificando as colunas esperadas
4. **Customize as visualizações** alterando os gráficos em `app.py`

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Marcos Vinicius** - [@MarcossVini](https://github.com/MarcossVini)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!