# EDA Exoplanetas
## Motivación
Me parecía interesante realizar un analisis exploratorio de estos datos para ver que forma tienen, ya que es algo que he visto este año y era una oportunidad única para profundizar más y ver un caso práctico en el que aplicar mis conocimientos. También era una oportunidad para aprender cosas nuevas, como métodos de detección y por qué funcionan.
## Recursos utilizados
 * Python 3.9
 * Pandas 1.3.1
 * Numpy 1.21.0
 * Matplotlib 4.2.1
 * Seaborn 0.11.1
 * Pyvo 1.1
 * Plotly 5.1.0
 * Streamlit 0.84.0

Bases de datos:
  * [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) 

## Problemas encontrados

Parece que a Streamlit no le gusta mucho los imports relativos (Python no da error pero streamlit no renderiza bien). Este problema está por ahora parcheado pero no solucionado, he tenido que usar absolute paths y un json para solventar este problema. 

Por lo demás todo ha sido bastante simple. Los datos estaban bien organizados y juntarlos ha sido tan fácil como hacer un aggregate. Hacer los gráficos también ha sido simple usando seaborn y plotly express, que hacen de la sintaxis algo muy simple. Quizá lo más díficil fue conseguir el diagrama de barras con los ejes cortados, ya que ha hecho falta mucho código para lograrlo. 

El notebook es un draft, tiene comentarios míos y alguna celda que da error. Está bien para leer los datos, pero está todo en inglés. Para el que no sepa de esto recomiendo ver primero el dashboard en streamlit, que contiene explicaciones de los métodos de detección y el significado de los gráficos. 

## Contacto

Si hay cualquier duda o problema, por favor escribimde a cuco20011@gmail.com


