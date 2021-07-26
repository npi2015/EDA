import streamlit as st
import pandas as pd

def app():
    st.write("""Los datos utilizados en este proyecto se obtuvieron desde la base de datos de exoplanetas de la NASA. 
    Al contener esta mucha información, en este caso me he centrado solo en un cierto tipo de datos, y solo he escogido
    las siguientes columnas.""")

    with st.beta_expander('Descripción de las columnas'):
        st.table(columns)

    st.write("""Debido a que distintos experimentos han detectado el mismo planeta había varios duplicados en el 
    dataset. Para no perder esa información que puede resultar valiosa se ha realizado un *groupby* usando el nombre
    del planeta junto con un agg tomando distintas características dependiendo del tipo de dato (media y primer dato).
    Esta tabla contiene las operaciónes realizadas con el aggregate:""")

    with st.beta_expander('Operaciones realizadas'):
        st.table(operations)

    st.write('''Tras estas operaciones, el dataframe final tenía la siguiente pinta''')

    with st.beta_expander('Dataframe final (50 primeros elementos)'):
        st.dataframe(pd.read_json('C:/Users/cuco2/Desktop/Verano2021/The_Bridge/Archivos de clase/EDA/test.json').head(50))


# TODO: move dataframes to another file and import them

columns = pd.DataFrame({'ast_flag': '''Bandera indicando si la estrella se ha detectado usando astrometría.''',
                                           'cb_flag': 'Bandera indicando si el planeta orbita un sistema binario',
                                           'disc_locale': '''Indica si el planeta se ha detectado desde la Tierra 
                                           o desde el espacio''',
                                           'discoverymethod': '''Indica con que método se descubrió el planeta''',
                                           'sy_snum': '''Número de estrellas en el sistema''',
                                           'dkin_flag': '''Indica si el planeta se ha detectado mediante cinemática de
                                           discos''',
                                           'etv_flag': '''Indica si el planeta se ha detectado mediante variaciones en 
                                           el tiempo de eclipse''',
                                           'ima_flag': '''Indica si el planeta fue detectado viéndolo directamente''',
                                           'obm_flag': '''Indica si el planeta se detecto mediante variaciones en 
                                           el brillo orbital''',
                                           'pl_masse': 'La masa del planeta como múltiplo de la masa de la Tierra',
                                           'pl_massj': 'La masa del planeta como múltiplo de la masa de la Tierra',
                                           'pl_msinie': 'Masa mínima del planeta en masas de la Tierra',
                                           'pl_msinij': 'Masa mínima del planeta en masas de Júpiter',
                                           'pl_orbeccen': 'Excentricidad de la órbita',
                                           'pl_orbper': 'Periodo orbital del planeta',
                                           'pl_orbsmax': 'El semieje mayor de la órbita',
                                           'pl_rade': 'Radio del planeta en radios de la Tierra',
                                           'pl_radj': 'Radio del planeta en radios de Júpiter',
                                           'pl_tranmid': '''El tiempo que tarda el planeta en cruzar la estrella de 
                                           un lado a otro visto desde la Tierra''',
                                           'ptv_flag': '''Indica si el planeta se detecto mediantes variaciones de 
                                           tiempo de pulsación.''',
                                           'pul_flag': '''Indica si el planeta se detecto mediante variaciones de 
                                                       tiempo de pulsar''',
                                           'rv_flag': '''Bandera indicando si la estrella exhibe variaciones de 
                                           velocidad radial debido al planeta''',
                                           'st_age': 'La edad de la estrella',
                                           'st_mass': 'La masa de la estrella en masas solares',
                                           'st_rad': 'El radio de la estrella, medido en radios solares',
                                           'st_teff': 'La temperatura de la estrella en Kelvin',
                                           'sy_dist': 'Distancia al sistema en parsecs',
                                           'sy_pnum': 'Número de planetas en el sistema',
                                           'sy_snum': 'Número de estrellas en el sistema',
                                           'tran_flag': '''Bandera indicando si el planeta se ha detectado mediante 
                                           tránsito primario'''
                                           }, index = [0]).T

operations = pd.DataFrame({'ast_flag': 'first',
                                           'cb_flag': 'max',
                                           'disc_locale': 'first',
                                           'discoverymethod': 'first',
                                           'sy_snum': 'max',
                                           'dkin_flag': 'max',
                                           'etv_flag': 'max',
                                           'ima_flag': 'max',
                                           'obm_flag': 'max',
                                           'pl_masse': 'mean',
                                           'pl_massj': 'mean',
                                           'pl_msinie': 'mean',
                                           'pl_msinij': 'mean',
                                           'pl_orbeccen': 'max',
                                           'pl_orbper': 'max',
                                           'pl_orbsmax': 'max',
                                           'pl_rade': 'mean',
                                           'pl_radj': 'mean',
                                           'pl_tranmid': 'mean',
                                           'ptv_flag': 'max',
                                           'pul_flag': 'max',
                                           'rv_flag': 'max',
                                           'st_age': 'mean',
                                           'st_mass': 'mean',
                                           'st_rad': 'mean',
                                           'st_teff': 'mean',
                                           'sy_dist': 'mean',
                                           'sy_pnum': 'max',
                                           'sy_snum': 'max',
                                           'tran_flag': 'max'
                                           }, index = ['operación']).T

