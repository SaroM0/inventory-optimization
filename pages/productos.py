import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Productos Más Vendidos")
    st.write("Esta sección muestra los productos más vendidos en el último período.")

if __name__ == "__main__":
    main()
