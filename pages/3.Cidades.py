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

          
#Data Processing
df = process_data(df)


#Streamlit page config
st.set_page_config(page_title="World Restaurants - Cidades", page_icon="🌎", layout="wide")

#Streamlit page title
st.title('World Restaurants - Visão Cidades')

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

#Top 10 cities with more restaurants bar graph
with st.container():
    
    st.markdown('### Top 10 Cidades com Mais Restaurantes registrados:')
    
    df_aux = (df.loc[:, ['restaurant_id' , 'city']]
              .groupby('city')
              .nunique()
              .sort_values('restaurant_id', ascending=False)
              .reset_index())
    
    fig = px.bar(df_aux.head(10),
               x='city',
               y='restaurant_id',
               text='restaurant_id',
               text_auto='.0f',
               #title='Top 10 Cidades com mais Restaurantes',
               color='city',
               labels={
                   'city':'Cidade',
                   'restaurant_id':'QTD Restaurantes',
               })
    
    st.plotly_chart(fig, use_container_width=True)


with st.container():
    
    col1, col2 = st.columns(2)
    
    
    #Top 5 cities with best ratings bar graph
    with col1:
        st.markdown('### Top 5 Cidades com as Melhores Avaliações (Acima de 4.6):')
        
        cond = df['aggregate_rating']>4.6
        df_aux = (df.loc[cond, ['restaurant_id', 'city', 'aggregate_rating']]
                  .groupby('city')
                  .count()
                  .sort_values('restaurant_id', ascending=False)
                  .reset_index()
                  .head(5))
        
        fig = px.bar(df_aux,
                x='city',
                y='restaurant_id',
                text='restaurant_id',
                text_auto='.0f',
                #title='Top 5 Cidades com as Melhores Avaliações (Acima de 4.6)',
                color='city',
                labels={'city':'Cidade',
                       'restaurant_id':'QTD Restaurantes'})
        
        st.plotly_chart(fig, use_container_width=True)
        
        #Top 5 cities with worst ratings bar graph
        with col2:
            st.markdown('### Top 5 Cidades com as Piores Avaliações (Abaixo de 2.0):')
            
            cond = df['aggregate_rating']<2.0
            df_aux = (df.loc[cond, ['restaurant_id', 'city', 'aggregate_rating']]
                      .groupby('city')
                      .count()
                      .sort_values('restaurant_id', ascending=False)
                      .reset_index()
                      .head(5))
            
            fig = px.bar(df_aux,
                    x='city',
                    y='restaurant_id',
                    text='restaurant_id',
                    text_auto='.0f',
                    #title='Top 5 Cidades com as Piores Avaliações (Abaixo de 2.0)',
                    color='city',
                    labels={'city':'Cidade',
                           'restaurant_id':'QTD Restaurantes'})
            
            st.plotly_chart(fig, use_container_width=True)

#Top 10 cities with more variety of culinary types bar graph            
with st.container():    
    
    st.markdown('### Top 10 cidades com maior variedade de Tipos de Culinária:')
    
    df_aux = (df.loc[:, ['cuisines', 'city']]
              .groupby('city')
              .nunique()
              .sort_values('cuisines', ascending=False)
              .reset_index()
              .head(10))
    
    fig = px.bar(df_aux,
            x='city',
            y='cuisines',
            text='cuisines',
            text_auto='.0f',
            #title='Top 10 Cidades com maior variedade de Tipos de Culinária',
            color='city',
            labels={'city':'Cidade',
                   'cuisines':'QTD Tipos Culinária'})
    
    st.plotly_chart(fig, use_container_width=True)

#Overall restaurant numbers by city dataframe
with st.container():
    
    st.markdown('### Quantidade Total de Restaurantes por Cidade:')
    
    df_aux = (df.loc[:, ['restaurant_id', 'city']]
              .groupby('city')
              .nunique()
              .sort_values('restaurant_id', ascending=False)
              .reset_index())
    df_aux.rename(columns={'city':'Cidade', 'restaurant_id':'QTD_Restaurantes'}, inplace=True)
    st.dataframe(df_aux, width=800, height=600)

