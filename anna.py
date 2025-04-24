import streamlit as st
import urllib.parse

st.title("Генератор ссылки на продукт в поиске")

query = st.text_input("Введите название продукта", placeholder="Например, iPhone 15")

if st.button("Сгенерировать ссылку"):
    if query.strip():
        encoded_query = urllib.parse.quote_plus(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        st.success("Вот ваша ссылка:")
        st.markdown(f"[{search_url}]({search_url})")
    else:
        st.warning("Пожалуйста, введите название продукта.")


