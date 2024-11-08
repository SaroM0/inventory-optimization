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
def display_charts(data_filtrada, col):
    # Gráfico de tendencias de ventas
    ventas_diarias = (
        data_filtrada.groupby('SalesDate')[['SalesDollars']].sum().reset_index()
    )
    fig_ventas = px.line(
        ventas_diarias,
        x='SalesDate',
        y='SalesDollars',
        title="Tendencias de Ventas por Fecha",
        labels={'SalesDollars': 'Ventas ($)', 'SalesDate': 'Fecha'}
    )
    col.plotly_chart(fig_ventas)

    # Top productos por ventas
    top_productos = (
        data_filtrada.groupby('Description')[['SalesDollars']].sum().reset_index()
        .sort_values('SalesDollars', ascending=False)
        .head(10)
    )
    fig_top_productos = px.bar(
        top_productos,
        x='Description',
        y='SalesDollars',
        title="Top 10 Productos por Ventas",
        labels={'SalesDollars': 'Ventas ($)', 'Description': 'Producto'}
    )
    col.plotly_chart(fig_top_productos)

# Función principal
def main():
    aplicar_css()
    st.title("Análisis de Tiendas")

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
    st.write(f"### Datos de la Tienda {tienda}")
    st.dataframe(data_filtrada[['Store', 'SalesQuantity', 'SalesDollars', 'SalesDate', 'Description']])

    st.write("### Visualización de Datos")
    if not data_filtrada.empty:
        col1, col2 = st.columns([1, 2])
        with col2:
            display_charts(data_filtrada, st)
    else:
        st.write("No hay datos para los filtros seleccionados.")

if __name__ == "__main__":
    main()
