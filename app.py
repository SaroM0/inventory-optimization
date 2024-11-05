import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Mi Aplicación de Gráficos",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Configuración")
tipo_grafico = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Línea", "Barras", "Dispersión"])


def graficar_linea():
    x = range(1, 11)
    y = [i**2 for i in x]
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    st.pyplot(fig)

def graficar_barras():
    data = {"Categoría": ["A", "B", "C", "D"], "Valores": [3, 7, 2, 5]}
    fig = px.bar(data, x="Categoría", y="Valores", title="Gráfico de Barras")
    st.plotly_chart(fig)


def graficar_linea():
    x = range(1, 11)
    y = [i**2 for i in x]
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    st.pyplot(fig)

def graficar_barras():
    data = {"Categoría": ["A", "B", "C", "D"], "Valores": [3, 7, 2, 5]}
    fig = px.bar(data, x="Categoría", y="Valores", title="Gráfico de Barras")
    st.plotly_chart(fig)

def aplicar_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

aplicar_css()

rango = st.sidebar.slider("Rango de valores", 1, 100, (1, 10))
def graficar_linea_personalizada():
    x = range(rango[0], rango[1] + 1)
    y = [i**2 for i in x]
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    st.pyplot(fig)
graficar_linea_personalizada()

