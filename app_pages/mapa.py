import streamlit as st
from components.config import aplicar_css
import pandas as pd
import plotly.express as px

def mapa():
    aplicar_css()
    st.title("Explora Nuestro Mapa")
    