import streamlit as st
import pandas as pd
from plotly.offline import iplot, plot
import plotly as py
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_json('C:/Users/cuco2/Desktop/Verano2021/The_Bridge/Archivos de clase/EDA/test.json')


def discovery_methods_plot():
    trace1 = go.Bar(x=df['discoverymethod'].value_counts().index,
                    y=df['discoverymethod'].value_counts(),
                    marker=dict(color=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)']),
                    text=df['discoverymethod'].value_counts())

    layout = go.Layout()

    discovery_methods = go.Figure(data=trace1, layout=layout)

    return discovery_methods


def discovered_planets_plot():
    discovered_planets = px.scatter(df, y='pl_massj', x='pl_orbsmax', color='discoverymethod', symbol='discoverymethod',
                                    opacity=0.8,
                                    hover_name='pl_name',
                                    hover_data={'pl_massj': True, 'pl_orbsmax': True, 'discoverymethod': True,
                                                'pl_name': False},
                                    labels={'discoverymethod': 'Método de descubrimiento', 'pl_massj': 'Masa',
                                            'pl_orbsmax': 'Semieje mayor'})
    discovered_planets.update_xaxes(type="log", title='Semieje mayor (AU)')
    discovered_planets.update_yaxes(type="log", title='Masa (Masa de Jupiter)', tickvals=[0.0001, 0.01, 1, 100],
                                    ticktext=['0.0001', '0.01', '1', '100'], tickmode='array')
    return discovered_planets


def orbper_vs_distance_plot():
    orbper_vs_distance = px.scatter(df, y='pl_orbsmax', x='pl_orbper', opacity=0.5, log_x=True, log_y=True,
                                    color='discoverymethod')
    orbper_vs_distance.update_xaxes(title='Periodo Orbital (días)')
    orbper_vs_distance.update_yaxes(title='Semieje mayor (AU)')
    return orbper_vs_distance


def no_stars_plot():
    stars = px.bar(x=df['sy_snum'].value_counts().index, y=df['sy_snum'].value_counts(),
                   color=df['sy_snum'].value_counts().index.astype(str),
                   labels={'x': 'Número de estrellas', 'y': 'Cuenta'})
    stars.update_xaxes(tickvals=[1, 2, 3, 4])
    return stars


def hot_jupiters_plot():
    hot_jupiters = df[(df['pl_massj'] > 1) & (df['pl_orbper'] < 10)]

    hot_jupiters_chart = px.scatter(hot_jupiters, x='pl_orbper', y='pl_massj', color='discoverymethod',
                                    symbol='discoverymethod',
                                    title='Jupiters Calientes')
    hot_jupiters_chart.update_xaxes(type="log", title='Periodo orbital (días)')
    hot_jupiters_chart.update_yaxes(type="log", title='Masa (Masa de Jupiter)')
    return hot_jupiters_chart


def hot_jupiter_overlay_plot():
    df['hot jupiters'] = (df['pl_massj'] > 1) & (df['pl_orbper'] < 10)

    HJ_overlay = px.scatter(df, x='pl_orbper', y='pl_massj', color='hot jupiters', title='Jupiters Calientes',
                            labels={'hot jupiters': 'Jupiters Calientes'})
    HJ_overlay.update_xaxes(type="log", title='Periodo orbital (días)')
    HJ_overlay.update_yaxes(type="log", title='Masa (Masa de Jupiter)')
    return HJ_overlay


def orbital_plot():
    orbital = px.scatter(df, y='pl_massj', x='pl_orbper', color='discoverymethod', symbol='discoverymethod',
                         opacity=0.8, hover_name='pl_name',
                         hover_data={'pl_massj': True, 'discoverymethod': True, 'pl_name': False},
                         labels={'discoverymethod': 'Método de descubrimiento', 'pl_massj': 'Masa (Masas de Jupiter)',
                                 'pl_orbper': 'Periodo orbital (días)', })
    orbital.update_xaxes(type="log")
    orbital.update_yaxes(type="log", tickvals=[0.0001, 0.01, 1, 100], ticktext=['0.0001', '0.01', '1', '100'],
                         tickmode='array')
    return orbital


