import streamlit as st
from components.config import aplicar_css
import os

def main():
    aplicar_css()
    st.title("Danu Analytics Dashboard")
    st.write("Bienvenido al panel principal. Selecciona una sección para continuar.")

    secciones = [
    {"nombre": "Chatbot", "imagen": "https://leadsales.io/wp-content/uploads/2023/06/image-38.png", "pagina": "chatbot", "descripcion": "Interacción automatizada con usuarios."},
    {"nombre": "Mapa", "imagen": "https://img.freepik.com/vector-premium/pin-navegador-gps-color-azul-mapa_99087-134.jpg?w=1380", "pagina": "mapa", "descripcion": "Visualiza ubicaciones en el mapa."},
    {"nombre": "Predicciones", "imagen": "https://enterprisersproject.com/sites/default/files/styles/large/public/images/cio_future_crystal_ball.png?itok=ivc7cszG", "pagina": "predicciones", "descripcion": "Análisis predictivo para tomar decisiones."},
    {"nombre": "Productos", "imagen": "https://www.culinariamexicana.com.mx/wp-content/uploads/2022/09/kobby-mendez-xBFTjrMIC0c-unsplash-800x445.jpg", "pagina": "productos", "descripcion": "Consulta productos y sus detalles."},
    {"nombre": "Tiendas", "imagen": "https://losimpuestos.com.mx/wp-content/uploads/abrir-sucursal-sat.jpg", "pagina": "tiendas", "descripcion": "Ubicación y detalles de tiendas."},
    ]

    cols = st.container()
    with cols:
        col1, col2, col3 = st.columns(3)
        for idx, seccion in enumerate(secciones):
            with [col1, col2, col3][idx % 3]:
                st.markdown(
                    f"""
                    <div class="card">
                        <a href="{seccion['pagina']}" target="_self">
                            <img src="{seccion['imagen']}" alt="{seccion['nombre']}" class="card-img">
                            <div class="card-text">{seccion['nombre']}</div>
                            <div class="card-description">{seccion['descripcion']}</div>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )



if __name__ == "__main__":
    main()
