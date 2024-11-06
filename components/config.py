# components/config.py
import streamlit as st
import os

def aplicar_css():
    st.logo("https://static.wixstatic.com/media/d34cc5_6396eedf64664d588f8e1e62035896af~mv2.png/v1/fill/w_1281,h_437,al_c/d34cc5_6396eedf64664d588f8e1e62035896af~mv2.png", size="medium")
    css_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'style.css')
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
