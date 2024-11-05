import streamlit as st
from components.config import aplicar_css
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Danu Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Aplicar el estilo CSS
aplicar_css()

st.write("Bienvenido a Danu Analytics Dashboard. Selecciona una página en la barra lateral.")
