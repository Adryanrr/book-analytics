import streamlit as st 
import pandas as pd

st.set_page_config(page_title="Reviews de Livros", page_icon="📚", layout="wide")

# Carregando os dados
df_reviews = pd.read_csv("./datasets/reviews.csv")
df_top100_books = pd.read_csv("./datasets/books.csv")

# Sidebar - seleção do livro
st.sidebar.header("Selecione um Livro")
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Livros", books)

# Dados do livro selecionado
df_book = df_top100_books[df_top100_books["book title"] == book]
df_review_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Exibição dos dados do livro
st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("💲 Preço", book_price)
col2.metric("⭐ Avaliação", book_rating)
col3.metric("📅 Ano de Publicação", book_year)

st.divider()

for row in df_review_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])