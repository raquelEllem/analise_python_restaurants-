import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


#---------------------------------
# Funções
#---------------------------------

def read_processed_data():
    return pd.read_csv("zomato.csv")



def make_sidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return list(countries)


def top_cities_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country", "city"]]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 10 Cidades com mais Restaurantes na Base de Dados",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def top_best_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] >= 4) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com Restaurantes com média de avaliação acima de 4",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def top_worst_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] <= 2.5) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def most_cuisines(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["cuisines", "country", "city"]]
        .groupby(["country", "city"])
        .nunique()
        .sort_values(["cuisines", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="cuisines",
        text="cuisines",
        color="country",
        title="Top 10 Cidades com mais restaurantes com tipos culinários distintos",
        labels={
            "city": "Cidades",
            "cuisines": "Quantidade de Tipos Culinários Únicos",
            "country": "País",
        },
    )

    return fig



st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

df = read_processed_data()

countries = make_sidebar(df)

st.markdown("# :cityscape: Visão Cidades")

fig = top_cities_restaurants(countries)

st.plotly_chart(fig, use_container_width=True)

best, worst = st.columns(2)


with best:
        fig = top_best_restaurants(countries)

        st.plotly_chart(fig, use_container_width=True)

with worst:
    fig = top_worst_restaurants(countries)

    st.plotly_chart(fig, use_container_width=True)

fig = most_cuisines(countries)

st.plotly_chart(fig, use_container_width=True)
