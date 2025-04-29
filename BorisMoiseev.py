import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Інтернет-магазин", layout="wide")

# Товары по категориям
PRODUCTS = {
    "Електроніка": [
        {"id": 1, "name": "Смартфон", "price": 30000, "description": "Сучасний смартфон"},
        {"id": 2, "name": "Ноутбук", "price": 60000, "description": "Потужний ноутбук"},
        {"id": 3, "name": "Навушники", "price": 5000, "description": "Бездротові навушники"},
    ],
    "Одяг": [
        {"id": 4, "name": "Футболка", "price": 700, "description": "Бавовняна футболка"},
        {"id": 5, "name": "Джинси", "price": 1800, "description": "Стильні джинси"},
    ],
    "Книги": [
        {"id": 6, "name": "1984", "price": 250, "description": "Антиутопічний роман Дж. Орвелла"},
        {"id": 7, "name": "Гаррі Поттер", "price": 400, "description": "Книга про юного чарівника"},
    ]
}

# Стили и фон
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1515169067865-5387ec356754?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Музыка
st.markdown(
    """
    <audio controls autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True
)

# Состояние корзины
if "cart" not in st.session_state:
    st.session_state.cart = []

# Заголовок
st.title("🛒 Онлайн-магазин")

# Меню
page = st.sidebar.radio("Меню", ["Каталог", "Кошик"])

# Каталог
if page == "Каталог":
    st.subheader("📦 Категорії товарів")
    selected_category = st.selectbox("Оберіть категорію", list(PRODUCTS.keys()))

    for product in PRODUCTS[selected_category]:
        with st.container():
            st.markdown(f"### {product['name']} — {product['price']}₴")
            st.write(product["description"])
            if st.button(f"Додати до кошика", key=f"add_{product['id']}"):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} додано до кошика!")

# Кошик
elif page == "Кошик":
    st.subheader("🧺 Ваш кошик")
    if st.session_state.cart:
        total = 0
        for item in st.session_state.cart:
            st.write(f"• {item['name']} — {item['price']}₴")
            total += item["price"]
        st.markdown(f"### **Загальна сума: {total}₴**")

        # Кнопка оплаты
        st.markdown(
            f"""
            <a href="https://www.liqpay.ua/" target="_blank">
                <button style="padding: 0.5rem 1rem; font-size: 1rem; background-color: green; color: white; border: none; border-radius: 8px; cursor: pointer;">
                    Перейти до оплати
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

        if st.button("Очистити кошик"):
            st.session_state.cart = []
            st.success("Кошик очищено!")
    else:
        st.info("Кошик порожній.")
