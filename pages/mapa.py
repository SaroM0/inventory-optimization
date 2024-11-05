import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Mapa de Ventas")
    st.write("Visualiza las ventas geográficamente en este mapa interactivo.")

if __name__ == "__main__":
    main()
