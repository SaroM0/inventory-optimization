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
    # Top productos por cantidad vendida
    top_cantidad = (
        data_filtrada.groupby('Description')[['SalesQuantity']].sum().reset_index()
        .sort_values('SalesQuantity', ascending=False)
        .head(10)
    )
    fig_cantidad = px.bar(
        top_cantidad,
        x='Description',
        y='SalesQuantity',
        title="Top 10 Productos por Cantidad Vendida",
        labels={'SalesQuantity': 'Cantidad Vendida', 'Description': 'Producto'}
    )
    col.plotly_chart(fig_cantidad)

    # Top productos por ingresos
    top_ingresos = (
        data_filtrada.groupby('Description')[['SalesDollars']].sum().reset_index()
        .sort_values('SalesDollars', ascending=False)
        .head(10)
    )
    fig_ingresos = px.bar(
        top_ingresos,
        x='Description',
        y='SalesDollars',
        title="Top 10 Productos por Ingresos",
        labels={'SalesDollars': 'Ingresos ($)', 'Description': 'Producto'}
    )
    col.plotly_chart(fig_ingresos)

    # Distribución de precios por producto
    fig_precios = px.box(
        data_filtrada,
        x='Description',
        y='SalesPrice',
        title="Distribución de Precios por Producto",
        labels={'SalesPrice': 'Precio ($)', 'Description': 'Producto'}
    )
    col.plotly_chart(fig_precios)

# Función principal
def main():
    aplicar_css()
    st.title("Productos Más Vendidos")
    st.write("Esta sección muestra los productos más vendidos en el último período.")

    if data.empty:
        st.error("No se pudieron cargar los datos. Por favor, verifica la ruta del archivo.")
        return

    # Filtros
    st.sidebar.header("Filtros")
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", data['SalesDate'].min())
    fecha_fin = st.sidebar.date_input("Fecha de fin", data['SalesDate'].max())
    rango_precio = st.sidebar.slider(
        "Rango de precios ($)", 
        float(data['SalesPrice'].min()), 
        float(data['SalesPrice'].max()), 
        (float(data['SalesPrice'].min()), float(data['SalesPrice'].max()))
    )

    # Aplicar filtros
    data_filtrada = data[
        (data['SalesDate'] >= pd.Timestamp(fecha_inicio)) &
        (data['SalesDate'] <= pd.Timestamp(fecha_fin)) &
        (data['SalesPrice'] >= rango_precio[0]) &
        (data['SalesPrice'] <= rango_precio[1])
    ]

    # Mostrar tabla y gráficos
    st.write("### Productos Filtrados")
    st.dataframe(data_filtrada[['Description', 'Brand', 'SalesQuantity', 'SalesDollars', 'SalesPrice', 'SalesDate']])

    st.write("### Visualización de Datos")
    if not data_filtrada.empty:
        col1, col2 = st.columns([1, 2])
        with col2:
            display_charts(data_filtrada, st)
    else:
        st.write("No hay datos para los filtros seleccionados.")

if __name__ == "__main__":
    main()
