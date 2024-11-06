import streamlit as st
import requests

# URL y token para la API
API_URL = "https://stapi.straico.com/v0/agent/66dce5fb10da9efc3041d915/prompt"
TOKEN = "dn-XniKcSjKqHn2E9cgyCf43Dcy3UtmB7hZpXjt4AAxbf7UbZZc"

# Función para realizar la solicitud a la API de Straico
def get_chatbot_response(prompt):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200 and response.json().get("success"):
        return response.json()["response"]["answer"]
    else:
        return "Error al obtener la respuesta del chatbot."

# Inicializar el historial de la conversación
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Configuración principal de la app
def main():
    st.title("ChatBot")
    st.write("Interactúa con nuestro chatbot para resolver tus dudas y obtener la información que desees.")

    # Campo de entrada para la pregunta del usuario
    user_input = st.chat_input("Escribe tu mensaje aquí:")

    # Procesar la entrada del usuario
    if user_input:
        # Agregar la pregunta del usuario al historial de conversación
        st.session_state.conversation.append({"user": user_input})

        # Obtener la respuesta del chatbot usando la API de Straico
        chatbot_response = get_chatbot_response(user_input)
        
        # Agregar la respuesta del chatbot al historial de conversación
        st.session_state.conversation.append({"bot": chatbot_response})

    # Mostrar la conversación completa
    for message in st.session_state.conversation:
        if "user" in message:
            st.write(f"**Usuario:** {message['user']}")
        elif "bot" in message:
            st.write(f"**Chatbot:** {message['bot']}")

if __name__ == "__main__":
    main()
