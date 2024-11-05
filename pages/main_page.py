import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Visión General")
    st.write("Bienvenido a la sección de Visión General. Aquí encontrarás un resumen de las métricas clave de tu negocio.")

if __name__ == "__main__":
    main()
