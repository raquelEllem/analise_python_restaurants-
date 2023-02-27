import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static


#from utils.process_data import process_data


import inflection


RAW_DATA_PATH = f"zomato.csv"


#========================
#   0.1. Helper Variables
#========================

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

#========================
#   0.2. Helper Functions
#========================

def rename_columns(dataframe):
    """  Esta função tem a responsabilidade de limpar o dataframe
    
    Tipos de limpeza: 
    1. Remoção dos espaços das variáveis de texto
    2. Mudança de nome das colunas
    
    Input: Dataframe
    Output: Dataframe       
    """
    
    df = dataframe.copy()

    title = lambda x: inflection.titleize(x)

    snakecase = lambda x: inflection.underscore(x)

    spaces = lambda x: x.replace(" ", "")

    cols_old = list(df.columns)

    cols_old = list(map(title, cols_old))

    cols_old = list(map(spaces, cols_old))

    cols_new = list(map(snakecase, cols_old))

    df.columns = cols_new
    return df


def country_name(country_id):
    """ Troca o código por nomes na coluna paises    """
    return COUNTRIES[country_id]


def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"
    
def color_name(color_code):
    return COLORS[color_code]


def adjust_columns_order(dataframe):
    df = dataframe.copy()

    new_cols_order = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df.loc[:, new_cols_order]

def process_data(file_path):
    """  Esta função tem a responsabilidade de modificar  o dataframe
    
    Tipos de limpeza: 
    1. Criação de uma coluna com os nomes dos paises
    2. Criação de uma coluna de categoria de comida 
    3. Criação uma coluna com o nome das Cores
 
    
    Input: Dataframe
    Output: Dataframe       
    
    """
    
    df = pd.read_csv(file_path)

    df = df.dropna()

    df = rename_columns(df)
    
    #Criação de uma coluna com os nomes dos paises de acordo com os códigos
    df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x))
    
    #Criação de uma coluna de categoria de comida 
    df["price_type"] = df.loc[:, "price_range"].apply(lambda x: create_price_tye(x))
    
    #Criação do nome das Cores
    df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x))

    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
    
    
    df = df.drop_duplicates()

    df = adjust_columns_order(df)

    df.to_csv("zomato.csv", index=False)

    return df


def create_sidebar(df):
    image = Image.open('logo.png')
    st.sidebar.image(image, width=120)

    col1, col2 = st.sidebar.columns([1, 4], gap="small")
    #col1.image(image, width=35)
    col2.markdown("# Fome Zero")

    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    st.sidebar.markdown("### Dados Tratados")

    processed_data = pd.read_csv("zomato.csv")

    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )

    return list(countries)


def create_map(dataframe):
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in dataframe.iterrows():

        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768)

#========================
#   0.3. Load Data
#========================

df_raw = pd.read_csv(RAW_DATA_PATH)
df_raw.head()

#========================
#   1. DATA DESCRIPTION
#========================
df1 = df_raw.copy()

#========================
#   1.1 Rename Columns
#========================

df1 = rename_columns(df1)

#========================
#   1.2 Check NA and Treat NA
#========================
df1.isna().sum()
df1 = df1.dropna()
df1.isna().sum()

#========================
#   2. Barra Lateral
#========================


st.set_page_config(
    page_title='Home',
    page_icon='📊',
    layout='wide'
)




selected_countries = create_sidebar(df1)



#========================
#   3. Página Principal
#========================

st.markdown('# Fome Zero!')
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')
st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")


restaurants, countries, cities, ratings, cuisines = st.columns(5)

with restaurants:
    restaurant_uniques = len(df1.loc[:, 'restaurant'].unique())
    restaurants.metric(label='Restaurantes Cadastrados', value=restaurant_uniques)
    

with countries:
    countries_uniques = len(df1.loc[:, 'country'].unique())
    countries.metric('Países Cadastrados', countries_uniques)

with cities:
    cities_uniques = len(df1.loc[:, 'city'].unique())
    cities.metric('Cidades Cadastrados', cities_uniques)
    
with ratings:
    total_ratings = df1.loc[:, 'votes'].sum()
    ratings.metric('Avaliações Feitas na Plataforma', total_ratings)
    

with cuisines:
    total_cuisines = df1.loc[:, 'cuisines'].nunique()
    cuisines.metric('Tipos de Culinárias Oferecidas', total_cuisines)
    

    
map_df = df1.loc[df1["country"].isin(selected_countries), :]

create_map(map_df)
