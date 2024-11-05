import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Tiendas Destacadas")
    st.write("Conoce las tiendas con mejor rendimiento en este apartado.")

if __name__ == "__main__":
    main()
