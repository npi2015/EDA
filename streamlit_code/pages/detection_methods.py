import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown('## Métodos de detección')

    st.markdown('Aquí veremos brevemente los distintos métodos de detección presentes en la base de datos.')

    with st.beta_expander('Tránsito primario', expanded=True):
        st.markdown('''Este método consiste en analizar el flujo proveniente de la estrella. Cuando se detecta un 
        mínimo en este flujo periódicamente, este se suele deber a un planeta que transita la estrella, 
        ya que al pasar por delante de la estrella, el planeta bloquea parte de la luz haciéndola parecer menos 
        luminosa. El video mostrado a continuación muestra esto de manera gráfica''')

        st.video('https://www.youtube.com/watch?v=BFi4HBUdWkk')

        st.write('Fuente: NASA Video en Youtube')

    with st.beta_expander('Velocidad radial'):
        st.markdown('''Una estrella no está completamente estacionario, sino que se mueve ligeramente debido a las 
        interacciones gravitacionales con los planetas que la orbitan. Estos movimientos causan que la estrella se 
        aleje de nosotros en momentos y que luego se acerque. Al alejarse la luz emitida por la estrella es *corrida 
        hacia el rojo* (se vuelve más roja), mientras que cuando se acerca a nosotros la luz se vuelve más azul (
        *corrimiento al azul*).\n\n '''

                    '''Con un espectrógrafo podemos analizar la luz de la estrella, y si vemos que esta sufre estos 
                    movimientos de manera periódica podemos inferir que hay un planeta orbitándola. También es 
                    posible deducir la masa del planeta a partir de este método. ''')

        st.video('https://www.youtube.com/watch?v=WK0WAmiP_Dk')

        st.write('Fuente: NASA Video en Youtube')

    with st.beta_expander('Imagen directa'):
        st.write('''Este simplemente consiste en ver el planeta de manera directa con un telescopio. Debido a la 
        distancia a la que los exoplanetas están de nosotros, es muy difícil detectar planetas de este modo. Incluso 
        sabiendo dónde buscar, es muy difícil ver exoplanetas con un telescopio.''')

    with st.beta_expander('Microlente gravitacional'):
        st.write('''Cuando una estrella poco luminosa se interpone ente la Tierra y una estrella más brillante, 
        actúa como una lupa, creando dos imágenes de la estrella más brillante. Esto es una 
        lente gravitacional.\n\n '''

                 '''Si hay un planeta orbitando la estrella menos luminosa, entonces está añade al efecto de lente 
                 gravitacional, creando un máximo local en el brillo de la estrella más lejana. Este [video] (
                 https://www.youtube.com/watch?v=_aZZt8dM-_0 "Microlente gravitacional (en inglés)") lo explica 
                 bastante bien.''')

        gravitational_lens = open("streamlit_code/pages/Gravitational_lens.gif", "rb")
        contents = gravitational_lens.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        gravitational_lens.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="gravitational_lens_gif" width = "650">',
            unsafe_allow_html=True,
        )
        st.write('''Fuente: De Lensshoe_hubble.jpg: ESA/Hubble &amp; NASAderivative work: Bulwersator (talk)
         - Lensshoe_hubble.jpg, Dominio público, https://commons.wikimedia.org/w/index.php?curid=17750437''')

    with st.beta_expander('Variación de tiempo de tránsito'):
        st.write('''En sistemas con varios planetas, las interacciones gravitacionales entre planetas pesados y 
        ligeros causa que los planetas se aceleran y frenen durante una órbita alrededor de su estrella. Esto hace 
        que el periodo orbital de cada planeta cambie en cada órbita, permitiendo detectar planetas con una masa como 
        la de la Tierra. '''

                 '''Un planeta pesado que podemos ver mediante otros métodos tendrá fluctuaciones en su periodo 
                 orbital debido a que un planeta más ligero está interactuando con él y causa que cambie de 
                 velocidad. El primer planeta detectado con este método fue Kepler 19c en 2011''')

        st.video(
            '''https://upload.wikimedia.org/wikipedia/commons/9/96/201008-2a_PlanetOrbits_16x9-_Transit_timing_of_1-planet_vs_2-planet_systems.ogv''')

        st.write('''Fuente: NASA Ames Research Center/Kepler Mission, Public domain, via Wikimedia Commons''')
    with st.beta_expander('Variación de tiempo de eclipse'):
        st.write('''En un sistema binario eclipsante (en el que una estrella se interpone entre la otra y la Tierra de 
                 manera periódica) podemos determinar con precisión cuando ocurren los eclipses. Con un exoplaneta
                 presente, las interacciones gravitacionales pueden causar que los eclipses ocurran antes o después de 
                 lo predicho.\n\n'''

                 '''Este método solo puede detectar planetas pesados, ya que de lo contrario la interacción 
                 gravitacional con la estrella es muy pequeña y díficil de detectar.''')

        sistema_binario = Image.open('streamlit_code/pages/eclipsing_binaries.jpg')
        st.image(sistema_binario, '''Medición del brillo de un sistema binario. Con un planeta presente, los mínimos 
        estarían ligeramente desplazados.''')

    with st.beta_expander('Variación de tiempo de púlsares'):
        st.write('''Un pulsar es un tipo de estrella de neutrones que rota a mucha velocidad, emitiendo pulsos 
        electromagnéticas periódicamente. Como estos pulsos son muy regulares (entre milisegundos y segundos) si se 
        observan variaciones periódicas en su ocurrencia estas se tienen que deber a la interacción del pulsar con algo, 
        normalmente un planeta.'''

                 '''Los primeros exoplanetas se detectaron mediante este método''')

    with st.beta_expander('Variación de tiempo de pulsaciones'):
        st.write('''Hay otros tipos de estrellas que emiten pulsaciones de manera regular, como las Cefeidas. Empleando
        una lógica similar a la utilizada con los púlsares, se pueden detectar exoplanetas que orbitan este tipo de 
        estrellas.''')

    with st.beta_expander('Cinemática de discos protoplanetarios'):
        st.write('''Consiste en encontrar exoplanetas debido a su interacción con discos protoplanetarios. Mediante 
        este método es posible encontrar proto-planetas (planetas en proceso de formación).''')

    with st.beta_expander('Astrometría'):
        st.write('''La astrometría consiste en detectar el movimiento de una estrella midiendo su posición en el cielo. 
        Su uso en la detección de exoplanetas consiste en medir pequeños (muy pequeños) cambios en la posición de la
        estrella mientras se mueve debido a la interacción con los planetas que la orbitan. Requiere una precisión muy 
        alta para detectar exoplanetas. La misión GAIA de la ESA utiliza este método para detectar exoplanetas''')

        st.video('''https://youtu.be/4u_dVKKRoPw''')

        st.write('Fuente: ESA')

    with st.beta_expander('Cambios en el brillo orbital'):
        st.write('''Planetas con un periodo corto alrededor de una estrella experimentan variaciones en la luz que reflejan ya 
        que, como la Luna, pasan por varias fases. También, ya que reciben mucha luz de su estrella, estos planetas 
        se calientan, haciendo posible detectar sus emisiones térmicas. Al no poder resolver con un telescopio la luz 
        del planeta y de la estrella (solo se ve la luz combinada de ambas), y la luz de la estrella parace cambiar 
        en cada órbita de manera periódica, es posible detectar planetas del tamaño de Júpiter y con un periodo 
        orbital de varios días se pueden detectar con telescopios espaciales como el Kepler Space Obsevatory. '''
                 
        '''Fuente: Wikipedia: Methods of detecting exoplanets''')


