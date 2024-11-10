import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_folium import st_folium
import folium
from components.config import aplicar_css

file_path = 'data/df_ventas_concat.csv'
data = pd.read_csv(file_path)

city_coordinates = {
    'HARDERSFIELD': [53.6458, -1.7780],
    'ASHBORNE': [53.0167, -1.7333],
    'HORNSEY': [51.5833, -0.1167],
    'EANVERNESS': [57.4778, -4.2247],
    'SUTTON': [51.3600, -0.1940],
    'BARNCOMBE': [50.7184, -3.5339],
    'TAMWORTH': [52.6333, -1.6833],
    'EASTHAVEN': [56.5000, -2.7500],
    'BALLYMENA': [54.8639, -6.2761],
    'PEMBROKE': [51.6740, -4.9158],
    'GOULCREST': [52.0000, -1.0000],
    'STANMORE': [51.6167, -0.3167],
    'ALNERWICK': [55.4000, -1.7000],
    'BLACKPOOL': [53.8175, -3.0357],
    'CARDEND': [56.5000, -3.0000],
    'LEESIDE': [51.7500, -0.0833],
    'TARMSWORTH': [53.0000, -2.0000],
    'BROMWICH': [52.5000, -2.0000],
    'WANBORNE': [53.5000, -1.0000],
    'LUNDY': [51.1800, -4.6667],
    'OLDHAM': [53.5409, -2.1114],
    'FURNESS': [54.2000, -3.2167],
    'WINTERVALE': [51.0000, -2.0000],
    'BREDWARDINE': [52.0000, -3.0000],
    'BALERNO': [55.8833, -3.3500],
    'SHARNWICK': [51.7000, -1.3000],
    'ARBINGTON': [52.0000, -1.5000],
    'PALPERROTH': [52.5000, -2.0000],
    'CAERSHIRE': [51.8333, -2.3500],
    "KNIFE'S EDGE": [50.0000, -5.0000],
    'MOUNTMEND': [51.3000, -2.5000],
    'LARNWICK': [53.0000, -1.5000],
    'AYLESBURY': [51.8168, -0.8141],
    'CULCHETH': [53.4500, -2.5000],
    'PITMERDEN': [57.3333, -2.3167],
    'HALIVAARA': [54.0000, -2.0000],
    'LEWES': [50.8753, 0.0172],
    'PAETHSMOUTH': [51.5000, -2.0000],
    'EASTHALLOW': [54.0000, -1.5000],
    'BULLMAR': [52.0000, -0.5000],
    'BLACK HOLLOW': [52.5000, -1.5000],
    'WOLFORD': [51.0000, -0.5000],
    'PORTHCRAWL': [51.5000, -3.7000],
    'VERITAS': [54.0000, -1.0000],
    "PELLA'S WISH": [51.0000, -1.0000],
    'NORFOLK': [52.6297, 1.2923],
    'GARIGILL': [54.8000, -2.3000],
    'ABERDEEN': [57.1497, -2.0943],
    'GRAYCOTT': [53.0000, -1.0000],
    'HILLFAR': [53.0000, -1.0000],
    'GUTHRAM': [52.0000, -0.5000],
    'DRY GULCH': [53.0000, -2.5000],
    "BEGGAR'S HOLE": [51.0000, -0.5000],
    'LANTEGLOS': [50.3400, -4.5800],
    'HARTLEPOOL': [54.6900, -1.2100],
    'CLAETHORPES': [53.5600, -0.0300],
    'IRRAGIN': [51.5000, -2.5000],
    'AETHELNEY': [51.0000, -2.0000],
    'KILMARNOCK': [55.6117, -4.4958],
    'SWORDBREAK': [52.5000, -1.5000],
    'CESTERFIELD': [53.2300, -1.4200],
    'LUTON': [51.8787, -0.4200],
    'SOLARIS': [51.5000, -2.5000],
    'KELD': [54.4000, -2.2000],
    'CLARCTON': [51.0000, -1.5000],
    'DONCASTER': [53.5228, -1.1285],
    'PAENTMARWY': [53.0000, -3.0000],
}


df_cities = pd.DataFrame([
    {'City': city, 'Latitude': coords[0], 'Longitude': coords[1]}
    for city, coords in city_coordinates.items()
])

def display_charts(city_data, col):
    top_products_quantity = city_data.groupby('Description').agg({
        'SalesQuantity': 'sum',
        'SalesDollars': 'sum'
    }).nlargest(10, 'SalesQuantity').reset_index()

    st.markdown('<h2 class="sub-titulo  ">Top 10 Productos por Cantidad Vendida</h2>', unsafe_allow_html=True)
    fig_top_products_quantity = go.Figure(data=[
        go.Bar(
            x=top_products_quantity['Description'],
            y=top_products_quantity['SalesQuantity'],
            marker_color='#183b61' 
        )
    ])
    fig_top_products_quantity.update_layout(
        xaxis_title='Producto',
        yaxis_title='Cantidad Vendida',
        width=500,
        height=300,
        transition_duration=500
    )
    col.plotly_chart(fig_top_products_quantity)

    top_products_revenue = city_data.groupby('Description').agg({
        'SalesQuantity': 'sum',
        'SalesDollars': 'sum'
    }).nlargest(10, 'SalesDollars').reset_index()

    st.markdown('<h2 class="sub-titulo  ">Top 10 Productos por Ingresos Más Altos</h2>', unsafe_allow_html=True)

    fig_top_products_revenue = go.Figure(data=[
        go.Bar(
            x=top_products_revenue['Description'],
            y=top_products_revenue['SalesDollars'],
            marker_color='#183b61' 
        )
    ])
    fig_top_products_revenue.update_layout(
        xaxis_title='Producto',
        yaxis_title='Ingresos',
        width=500,
        height=300,
        transition_duration=500
    )
    col.plotly_chart(fig_top_products_revenue)


def main():
    aplicar_css()
    st.markdown('<h1 class="titulo-principal">Mapa de Ventas</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])

    with col1:
        st.write("Haz clic en una ciudad para ver las estadísticas de ventas y productos más destacados.")
        m = folium.Map(location=[53.0, -1.5], zoom_start=6)
        for idx, row in df_cities.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['City'],
                tooltip=row['City'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
        map_data = st_folium(m, width=800, height=800)

    with col2:
        if not map_data or 'last_object_clicked' not in map_data or not map_data['last_object_clicked']:
            st.write("**Datos generales**")
            display_charts(data, col2)

    if map_data and 'last_object_clicked' in map_data and map_data['last_object_clicked']:
        clicked_data = map_data['last_object_clicked']
        clicked_lat = clicked_data['lat']
        clicked_lng = clicked_data['lng']

        city_row = df_cities[
            (df_cities['Latitude'] == clicked_lat) & (df_cities['Longitude'] == clicked_lng)
        ]

        if not city_row.empty:
            clicked_city = city_row.iloc[0]['City']
            col2.write(f"**Ciudad seleccionada:** {clicked_city}")

            city_data = data[(data['City_x'] == clicked_city) | (data['City_y'] == clicked_city)]

            if not city_data.empty:
                display_charts(city_data, col2)
            else:
                col2.write("Lo sentimos, no hay datos disponibles para la ciudad seleccionada.")


if __name__ == "__main__":
    main()