def discovery_site_mass_plot():
    disc_site_mass = px.scatter(df, y='pl_massj', x='pl_orbper', color='disc_locale',
                                opacity=0.8, hover_name='pl_name',
                                hover_data={'pl_massj': True, 'discoverymethod': True, 'pl_name': False},
                                labels={'discoverymethod': 'Método de descubrimiento',
                                        'pl_massj': 'Masa (Masas de Jupiter)',
                                        'pl_orbper': 'Periodo orbital (días)',
                                        'disc_locale': 'Sitio de descubrimiento'})
    disc_site_mass.update_xaxes(type="log")
    disc_site_mass.update_yaxes(type="log", tickvals=[0.0001, 0.01, 1, 100], ticktext=['0.0001', '0.01', '1', '100'],
                                tickmode='array')
    return disc_site_mass


def discovery_site_dist_plot():
    disc_site_dist = px.scatter(df, y='pl_massj', x='pl_orbsmax', color='disc_locale',
                                opacity=0.8, hover_name='pl_name',
                                hover_data={'pl_massj': True, 'discoverymethod': True, 'pl_name': False},
                                labels={'discoverymethod': 'Método de descubrimiento',
                                        'pl_massj': 'Masa (Masas de Jupiter)',
                                        'pl_orbsmax': 'Semieje mayor (UA)', 'disc_locale': 'Sitio de descubrimiento'})
    disc_site_dist.update_xaxes(type="log")
    disc_site_dist.update_yaxes(type="log", tickvals=[0.0001, 0.01, 1, 100], ticktext=['0.0001', '0.01', '1', '100'],
                                tickmode='array')
    return disc_site_dist


