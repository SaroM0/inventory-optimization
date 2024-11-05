import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Predicciones de Ventas")
    st.write("Explora las proyecciones de ventas futuras basadas en datos históricos.")

if __name__ == "__main__":
    main()
