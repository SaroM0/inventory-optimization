import streamlit as st
import pandas as pd
import plotly.express as px
from components.config import aplicar_css

# Cargar datos
@st.cache_data
def cargar_datos(filepath):
    try:
        df = pd.read_csv(filepath)
        df['SalesDate'] = pd.to_datetime(df['SalesDate'], format='%m/%d/%Y', errors='coerce')  # Convertir fechas
        return df
    except FileNotFoundError:
        st.error(f"No se encontró el archivo en la ruta: {filepath}")
        return pd.DataFrame()

file_path = 'data/df_ventas_concat.csv'
data = cargar_datos(file_path)

# Función para mostrar gráficos
def display_charts(data_filtrada):
    # Crear columnas para la tabla y las gráficas principales
    col_table, col_graphs = st.columns([1, 2])  # Relación 1:2 para tabla y gráficas

    # Tabla en la izquierda
    with col_table:
        st.markdown('<h2 class="sub-titulo">Datos Filtrados</h2>', unsafe_allow_html=True)
        st.dataframe(data_filtrada[['Store', 'SalesQuantity', 'SalesDollars', 'SalesDate', 'Description']])

    # Gráfica de barras a la derecha
    with col_graphs:
        st.markdown('<h2 class="sub-titulo">Top 10 Productos por Ventas</h2>', unsafe_allow_html=True)
        top_productos = (
            data_filtrada.groupby('Description')[['SalesDollars']].sum().reset_index()
            .sort_values('SalesDollars', ascending=False)
            .head(10)
        )
        fig_top_productos = px.bar(
            top_productos,
            x='Description',
            y='SalesDollars',
            title=None,  # Título manejado por el HTML
            labels={'SalesDollars': 'Ventas ($)', 'Description': 'Producto'},
            width=500,
            height=300,
        )
        fig_top_productos.update_traces(marker_color='#183b61')  # Color personalizado
        st.plotly_chart(fig_top_productos, use_container_width=True)

    # Gráfica de dispersión abajo
    st.markdown('<h2 class="sub-titulo">Tendencias de Ventas por Fecha</h2>', unsafe_allow_html=True)
    ventas_diarias = (
        data_filtrada.groupby('SalesDate')[['SalesDollars']].sum().reset_index()
    )
    fig_ventas = px.line(
        ventas_diarias,
        x='SalesDate',
        y='SalesDollars',
        title=None,  # Título manejado por el HTML
        labels={'SalesDollars': 'Ventas ($)', 'SalesDate': 'Fecha'}
    )
    fig_ventas.update_traces(line_color='#183b61')  # Color personalizado
    st.plotly_chart(fig_ventas, use_container_width=True)

# Función principal
def main():
    aplicar_css()
    st.markdown('<h1 class="titulo-principal">Análisis de Tiendas</h1>', unsafe_allow_html=True)

    if data.empty:
        st.error("No se pudieron cargar los datos. Por favor, verifica la ruta del archivo.")
        return

    # Filtros
    st.sidebar.header("Filtros")
    tienda = st.sidebar.selectbox("Selecciona una tienda", options=data['Store'].dropna().unique())
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", data['SalesDate'].min())
    fecha_fin = st.sidebar.date_input("Fecha de fin", data['SalesDate'].max())

    # Aplicar filtros
    data_filtrada = data[
        (data['Store'] == tienda) &
        (data['SalesDate'] >= pd.Timestamp(fecha_inicio)) &
        (data['SalesDate'] <= pd.Timestamp(fecha_fin))
    ]

    # Mostrar tabla y gráficos
    if not data_filtrada.empty:
        display_charts(data_filtrada)
    else:
        st.write("No hay datos para los filtros seleccionados.")

if __name__ == "__main__":
    main()
