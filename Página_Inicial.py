#Import Libraries
import pandas as pd
import numpy as np
import streamlit as st

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
st.set_page_config(page_title="World Restaurants - Início", page_icon="🌎", layout="wide")

#Streamlit page title
st.title('World Restaurants - Página Inicial')

# =======================================
# Side Bar
# =======================================

#Streamlit sidebar config
st.sidebar.markdown('# World Restaurants')
st.sidebar.image('images/restaurant.jpg')
st.sidebar.markdown('## Painel Gerencial')

st.sidebar.markdown('''---''')

st.sidebar.markdown('### Download dos Dados (Arquivo CSV):')

st.sidebar.download_button(
        label="Download",
        data=df.to_csv(index=False, sep=";"),
        file_name="world_restaurants-database.csv",
        mime="text/csv",
    )

st.sidebar.markdown('Base de dados processada e atualizada!')

st.sidebar.markdown('''---''')

st.sidebar.markdown('### Powered by Caio Michelan')


# =======================================
# Streamlit Layout
# =======================================


#About, Overall instructions and help contact
st.markdown(
    '''
    ## Sobre: 
    
    Este Painel Gerencial foi desenvolvido para proporcionar análises assertivas sobre os restaurantes cadastrados na plataforma "World Restaurants" e fornecer Insights valiosos para tomadas de decisões estratégicas da empresa!
    
    
    ---
    
    ### Como Utilizar?
    
    Pelo Menu disponibilizado na Barra Lateral à esquerda, basta navegar entre as diferentes visões:
    
    - Visão Geral:
        - Escopo geral dos restaurantes registrados na Base de Dados
        - Visualização dos Restaurantes no Mapa
        
    - Visão Países:
        - Principais indicadores para análise dos restaurantes por País
        
    - Visão Cidades:
        - Principais indicadores para análise dos restaurantes por Cidade
        
    - Visão Culinária:
        - Principais indicadores para análise dos restaurantes por Tipo de Culinária oferecida
    ---
    
    ### Ajuda:
    
    - Em caso de dúvidas, sugestões ou demais considerações, fique à vontade para entrar em contato:
        - https://github.com/caiomichelan
     
    '''
)

