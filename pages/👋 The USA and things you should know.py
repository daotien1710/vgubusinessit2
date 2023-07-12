import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
import plotly.express as px 

st.set_page_config(page_title="The USA and things you should know",page_icon="🇺🇸",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[The USA - what are there to know?]')
st.write(" ")

colored_header(
    label="An introduction 💡",
    description="About the United States of America",
    color_name="light-blue-70",)
left_column, right_column = st.columns(2)
with left_column:
    annotated_text(("United States","🇺🇸","#1B6B93"),", officially United States of America, abbreviated U.S. or U.S.A., byname America, country in North America, a federal republic of 50 states. Besides the 48 conterminous states that occupy the middle latitudes of the continent, the United States includes the state of Alaska, at the northwestern extreme of North America, and the island state of Hawaii, in the mid-Pacific Ocean. The conterminous states are bounded on the north by Canada, on the east by the Atlantic Ocean, on the south by the Gulf of Mexico and Mexico, and on the west by the Pacific Ocean. The United States is the fourth largest country in the world in area (after Russia, Canada, and China).",("The national capital is Washington","📍","#1B6B93"),", which is coextensive with the District of Columbia, the federal capital region created in 1790.")

with right_column:
    st.lottie("https://assets4.lottiefiles.com/packages/lf20_vwcugezu.json",key="usa")

colored_header(
    label="The economy 💰",
    description="The United States is a highly developed mixed economy",
    color_name="blue-70",)
column1, column2 = st.columns(2)
with column1:
    st.lottie("https://assets10.lottiefiles.com/private_files/lf30_oOGQFY.json",key="economy")
with column2:
    annotated_text("The United States is a highly developed mixed economy. It is the world's largest economy by nominal GDP, and the second-largest by ",("purchasing power parity","PPP","#4FC0D0")," behind China. It has the world's seventh-highest per capita GDP (nominal) and the eighth-highest per capita GDP (PPP) as of 2022. The U.S. accounted for 25.4 percent of the global economy in 2022 in nominal terms, and around 15.6 percent in PPP terms. The U.S. dollar is the currency of record most used in international transactions and is the world's reserve currency, backed by a large U.S. treasuries market, its role as the reference standard for the petrodollar system, and its linked eurodollar. Several countries use it as their official currency and in others it is the de facto currency.")

st.subheader("GDP per capita in the US (2022)")
load = pd.read_csv('States-Behavior-And-More-MainSheet.csv')

geoif =  {'state_code' : [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
          'State' : ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'District of Columbia',
            'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
            'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina',
            'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma',
            'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia',
            'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
         }

geoif = pd.DataFrame(geoif)

df1 = load.merge(geoif, on='State', how='left')

df1.rename({'FIPS Code':'FIPS'},axis=1, inplace=True)

fig1 = px.choropleth(df1,
                    locations='state_code',
                    locationmode="USA-states",
                    scope="usa",
                    color='GDP.Per.Capita',
                    color_continuous_scale="agsunset_r",
                    labels={'GDP.Per.Capita':'GDP per capita'},
                    hover_name = 'State', hover_data=["State","GDP.Per.Capita"]
                    )


st.plotly_chart(fig1)

colored_header(
    label="The population (2020)",
    description="The US is having a population of nearly 328 million people (2021), increasingly driven by immigrants. The U.S. is a country of 50 states covering a vast swath of North America. ",
    color_name="blue-green-70",)

load = pd.read_csv('USA-Covid-Data.csv')

geoinfo =  {'state_code' : [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
          'State' : ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'District of Columbia',
            'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
            'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina',
            'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma',
            'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia',
            'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
         }


geoinfo = pd.DataFrame(geoinfo)

df = load.merge(geoinfo, on='State', how='left')

df.rename({'FIPS Code':'FIPS'},axis=1, inplace=True)

fig1 = px.choropleth(df,
                        locations='state_code',
                        locationmode="USA-states",
                        scope="usa",
                        color='Population',
                        color_continuous_scale="Viridis_r",
                        labels={'Population':'Population'},title="The US population in 2020",
                        hover_name= 'State', hover_data=["State","Population"]
                        )

st.plotly_chart(fig1)
