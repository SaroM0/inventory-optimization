import streamlit as st
import requests
from components.config import aplicar_css

# URL y token para la API
API_URL = "https://stapi.straico.com/v0/agent/66dce5fb10da9efc3041d915/prompt"
TOKEN = "dn-XniKcSjKqHn2E9cgyCf43Dcy3UtmB7hZpXjt4AAxbf7UbZZc"

# Función para realizar la solicitud a la API de Straico
def get_chatbot_response(prompt):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": prompt}
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200 and response.json().get("success"):
        return response.json()["response"]["answer"]
    else:
        return "Error al obtener la respuesta del chatbot. Por favor, intenta de nuevo más tarde."

# Inicializar el historial de la conversación
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Configuración principal de la app
def main():
    aplicar_css()
    st.markdown('<h1 class="titulo-principal">ChatBot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-titulo">Interactúa con nuestro chatbot para resolver tus dudas y obtener información al instante.</p>', unsafe_allow_html=True)

    # Campo de entrada para la pregunta del usuario
    user_input = st.chat_input("Escribe tu mensaje aquí:")

    # Procesar la entrada del usuario
    if user_input:
        # Agregar la pregunta del usuario al historial de conversación
        st.session_state.conversation.append({"role": "user", "text": user_input})

        # Obtener la respuesta del chatbot usando la API de Straico
        chatbot_response = get_chatbot_response(user_input)
        st.session_state.conversation.append({"role": "bot", "text": chatbot_response})

    # Mostrar el historial de conversación
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-bubble user">
                    <p><strong>Usuario:</strong> {message["text"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif message["role"] == "bot":
            st.markdown(
                f"""
                <div class="chat-bubble bot">
                    <p><strong>Chatbot:</strong> {message["text"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
