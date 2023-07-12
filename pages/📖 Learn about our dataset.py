import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text

st.set_page_config(page_title="Learn about our dataset", page_icon="📖", layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Learn about our dataset]')

prompt = st.text_input('What is your name?')
if prompt:
    st.write(f":blue[**Hello *{prompt}*, we are delighted that you want to join us on this amazing data visualization journey 🫰🤗**]")
st.markdown("---")
colored_header(
    label="Let's get to know about our dataset",
    description="We think you may want to read this...",
    color_name="light-blue-70",)

st.write("**Our reason:** The chosen database for our project is about the employment rate in the US from 1976 to 2022. Employment and unemployment rates have remained to be one of the matters that are in the center of attention ever since several crises that severely affected the US’s labor market such as the financial crisis in 2008 and the Covid-19 pandemic in 2019. This is the reason why we chose this topic to be our main data to analyze its impacts on not only the job market but also the economy of the US in general. ")
st.write("**Our goal:** This data is of utmost importance for most people, especially students who are about to enter the workforce like us. We believe this data could help us see the pattern of the job market after crises so that students could better understand and prepare for what is about to come next.")
st.write("**Our way:** We use different types of graph such as line graph, bar graph, and map to demonstrate our analysis and findings. Through these visualizations, we hope to bring the most comprehensive illustration out of an enormous data set that details and information could hardly be drawn.")

cl1, cl2 = st.columns(2)
with cl1:
    st.write("With our interactive web, users could freely experience our carefully designed graphs and figures with ease and find out interesting numbers about a fast changing job market in the US. By typing your name in the “What is your name?” box, you will receive the most personalized experience. This is the experience that we strive to deliver from the beginning as one of the main goals of creating this web beside demonstrating data.")
with cl2:
    st.lottie("https://assets9.lottiefiles.com/packages/lf20_G2nVPR715x.json",key="data")

st.write("**Our data set:** our data collection includes Total Civilian of Non-Institutional Population, Total Civilian Labor Force, Percent of Population, Total number of Employed Workers, Percent of Employed Population, Total number of Unemployed Workers, Percent of Unemployed Population.")
st.write("Our findings: Through data visualization, we found that there are great fluctuations in employment rate and unemployment rate during the researched period. To discover thoroughly, please continue to explore our graphs and figures by","[ clicking here.](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link&ouid=114022649098492793407&rtpof=true&sd=true)")

st.markdown("---")

st.subheader("Datasets' variables introduction")
choice = st.selectbox('Please select the datasets you want to learn about:',('Main dataset','Sub dataset - The US population','Sub dataset - The US GDP per capita per state'))
st.caption(f"You selected: {choice}")

if choice == 'Main dataset':
    st.write("**VARIABLES:**")
    st.markdown("1. :blue[**FIPS Code:**] numbers which uniquely identify states in the USA")
    st.markdown("2. :blue[**Area:**] names of 51 states in the USA")
    st.markdown("3. :blue[**Year:**] the year which the statistics are reported")
    st.markdown("4. :blue[**Month:**] the year which the statistics are reported")
    st.markdown("5. :blue[**Total_Civilian_Non_Institutional_Population_in_Area:**] refers to people 16 years of age and older who are not inmates of institutions (penal, mental facilities, homes for the aged), and who are not on active duty in the Armed Forces")
    st.markdown("6. :blue[**Total_Civilian_Labor_Force_in_Area:**] is the U.S. civilian population that the Bureau of Labor Statistics (BLS) classifies as either employed or unemployed")
    st.markdown("7. :blue[**Percent_(%)_of_Area's_Population:**] the ratio of *Total_Civilian_Labor_Force_in_Area* on *Total_Civilian_Non_Institutional_Population_in_Area*")
    st.markdown("8. :blue[**Total_Employment_in_Area:**] number of people who have a job")
    st.markdown("9. :blue[**Percent_(%) of Labor Force Employed in State/Area:**] the ratio of *Total_Employment_in_Area* on *Total_Civilian_Labor_Force_in_Area*")
    st.markdown("10. :blue[**Total_Unemployment_in_Area:**] number of people who don't have a job")
    st.markdown("11. :blue[**Percent_(%)_of_Labor_Force_Unemployed_in_Area:**] the ratio of *Total_Unemployment_in_Area* on *Total_Civilian_Labor_Force_in_Area*")

if choice == 'Sub dataset - The US population':
    st.write("*This dataset contains data of the citizens total in 50 particular states in the US. It was lastest updated at the beginning of this year 2023, on January 11. Thus, illustrated in this database are the very upcoming statistics of the 50 states population, and we wondered whether we could display those figures into a more neat visualization. The outcome is the graph below.*")    
    st.write("**VARIABLES:**")
    st.markdown("1. :blue[**State:**] names of 51 states in the USA")
    st.markdown("2. :blue[**Population:**] the number of citizens in a state , report conducted in 2020")

if choice =='Sub dataset - The US GDP per capita per state':
    st.write("*All data collected in this dataset are from public databases, substantially government databases or government public investigations. GDP per capita data of 51 states in the US are particularly surveyed in 2020, during the severe outbreak of COVID-19 pandemic. Owing to this basis, the visualized graph is entirely a realistic image of the general financial statement of this country during the epidemic period.*")
    st.write("**VARIABLES:**")
    st.markdown("1. :blue[**State:**] names of 51 states in the USA")
    st.markdown("2. :blue[**GDP per capita:**] Gross Domestic Production in a state, report conducted in 2022")

colored_header(
    label="Dataset",
    description="Let's take a look at the dataset!",
    color_name="light-blue-70",)

if choice == 'Main dataset':
    load = pd.read_csv('Unemployment1.csv')

    load.rename (columns = {'Percent_(%)_of_Labor_Force_Unemployed_in_Area':'Unemployed percentage'}, inplace = True)
    load.rename (columns = {'Total_Unemployment_in_Area':'Total unemployers'}, inplace = True)
    load.rename (columns = {'Percent_(%) of Labor Force Employed in State/Area':'Employed percentage'}, inplace = True)
    load.rename (columns = {'Total_Employment_in_Area':'Total employers'}, inplace = True)
    load.rename (columns = {'Percent_(%)_of_Areas_Population':'Labor force percentage'}, inplace = True)
    load.rename (columns = {'Total_Civilian_Labor_Force_in_Area':'Total labor force'}, inplace = True)
    load.rename (columns = {'Total_Civilian_Non_Institutional_Population_in_Area':'Population'}, inplace = True)

    st.sidebar.header("Filter:")

    Area_select = st.sidebar.multiselect("Select the area:",options=load["Area"].unique(),default=None)
    Year_select = st.sidebar.multiselect("Select the year:",options=load["Year"].unique(),default=None)
    Month_select = st.sidebar.multiselect("Select the month:",options=load["Month"].unique(),default=None)

    load_selection = load.query("Area == @Area_select & Year == @Year_select & Month == @Month_select")

    st.dataframe(load_selection)

if choice =='Sub dataset - The US GDP per capita per state':
    load1 = pd.read_csv('States-Behavior-And-More-MainSheet.csv')
    
    load1.rename(columns = {'GDP.Per.Capita':'GDP per capita'}, inplace = True)
    load1.loc[:,['State','GDP per capita']]
                        

if choice == 'Sub dataset - The US population':
    load2 = pd.read_csv('USA-Covid-Data.csv')
    st.dataframe(load2)