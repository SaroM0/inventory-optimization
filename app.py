import streamlit as st
from components.config import aplicar_css
from app_pages.main_page import main_page
from app_pages.productos import productos
from app_pages.mapa import mapa
from app_pages.tiendas import tiendas
from app_pages.predicciones import predicciones
from app_pages.chatbot import chatbot

# Configuración de la página
st.set_page_config(
    page_title="Danu Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Aplicar el estilo CSS
aplicar_css()

# Título principal de la aplicación
st.title("Danu Analytics Dashboard")

# Crear una "cajita" o contenedor para cada sección
with st.container():
    st.header("Visión General")
    main_page()

with st.container():
    st.header("Productos Más Vendidos")
    productos()

with st.container():
    st.header("Explora Nuestro Mapa")
    mapa()

with st.container():
    st.header("Tiendas Más Vendidas")
    tiendas()

with st.container():
    st.header("Predicciones")
    predicciones()

with st.container():
    st.header("Chatbot")
    chatbot()
