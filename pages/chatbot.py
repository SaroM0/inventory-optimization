import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("Asistente Virtual")
    st.write("Interactúa con nuestro chatbot para resolver tus dudas y obtener información.")

if __name__ == "__main__":
    main()
