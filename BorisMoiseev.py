import streamlit as st

# Список товаров
PRODUCTS = [
    {"id": 1, "name": "Смартфон", "price": 30000, "description": "Современный смартфон"},
    {"id": 2, "name": "Ноутбук", "price": 60000, "description": "Мощный ноутбук"},
    {"id": 3, "name": "Наушники", "price": 5000, "description": "Беспроводные наушники"},
]

st.set_page_config(page_title="Интернет-магазин")

# Инициализируем корзину
if "cart" not in st.session_state:
    st.session_state.cart = []

# Шапка
st.title("🛒 Интернет-магазин")

# Меню страниц
page = st.sidebar.radio("Меню", ["Каталог", "Корзина"])

# --- Каталог товаров ---
if page == "Каталог":
    st.subheader("📦 Товары")
    for product in PRODUCTS:
        with st.container():
            st.markdown(f"### {product['name']} — {product['price']}₽")
            st.write(product["description"])
            if st.button(f"Добавить в корзину", key=f"add_{product['id']}"):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} добавлен в корзину")

# --- Корзина ---
elif page == "Корзина":
    st.subheader("🧺 Ваша корзина")
    if st.session_state.cart:
        total = 0
        for item in st.session_state.cart:
            st.write(f"• {item['name']} — {item['price']}₽")
            total += item["price"]
        st.markdown(f"**Итого: {total}₽**")
        if st.button("Очистить корзину"):
            st.session_state.cart = []
            st.success("Корзина очищена")
    else:
        st.info("Корзина пуста")
