import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import st_folium
import folium
from components.config import aplicar_css

# Datos ficticios de ventas por ciudad
data = {
    'Ciudad': ['Monterrey', 'Guadalajara', 'Ciudad de México', 'Puebla', 'Tijuana'],
    'Latitud': [25.6866, 20.6597, 19.4326, 19.0414, 32.5149],
    'Longitud': [-100.3161, -103.3496, -99.1332, -98.2063, -117.0382],
    'Ventas': [150, 200, 300, 180, 220],
    'Categoría': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

def main():
    aplicar_css()
    st.title("Mapa de Ventas")
    st.write("Haz clic en una ciudad para ver las estadísticas de ventas.")

    # Crear el mapa centrado en México
    m = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

    # Añadir marcadores para cada ciudad
    for idx, row in df.iterrows():
        folium.Marker(
            location=[row['Latitud'], row['Longitud']],
            popup=row['Ciudad'],
            tooltip=row['Ciudad'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # Mostrar el mapa en Streamlit
    map_data = st_folium(m, width=700, height=500)

    # Verificar si se ha hecho clic en un marcador
    if map_data and 'last_object_clicked' in map_data and map_data['last_object_clicked']:
        clicked_data = map_data['last_object_clicked']
        if 'popup' in clicked_data and clicked_data['popup']:
            clicked_city = clicked_data['popup']
            st.write(f"**Ciudad seleccionada:** {clicked_city}")

            # Filtrar datos para la ciudad seleccionada
            city_data = df[df['Ciudad'] == clicked_city]

            if not city_data.empty:
                # Gráfico de barras de ventas
                fig_bar = px.bar(city_data, x='Ciudad', y='Ventas', title='Ventas por Ciudad')
                st.plotly_chart(fig_bar)

                # Histograma de categorías
                fig_hist = px.histogram(city_data, x='Categoría', title='Distribución de Categorías')
                st.plotly_chart(fig_hist)
            else:
                st.write("No hay datos disponibles para la ciudad seleccionada.")
        else:
            st.write("Haga clic en un marcador para ver los detalles.")
    else:
        st.write("Haga clic en un marcador para ver los detalles.")

if __name__ == "__main__":
    main()