def app():
    page = st.sidebar.selectbox(
        'Gráfica a mostrar',
        ('Planetas descubiertos (distancia)', 'Planetas descubiertos (periodo)',
         'Planetas descubiertos (lugar de descubrimiento)', 'Métodos de detección', 'Júpiters Calientes',
         'Números de estrellas en un sistema',
         'Periodo orbital contra distancia')
    )

    if page == 'Métodos de detección':
        st.write('''Aquí podemos ver cuantos planetas han sido detectados con cada método. El más común, y por mucho, es 
        el de tránsito primario. Esto probablemente se deba a que Kepler, una misión de la NASA con un telescopio 
        espacial, usaba este método de detección. También, a medida que evoluciona la tecnología, métodos más sofisticados 
        como la astrometría aumentarán sus detecciones. Es muy probable que con el siguiente gran release de datos de 
        GAIA, en 2022, veamos una imagen muy distinta de los datos''')
        st.plotly_chart(discovery_methods_plot())
    elif page == 'Planetas descubiertos (distancia)':
        st.markdown('''En esta gráfica podemos ver la masa de los planetas descubiertos contra su radio orbital(también llamado semieje mayor).
         Hay que mencionar un par de cosas:''')
        st.markdown(
            '''
          <ul>
              <li>Hay muchos planetas cerca de su estrella, pero no muchos a más de 10 AU. Como referencia, sabed que Saturno
                     está a 9,6 AU del Sol, y Urano está a 19 AU. Tienen 0,3 y  0,045 la masa de Júpiter respectivamente.</li>
              <li>Hay muchos planetas pesados cerca de su estrella, algo que no vemos en nuestro Sistema Solar. Estos planetas 
                     son llamados Jupiters Calientes.</li>
              <li>Parece que no hay planetas ligeros lejos de la estrella, pero esto es probablemente un problema con los métodos 
                     de detección, ya que estos planetas no se ven.</li>
              <li>Se puede ver que cada planeta tiene distintas fortalezas: 
                <ul>
                    <li>Tránsito primario detecta planetas cerca de la estrella</li>
                    <li>Velocidad radial nos permite detectar planetas que están un poco más lejos de la estrella</li>
                    <li>Con telescopios (imagen) podemos solo ver planetas grandes, pero estos pueden estar bastante lejos de la 
                estrella. </li>
                    <li>Los demás métodos no tienen suficientes detecciones para determinar sus fortalezas analizando el gráfico</li>
                </ul>
              </li>
          </ul> 
         ''', unsafe_allow_html=True)
        st.plotly_chart(discovered_planets_plot())

    elif page == 'Planetas descubiertos (periodo)':
        st.write('''Si tomamos el Sitema Solar de referencia, creemos que los planetas más pesados son los que más lejos están de la estrella. Esto no es lo que refleja este gráfico. 

Podemos ver que hay muchos planetas con un periodo orbital corto, que tiene sentido porque implica que podemos detectar el planeta varias veces en un tiempo razonable, algo particularmente útil en métodos como el tránsito primario. También podemos ver que este método en particular tiene la mayoría de sus detecciones en planetas con un periodo orbital corto. 

A medida que nos movemos más lejos y el periodo orbital aumenta (y también la distancia), el número de planetas 
detectados decrece. Esto, más que algo que ocurre es un bias en los datos, ya que estos planetas son más díficiles de 
detectar (o de confirmar). No significa que no existan este tipo de planetas. ''')
        st.plotly_chart(orbital_plot())
    elif page == 'Periodo orbital contra distancia':
        st.write('''Aquí vemos la relacion entre periodo orbital y radio orbital. Esta relación es linear, como se puede
        ver en la imagen, ya que cuanto más lejos este un planeta de su estrella más tardará en rotar alrededor. El 
        coficiente de correlacion de Pearson de estos datos es de 0.92''')
        st.plotly_chart(orbper_vs_distance_plot())
    elif page == 'Números de estrellas en un sistema':
        st.write('''Aquí vemos cuantos sistemas con varias estrellas. Lo más común es el sistema con una sola estrella, 
        pero también hay bastantes sistemas binarios. Sistemas trinarios como Alpha Centauri (el más cercano al Sistema 
        Solar) son menos comunes, y cuaternarios aún menos. Estos sistemas ocurren debido a como se forman las estrellas, 
        en nebulosas en las que se forman varios millones de estrellas algunas van a acabar juntas.''')
        st.plotly_chart(no_stars_plot())
    elif page == 'Júpiters Calientes':
        st.write('''Un Júpiter Caliente es un planeta que rstá cerca de su estrella (periodo orbital de menos de 10 
        días) y tiene las caractéristicas de Júpiter (masa o tamaño). Estos planetas son fáciles de detectar debido a su
        tamaño con métodos como el de tránsito primario, como se puede ver en la figura.'''
        
        '''También puedes darle al botón para ver cuantos planetas del total de la base de datos son Júpiters Calientes (230).''')
        overlay = st.checkbox('Ver en overlay')
        if overlay:
            st.plotly_chart(hot_jupiter_overlay_plot())
        else:
            st.plotly_chart(hot_jupiters_plot())
    elif page == 'Planetas descubiertos (lugar de descubrimiento)':
        st.write('''En este caso estamos viendo que tipo de planetas se descubren desde cada local (espacio o tierra).
        Vemos que no hay una correlación entre la masa del planeta y el local de descubrimiento, estando los datos 
        muy mezclados.\n\n'''

                 '''Viendo el segundo gráfico (dale al botón), vemos que aquí los datos se separan más. Hay muchas 
                 detecciones desde la tierra en planetas que están cerca de la estrella, pero a medida que nos 
                 alejamos las detecciones desde telescopios terrestres se reducen. Esto se debe a la presencia de la 
                 atmósfera, que distorsiona la luz y hace estos planetas más díficiles de detectar.''')
        mass_or_distance = st.checkbox('Ver masa contra distancia a la estrella')
        if mass_or_distance:
            st.plotly_chart(discovery_site_dist_plot())
        else:
            st.plotly_chart(discovery_site_mass_plot())
