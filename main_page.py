import streamlit as st
from components.config import aplicar_css

def main():
    # Configuración inicial
    st.set_page_config(layout="wide", page_title="Danu Analytics Dashboard")
    aplicar_css()

    # Título principal estilizado
    st.markdown('<h1 class="titulo-principal">Danu Analytics Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-titulo">Bienvenido al panel principal. Selecciona una sección para continuar.</p>', unsafe_allow_html=True)

    # Secciones de la página
    secciones = [
        {"nombre": "Chatbot", "imagen": "https://leadsales.io/wp-content/uploads/2023/06/image-38.png", "pagina": "chatbot", "descripcion": "Interacción automatizada con usuarios."},
        {"nombre": "Mapa", "imagen": "https://img.freepik.com/vector-premium/pin-navegador-gps-color-azul-mapa_99087-134.jpg?w=1380", "pagina": "mapa", "descripcion": "Visualiza ubicaciones en el mapa."},
        {"nombre": "Predicciones", "imagen": "https://enterprisersproject.com/sites/default/files/styles/large/public/images/cio_future_crystal_ball.png?itok=ivc7cszG", "pagina": "predicciones", "descripcion": "Análisis predictivo para tomar decisiones."},
        {"nombre": "Productos", "imagen": "https://www.culinariamexicana.com.mx/wp-content/uploads/2022/09/kobby-mendez-xBFTjrMIC0c-unsplash-800x445.jpg", "pagina": "productos", "descripcion": "Consulta productos y sus detalles."},
        {"nombre": "Tiendas", "imagen": "https://losimpuestos.com.mx/wp-content/uploads/abrir-sucursal-sat.jpg", "pagina": "tiendas", "descripcion": "Ubicación y detalles de tiendas."},
    ]

    # Contenedor para las tarjetas
    with st.container():
        # Dividir las tarjetas en columnas
        cols = st.columns(3)  # Tres columnas por fila
        for idx, seccion in enumerate(secciones):
            with cols[idx % 3]:  # Repartir las tarjetas en las columnas
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
