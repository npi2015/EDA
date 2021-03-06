import streamlit as st

# Custom imports
from multipage import MultiPage
from pages import introduction, detection_methods, graficos, datos # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Análisis de exoplanetas")

# Add all your applications (pages) here
app.add_page("Introducción", introduction.app)
app.add_page("Métodos de detección", detection_methods.app)
app.add_page("Datos", datos.app)
app.add_page("Visualización", graficos.app)


# The main app
app.run()