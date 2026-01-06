import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal de la aplicación
st.header("Dashboard de anuncios de venta de coches en EE.UU.")

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una breve descripción
st.write(
    "Esta aplicación permite explorar visualmente un conjunto de datos "
    "de anuncios de coches usados mediante gráficos interactivos."
)

# Casillas de verificación para controlar los gráficos
show_histogram = st.checkbox("Mostrar histograma del odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión (precio vs odómetro)")

# Histograma
if show_histogram:
    st.write("Distribución del kilometraje (odómetro)")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del odómetro"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if show_scatter:
    st.write("Relación entre el precio y el kilometraje")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Precio vs Odómetro"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


