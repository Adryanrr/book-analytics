import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações da página
st.set_page_config(page_title="Dashboard de Livros",page_icon="📚",layout="wide")

# Título principal
st.title("Dashboard de Livros")


# Carregando os dados
df_reviews = pd.read_csv("./datasets/reviews.csv")
df_top100_books = pd.read_csv("./datasets/books.csv")

# Definindo o intervalo de preço
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# Painel lateral de filtros
st.sidebar.title("Painel de Filtros")
st.sidebar.markdown("Ajuste o preço máximo para visualizar os livros")

max_price = st.sidebar.slider("Faixa de Preço", price_min, price_max, price_max)

# Filtrando os dados com base no preço selecionado
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

# Contagem dos livros por ano de publicação
df_year_counts = df_books['year of publication'].value_counts().sort_index().reset_index()
df_year_counts.columns = ['Ano de Publicação', 'Número de Livros']

# Gráfico de distribuição de ano de publicação
chart_publication = px.line(
    df_year_counts,
    x='Ano de Publicação',
    y='Número de Livros',
    title="Distribuição de Ano de Publicação dos Livros",
    template="plotly_dark",
)

# Gráfico de distribuição de preços dos livros
chart_price = px.histogram(
    df_books,
    x="book price",
    nbins=20,
    title="Distribuição de Preços dos Livros",
    template="plotly_dark",
)

chart_price.update_layout(
    xaxis_title="Preço do Livro",
    yaxis_title="Frequência",
    plot_bgcolor="rgba(0, 0, 0, 0)",  # Fundo transparente
    bargap=0.2
)

# Exibindo os dados e gráficos
st.dataframe(df_books, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)
col1.plotly_chart(chart_publication, use_container_width=True)
col2.plotly_chart(chart_price, use_container_width=True)
