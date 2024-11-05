import streamlit as st
from components.config import aplicar_css

def predicciones():
    aplicar_css()
    st.title("Predicciones de Ventas")
    st.write("Modelo de predicciones en construcción. Aquí podrás ver proyecciones de ventas futuras.")