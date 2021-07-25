import streamlit as st
from PIL import Image


# @st.cache
def app():
    st.markdown("## Introducción")
    exoplanetas_imagen = Image.open('streamlit/pages/exoplanetas.jpg')
    st.image(exoplanetas_imagen)
    st.markdown('''En este análisis exploratorio analizamos los exoplanetas presentes en la base de datos de exoplanetas 
     de la NASA (disponible [aquí](https://exoplanetarchive.ipac.caltech.edu/ "Nasa Exoplanet Archive")). En esta base de 
     datos tenemos información de varios telescopios, como [Hubble] (https://www.nasa.gov/mission_pages/hubble/main/index.html 
     "Telescopio Espacial Hubble (en inglés)") o [Kepler] (https://www.nasa.gov/mission_pages/kepler/overview/index.html 
     "Proyecto Kepler (en inglés)"), y observatorios.\n\n'''
     
     '''Debido a que cada telescopio y observatorio se especializa en cosas distintas (distintas partes del espectro electromagnético, 
     distintas técnicas de detección de exoplanetas...) en este dataset hay muchos datos. En este EDA nos centraremos principalmente 
     en los que tienen que ver con los exoplanetas y no con las estrellas a las que orbitan.\n\n'''
    
     '''Empezaremos dando una breve explicación a los distintos métodos de detección más utilizados, para luego analizar los
     datos en gráficos y explicar su posible significado. Se hará principal hincapié en los llamados Júpiters calientes y se acabará
     con un pequeño análisis sobre los tipos de sistemas estelares presentes en el dataset.''')