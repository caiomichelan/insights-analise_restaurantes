#Import Libraries
import pandas as pd
import numpy as np
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

import plotly.express as px
import inflection


#Load data
df = pd.read_csv('data/base_restaurantes.csv')

# =======================================
# Functions
# =======================================

#Data processing
#Adjusting variables
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}


COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

#Rename columns
def rename_cols(df):
    df1 = df.copy()
    
    title = lambda x: inflection.titleize(x)
    spaces = lambda x: x.replace(' ', '') 
    snakecase = lambda x: inflection.underscore(x)
    
    cols_old = list(df1.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    
    cols_new = list(map(snakecase, cols_old))
    
    df1.columns = cols_new
    
    return df1

#Adjust price type
def price_type(price_range):
    if price_range == 1:
        return 'Cheap'
    elif price_range == 2:
        return 'Normal'
    elif price_range == 3:
        return 'Expensive'
    else:
        return 'Gourmet'
    
#Adjust country names
def country_name(country_id):
    return COUNTRIES[country_id]

#Adjust color names
def color_name(color_code):
    return COLORS[color_code]

#Adjust columns order
def adjust_cols_order(df):
    df1 = df.copy()

    new_cols_order = [
        'restaurant_id',
        'restaurant_name',
        'country',
        'city',
        'address',
        'locality',
        'locality_verbose',
        'longitude',
        'latitude',
        'cuisines',
        'price_type',
        'average_cost_for_two',
        'currency',
        'has_table_booking',
        'has_online_delivery',
        'is_delivering_now',
        'aggregate_rating',
        'rating_color',
        'color_name',
        'rating_text',
        'votes',
    ]
    
    return df1.loc[:, new_cols_order]

#General Data Processing
def process_data(df):
    df = df.dropna()

    df = rename_cols(df)

    df['price_type'] = df.loc[:, 'price_range'].apply(lambda x: price_type(x))

    df['country'] = df.loc[:, 'country_code'].apply(lambda x: country_name(x))

    df['color_name'] = df.loc[:, 'rating_color'].apply(lambda x: color_name(x))

    df['cuisines'] = df.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])

    df = df.drop_duplicates()

    df = adjust_cols_order(df)

    df.to_csv('data/base_restaurantes_tratada.csv', index=False)

    return df
  
#Draw map
def create_map(df):
    fig = folium.Figure(width=800, height=600)

    map = folium.Map(max_bounds=True, titles='World Restaurants').add_to(fig)

    marker_cluster = MarkerCluster().add_to(map)

    for i, line in df.iterrows():
        name = line['restaurant_name']
        price_for_two = line['average_cost_for_two']
        cuisine = line['cuisines']
        currency = line['currency']
        rating = line['aggregate_rating']
        color = f'{line["color_name"]}'
        
        html = '<p><strong>{}</strong></p>'
        html += '<p>Preço p/ dois: {},00 ({})'
        html += '<br />Tipo: {}'
        html += '<br />Nota: {}/5.0'
        html = html.format(name, price_for_two, currency, cuisine, rating)
        
        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )
        
        folium.Marker(
            [line['latitude'], line['longitude']],
            popup = popup,
            icon = folium.Icon(color=color, icon='home', prefix='fa'),
        ).add_to(marker_cluster)
        
    folium_static(map, width=800, height=600)
          
#Data Processing
df = process_data(df)


#Streamlit page config
st.set_page_config(page_title="World Restaurants - Geral", page_icon="🌎", layout="wide")

#Streamlit page title
st.title('World Restaurants - Acompanhamento Geral')

# =======================================
# Side Bar
# =======================================

#Streamlit sidebar config
st.sidebar.markdown('# World Restaurants')
st.sidebar.image('images/restaurant.jpg')
st.sidebar.markdown('## Painel Gerencial')
                    
st.sidebar.markdown('''---''')

#Insert multiselector for filtering
paises = st.sidebar.multiselect(
    'Selecione os países que deseja visualizar:',
    df.loc[:, 'country'].unique().tolist(),
    default = ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])

st.sidebar.markdown('''---''')

st.sidebar.markdown('### Powered by Caio Michelan')

#Data filter on countries
paises_sel = df.loc[:, 'country'].isin(paises)
df = df.loc[paises_sel, :]

# =======================================
# Streamlit Layout
# =======================================

#Metrics
with st.container():
    st.markdown('## Escopo Geral:')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        rest = df['restaurant_id'].nunique()
        col1.metric('Restaurantes Cadastrados: ', '{:,}'.format(rest).replace(',','.'))
        
    with col2:
        paises = df['country'].nunique()
        col2.metric('Países Cadastrados: ', paises)
 
    with col3:
        cidades = df['city'].nunique()
        col3.metric('Cidades Cadastradas: ', cidades)
        
    with col4:
        culinaria = df['cuisines'].nunique()
        col4.metric('Tipos de Culinária: ', culinaria)
    
    av = df['votes'].sum()
    st.metric('Total de avaliações registradas: ', '{:,}'.format(av).replace(',','.'))

#Map
with st.container():
    st.markdown('## Visualização no Mapa:')
    create_map(df)
