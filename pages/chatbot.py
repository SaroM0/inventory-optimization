import streamlit as st
from components.config import aplicar_css

def main():
    aplicar_css()
    st.title("ChatBot")
    st.write("Interactúa con nuestro chatbot para resolver tus dudas y obtener la información que desees.")

    # Contenedor para la conversación
    chat_container = st.container()

    # Campo de entrada para la pregunta del usuario
    user_input = st.chat_input("Escribe tu mensaje aquí:")

    if user_input:
        with chat_container:
            st.write(f"**Usuario:** {user_input}")
            st.write(f"**Chatbot:** [Respuesta del chatbot]")

if __name__ == "__main__":
    main()
