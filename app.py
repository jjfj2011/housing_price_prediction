import streamlit as st
import numpy as np
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go

# Cargar modelo entrenado
model = joblib.load('modelo_lightgbm_optimizado.pkl')

# Encabezado decorativo
st.markdown(
    """
    <div style='background-color:#f0f2f6;padding:10px 15px;border-radius:10px;'>
        <h4 style='color:#2e7d32;'>📊 Proyecto de Machine Learning</h4>
        <p>Este modelo predice el precio estimado de una vivienda en California según características geográficas y socioeconómicas.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.title('🏠 Predicción del Precio de Viviendas en California')

# Inicializa el estado si no existe
if 'mostrar_resultado' not in st.session_state:
    st.session_state.mostrar_resultado = False
if 'features' not in st.session_state:
    st.session_state.features = None

# Inputs dentro de un expander
with st.expander("📝 Ingrese las características del inmueble", expanded=True):
    Median_Income = st.number_input('Ingreso Medio (Median Income)', min_value=0.0, value=5.0, step=0.1, key='income')
    Median_Age = st.number_input('Edad Media de las Casas (Median Age)', min_value=1, value=30, key='age')
    Tot_Rooms = st.number_input('Total de Habitaciones (Tot Rooms)', min_value=1.0, value=2000.0, key='rooms')
    Tot_Bedrooms = st.number_input('Total de Dormitorios (Tot Bedrooms)', min_value=1.0, value=400.0, key='bedrooms')
    Population = st.number_input('Población (Population)', min_value=1.0, value=1000.0, key='population')
    Households = st.number_input('Número de Hogares (Households)', min_value=1.0, value=400.0, key='households')
    Latitude = st.number_input('Latitud (Latitude)', min_value=32.0, max_value=42.0, value=36.5, key='latitude')
    Longitude = st.number_input('Longitud (Longitude)', min_value=-125.0, max_value=-113.0, value=-119.5, key='longitude')
    Distance_to_coast = st.number_input('Distancia a la costa (m)', min_value=0.0, value=8000.0, key='coast')
    Distance_to_LA = st.number_input('Distancia a Los Ángeles (m)', min_value=0.0, value=500000.0, key='la')
    Distance_to_SanDiego = st.number_input('Distancia a San Diego (m)', min_value=0.0, value=700000.0, key='sd')
    Distance_to_SanJose = st.number_input('Distancia a San José (m)', min_value=0.0, value=80000.0, key='sj')
    Distance_to_SanFrancisco = st.number_input('Distancia a San Francisco (m)', min_value=0.0, value=20000.0, key='sf')

col1, col2 = st.columns([1, 1])

# Botón de predicción
with col1:
    if st.button('📈 Predecir Precio de Vivienda'):
        st.session_state.features = np.array([[
            Median_Income, Median_Age, Tot_Rooms, Tot_Bedrooms,
            Population, Households, Latitude, Longitude,
            Distance_to_coast, Distance_to_LA,
            Distance_to_SanDiego, Distance_to_SanJose, Distance_to_SanFrancisco
        ]])
        st.session_state.mostrar_resultado = True

# Botón de limpieza
with col2:
    if st.button('🧹 Limpiar Valores'):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state['mostrar_resultado'] = False
        st.session_state['features'] = None
        st.rerun()

# Mostrar predicción y visualización
if st.session_state.mostrar_resultado and st.session_state.features is not None:
    try:
        features = st.session_state.features
        prediction = model.predict(features)[0]
        st.success(f'💰 Precio estimado de la vivienda: ${prediction:,.2f}')

        # Tabla de entrada
        st.markdown("#### 📋 Características del Inmueble")
        cols = ['Median Income', 'Median Age', 'Tot Rooms', 'Tot Bedrooms',
                'Population', 'Households', 'Latitude', 'Longitude',
                'Dist. to Coast', 'Dist. to LA', 'Dist. to San Diego',
                'Dist. to San Jose', 'Dist. to SF']
        df_input = pd.DataFrame(features, columns=cols)
        st.dataframe(df_input)

        # Gráfico tipo gauge
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prediction,
            title = {'text': "Precio Estimado"},
            gauge = {
                'axis': {'range': [0, 500000]},
                'bar': {'color': "green"},
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        # Calcular precio promedio general para decidir color del marcador
        promedio_precio = 250000  # Este valor puedes ajustarlo según tu dataset
        color_icono = 'green' if prediction >= promedio_precio else 'red'

        # Crear mapa centrado en la ubicación ingresada
        m = folium.Map(location=[features[0][6], features[0][7]], zoom_start=8)
        popup_text = f"📍 Lat: {features[0][6]}, Lon: {features[0][7]}<br>💰 Precio estimado: ${prediction:,.2f}"
        tooltip_text = f"💰 ${prediction:,.2f} (Precio estimado)"
        folium.Marker(
            [features[0][6], features[0][7]],
            tooltip=tooltip_text,
            popup=popup_text,
            icon=folium.Icon(color=color_icono, icon='home')
        ).add_to(m)

        st.markdown("### 🌍 Ubicación Geográfica de la Vivienda")
        st_folium(m, width=700, height=500)

    except Exception as e:
        st.error(f"⚠️ Error al hacer la predicción: {e}")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Proyecto desarrollado por: **Frans Benavides**")