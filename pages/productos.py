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
        st.markdown('<h2 class="sub-titulo">Productos Filtrados</h2>', unsafe_allow_html=True)
        st.dataframe(data_filtrada[['Description', 'Brand', 'SalesQuantity', 'SalesDollars', 'SalesPrice', 'SalesDate']])

    # Gráficas de "Top 10" en la derecha
    with col_graphs:
        # Top productos por cantidad vendida
        st.markdown('<h2 class="sub-titulo">Top 10 Productos por Cantidad Vendida</h2>', unsafe_allow_html=True)
        top_cantidad = (
            data_filtrada.groupby('Description')[['SalesQuantity']].sum().reset_index()
            .sort_values('SalesQuantity', ascending=False)
            .head(10)
        )
        fig_cantidad = px.bar(
            top_cantidad,
            x='Description',
            y='SalesQuantity',
            title=None,  # Título manejado por el HTML
            labels={'SalesQuantity': 'Cantidad Vendida', 'Description': 'Producto'},
            width=500,
            height=300,
        )
        fig_cantidad.update_traces(marker_color='#183b61')  # Color personalizado
        st.plotly_chart(fig_cantidad, use_container_width=True)

        # Top productos por ingresos
        st.markdown('<h2 class="sub-titulo">Top 10 Productos por Ingresos Más Altos</h2>', unsafe_allow_html=True)
        top_ingresos = (
            data_filtrada.groupby('Description')[['SalesDollars']].sum().reset_index()
            .sort_values('SalesDollars', ascending=False)
            .head(10)
        )
        fig_ingresos = px.bar(
            top_ingresos,
            x='Description',
            y='SalesDollars',
            title=None,  # Título manejado por el HTML
            labels={'SalesDollars': 'Ingresos ($)', 'Description': 'Producto'},
            width=500,
            height=300,
        )
        fig_ingresos.update_traces(marker_color='#183b61')  # Color personalizado
        st.plotly_chart(fig_ingresos, use_container_width=True)

    # Gráfica de distribución de precios en la parte inferior
    st.markdown('<h2 class="sub-titulo">Distribución de Precios por Producto</h2>', unsafe_allow_html=True)
    fig_precios = px.box(
        data_filtrada,
        x='Description',
        y='SalesPrice',
        title=None,  # Título manejado por el HTML
        labels={'SalesPrice': 'Precio ($)', 'Description': 'Producto'}
    )
    fig_precios.update_traces(marker_color='#183b61')  # Color personalizado
    st.plotly_chart(fig_precios, use_container_width=True)

# Función principal
def main():
    aplicar_css()
    st.markdown('<h1 class="titulo-principal">Productos Más Vendidos</h1>', unsafe_allow_html=True)

    if data.empty:
        st.error("No se pudieron cargar los datos. Por favor, verifica la ruta del archivo.")
        return

    # Filtros
    st.sidebar.header("Filtros")
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", data['SalesDate'].min())
    fecha_fin = st.sidebar.date_input("Fecha de fin", data['SalesDate'].max())
    precio_min, precio_max = data['SalesPrice'].min(), data['SalesPrice'].max()

    precio_predeterminado_min = precio_min + (precio_max - precio_min) * 0.1
    precio_predeterminado_max = precio_max - (precio_max - precio_min) * 0.1

    rango_precio = st.sidebar.slider(
        "Rango de precios ($)",
        float(precio_min),
        float(precio_max),
        (float(precio_predeterminado_min), float(precio_predeterminado_max))
    )

    # Aplicar filtros
    data_filtrada = data[
        (data['SalesDate'] >= pd.Timestamp(fecha_inicio)) &
        (data['SalesDate'] <= pd.Timestamp(fecha_fin)) &
        (data['SalesPrice'] >= rango_precio[0]) &
        (data['SalesPrice'] <= rango_precio[1])
    ]

    if not data_filtrada.empty:
        display_charts(data_filtrada)
    else:
        st.write("No hay datos para los filtros seleccionados.")

if __name__ == "__main__":
    main()
