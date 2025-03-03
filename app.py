import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('players_20.csv')

# Configuración de la página
st.set_page_config(page_title='Sofifa Player Analysis', layout='wide')

# Logo y autor
st.sidebar.image('Captura desde 2025-03-03 12-52-33.png', caption='Proyecto Individual')
st.sidebar.markdown('**Autor:** Antonio Ixmtlahua Reyes')

# Visualización de los primeros n renglones
st.title('Análisis de Jugadores Sofifa')
n_rows = st.slider('Selecciona el número de filas a mostrar', 0, 15000, 10000)
st.dataframe(df.head(n_rows))

# Buscador de información
st.sidebar.header('Buscador de Jugadores')
search_term = st.sidebar.text_input('Ingrese el nombre del jugador')
if st.sidebar.button('Buscar'):
    results = df[df['short_name'].str.contains(search_term, case=False, na=False)]
    st.write(f'Resultados para: {search_term}')
    st.dataframe(results)

# Filtro de información
st.sidebar.header('Filtrado por Nacionalidad')
nationalities = st.sidebar.multiselect('Selecciona las nacionalidades', df['nationality'].unique())
if nationalities:
    filtered_df = df[df['nationality'].isin(nationalities)]
    st.write('Jugadores filtrados por nacionalidad:')
    st.dataframe(filtered_df)

# Histograma
st.header('Distribución de Edades de los Jugadores')
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True)
st.pyplot(plt)
st.markdown('El histograma muestra la distribución de las edades de los jugadores en el dataset, indicando las edades más comunes.')

# Gráfica de barras
st.header('Relación entre Nacionalidad y Cantidad de Jugadores')
plt.figure(figsize=(12, 8))
nat_counts = df['nationality'].value_counts().head(10)
sns.barplot(x=nat_counts.index, y=nat_counts.values)
st.pyplot(plt)
st.markdown('El gráfico de barras muestra las 10 nacionalidades con más jugadores representados en el dataset.')

# Gráfica scatter
st.header('Relación entre Valor y Potencial del Jugador')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='value_eur', y='potential', data=df)
st.pyplot(plt)
st.markdown('El gráfico scatter refleja cómo el valor económico de un jugador (en euros) se relaciona con su potencial.')

# Actualización de datos
st.sidebar.header('Actualizar Datos')
if st.sidebar.button('Actualizar información'):
    st.experimental_rerun()
