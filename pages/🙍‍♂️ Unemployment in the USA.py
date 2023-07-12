import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Unemployment in the USA",page_icon="🙍‍♂️",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Unemployment in the USA]')

colored_header(
    label="What is unemployment?",
    description="How to define if someone is unemployed",
    color_name="light-blue-70",)
annotated_text("Unemployment generally falls during periods of economic prosperity and rises during recessions, creating significant pressure on public finances as tax revenue falls and social safety net costs increase.",("Government spending and taxation decisions","fiscal policy","#9681EB")," and ",("U.S. Federal Reserve interest rate adjustments","monetary policy","#45CFDD"),"are important tools for managing the unemployment rate. There may be an economic trade-off between unemployment and inflation, as policies designed to reduce unemployment can create inflationary pressure, and vice versa. ",("The U.S. Federal Reserve","the Fed","#6527BE")," has a dual mandate to achieve full employment while maintaining a low rate of inflation. The major political parties debate appropriate solutions for improving the job creation rate, with liberals arguing for more government spending and conservatives arguing for lower taxes and less regulation. Polls indicate that Americans believe job creation is the most important government priority, with not sending jobs overseas the primary solution.")
st.write("*Unemployment can be measured in several ways. A person is defined as unemployed in the United States if they are jobless, but have looked for work in the last four weeks and are available for work. People who are neither employed nor defined as unemployed are not included in the labor force calculation.*")

st.markdown("---")

load = pd.read_csv('Unemployment1.csv')

load.rename (columns = {'Percent_(%)_of_Labor_Force_Unemployed_in_Area':'Unemployed percentage'}, inplace = True)
load.rename (columns = {'Total_Unemployment_in_Area':'Total unemployers'}, inplace = True)
load.rename (columns = {'Percent_(%) of Labor Force Employed in State/Area':'Employed percentage'}, inplace = True)
load.rename (columns = {'Total_Employment_in_Area':'Total employers'}, inplace = True)
load.rename (columns = {'Percent_(%)_of_Areas_Population':'Labor force percentage'}, inplace = True)
load.rename (columns = {'Total_Civilian_Labor_Force_in_Area':'Total labor force'}, inplace = True)
load.rename (columns = {'Total_Civilian_Non_Institutional_Population_in_Area':'Population'}, inplace = True)
st.subheader("Unemployed percentage fluctuation from 2013-2022 in top 5 states with the highest GDP in the USA")

subcl= load[(load["Month"]==12)]
subcl1= subcl[(subcl["Area"]=='California')]
subcl2= subcl1[(subcl1["Year"] > 2012)]
finalcl = subcl2.loc[:,['Unemployed percentage','Year']]

subtx= load[(load["Month"]==12)]
subtx1= subtx[(subtx["Area"]=='Texas')]
subtx2= subtx1[(subtx1["Year"] > 2012)]
finaltx = subtx2.loc[:,['Unemployed percentage','Year']]

subny= load[(load["Month"]==12)]
subny1= subny[(subny["Area"]=='New York')]
subny2= subny1[(subny1["Year"] > 2012)]
finalny = subny2.loc[:,['Unemployed percentage','Year']]

subfl= load[(load["Month"]==12)]
subfl1= subfl[(subfl["Area"]=='Florida')]
subfl2= subfl1[(subfl1["Year"] > 2012)]
finalfl = subfl2.loc[:,['Unemployed percentage','Year']]

subil= load[(load["Month"]==12)]
subil1= subil[(subil["Area"]=='Illinois')]
subil2= subil1[(subil1["Year"] > 2012)]
finalil = subil2.loc[:,['Unemployed percentage','Year']]

option = st.selectbox(
'Please select state:',
('California', 'Florida', 'Texas','New York','Illinois'))
st.caption(f"You selected: {option}")

left_column, right_column = st.columns((1,2))
with right_column:

    if option=='California':
        cali = px.line(finalcl, x='Year', y='Unemployed percentage',markers=False)
        cali.update_layout(title=f"Unemployed percentage fluctuation from 2013-2022 in {option}",
                   xaxis_title='Year',
                   yaxis_title='Unemployed percentage')
        st.plotly_chart(cali)

    if option=='Florida':
         flor = px.line(finalfl, x='Year', y='Unemployed percentage',markers=False)
         flor.update_layout(title=f"Unemployed percentage fluctuation from 2013-2022 in {option}",
                   xaxis_title='Year',
                   yaxis_title='Unemployed percentage')
         st.plotly_chart(flor)

    if option=='New York':
        new = px.line(finalny, x='Year', y='Unemployed percentage',markers=False)
        new.update_layout(title=f"Unemployed percentage fluctuation from 2013-2022 in {option}",
                   xaxis_title='Year',
                   yaxis_title='Unemployed percentage')
        st.plotly_chart(new)

    if option=='Texas':
        tex = px.line(finalfl, x='Year', y='Unemployed percentage',markers=False)
        tex.update_layout(title=f"Unemployed percentage fluctuation from 2013-2022 in {option}",
                   xaxis_title='Year',
                   yaxis_title='Unemployed percentage')
        st.plotly_chart(tex)

    if option=='Illinois':
        illi = px.line(finalil, x='Year', y='Unemployed percentage',markers=False)
        illi.update_layout(title=f"Unemployed percentage fluctuation from 2013-2022 in {option}",
                   xaxis_title='Year',
                   yaxis_title='Unemployed percentage')
        st.plotly_chart(illi)

with left_column:
    if option=='California':
        st.write("From 2013 - 2022, the unemployment rate in California has undergone some clear fluctuations. The rate of unemployment reached its highest peak in 2020 with the rate of 9.1% due to the impact of Covid-19 pandemic. In 2022, the unemployment rate decreased to 4.1% - the lowest rate within the past 10 years. The unemployment rate started at the rate of 8.4 percent in 2013 and steadily went down until 2019 when it reached the rate of 4.2%. However, it has sharply increased in 2020 to the rate of 9.1 percent - a 4.9 percent difference compared to the previous year.")
    if option=='Florida':
        st.write("From 2013 - 2022, the unemployment rate in Florida has undergone some significant changes but in general the trend is going down. However, it still remains as a state with a fairly low unemployment rate. In 2013, the unemployment rate in Florida was 7 percent and slowly went down until 2019 when it reached 3 percent. However, in 2020 the unemployment rate reached its peak of 6.4 percent as a result of the Covid-19 pandemic and the follow-up layoff trend. Nonetheless, in 2022, Florida has successfully managed to bring the unemployment rate down to 2.7 percent - the lowest point within the past 10 years.")
    if option=='Texas':
        st.write("Compared to other states within the top 5 states with the highest GDP in the USA, Texas is the state with the most noticeable fluctuations although the rate is not high most of the time. Texas had an unemployment rate of 5.8 percent in 2013 and underwent some up and down with a small peak of 4.2 percent in 2016 then continued to go down until it reached the lowest point in 2019 at 3.5 percent. However, in 2019 the unemployment rate went up again to 6.9 percent as a result of the Covid-19 pandemic in the USA and in the world. As the pandemic went away, Texas has managed to bring its economy back and lowered the unemployment rate to 3.8 percent in 2022.")
    if option=='New York':
        st.write("New York observed the same fluctuation pattern as other states with the top 5. The starting point in 2013 had an unemployment rate of 7.1 percent - a decent number compared to other states. The rate then went down steadily until 2019 when it reached 4 percent. With the impact of the Covid-19 pandemic in the world, in 2020 the unemployment rate reached a peak of 8.7 percent. However, the fast recovery of the economy has helped the unemployment rate to go down to the point of 4.1 percent in 2022.")
    if option=='Illinois':
        st.write("Illinois started in 2013 with a fairly high unemployment rate - 8.6 percent. However, the rate steadily went down to 3.6 percent in 2019. In 2020, the unemployment rate went up to 7.6 percent due to the Covid-19 pandemic and its impact on the economy. As the economy is recovering when the pandemic has gone away, the unemployment rate also went down in 2022 and reached 4.6 percent.")

st.markdown("---")

data = pd.read_csv('Unemployment.csv')

years = [1976, 1987, 1998, 2009, 2020]
st.subheader("Employed labor force percentage in the USA in noticeable years")
st.write("*This demonstrated visualization displays a general illustration of residents successfully pursuing occupations in 53 states of the US within a 44-year-period. Specifically, the 5 particular years selected are 1976, 1987, 1998, 2009, 2020, with the latter one successively being 11-unit-year more than the former. Throughout the recorded time, it’s unchallenging to make out that employed Americans’ percentage were gradually rising, with approximately 50%-60% in 1976 and ultimately climbing to 60%-70% in 2020. This proved an undeniable fact that the employment status of this nation was improving consistently, perhaps on account of suitable government policies in the progress of developing the US economy.*")
selected_year = st.selectbox("Seletct year", years)
st.caption(f"You selected: {selected_year}")
if selected_year:
    filterd_data = data[data['Year'] == selected_year]
    chart= px.bar(filterd_data,x= filterd_data['Area'],
                  y= filterd_data['Percent_(%) of Labor Force Employed in State/Area'])
    chart.update_layout(title=f"Employed labor force percentage in the USA in {selected_year}",
                        xaxis_title="States", yaxis_title="Employed labor force percentage",xaxis_tickangle=-45)
    chart.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0, opacity=0.6)
    st.plotly_chart(chart)

st.markdown("---")

st.subheader(':blue[Total Civilian Labor Force in 5 most Populous States in the US from 2000 to 2022]')
st.write("*The graph demonstrates the total civilian labor force in five most populous states in the US from 2000 to 2022. Through these numbers, readers could acknowledge the number of people who are employed and who are actively looking for jobs, showing the US population and labor force since 2000 through representatives like New York, California, Washington, Virginia, and Pennsylvania. We believe that this graph could give you a glimpse into the number of people available to work during the researched period so that you could compare and better prepare yourself.*")

df = pd.read_csv('Unemploymentquyen.csv')
Area_chosen = "California", "New York", "Pennsylvania", "Virginia", "Washington"

selected_state = st.selectbox("Please select a state:",Area_chosen)
st.caption(f"You select {selected_state}")
c1,c2 = st.columns((1,2))
with c2:
    if selected_state:
        bar_data = df[df['Area'] == selected_state]
        bar_data1 = bar_data[bar_data['Month'] == 1]
        bar_data2 = bar_data1[bar_data1['Year'] > 1999]
        bar_data3 = bar_data2.loc[:,['Year','Total_Civilian_Labor_Force_in_Area']]
        bar_data3['Total_Civilian_Labor_Force_in_Area'] = bar_data3['Total_Civilian_Labor_Force_in_Area'].div(10**7)
        fig = px.line(bar_data3, x='Year', y='Total_Civilian_Labor_Force_in_Area',markers=True)
        fig.update_layout(title=f"Total Civilian Labor Force in {selected_state} from 2000 to 2022",
                   xaxis_title='Year',
                   yaxis_title='Total Civilian Labor Force (10e7) - million')
        st.plotly_chart(fig)

with c1:
    if selected_state:
        bar_data = df[df['Area'] == selected_state]
        bar_data1 = bar_data[bar_data['Month'] == 1]
        bar_data2 = bar_data1[bar_data1['Year'] > 1999]
        bar_data3 = bar_data2.loc[:,['Year','Total_Civilian_Labor_Force_in_Area']]
        bar_data3.rename (columns = {'Total_Civilian_Labor_Force_in_Area':'Total Civilian Labor Force'}, inplace = True)
        df3 = st.dataframe(bar_data3,use_container_width= True,hide_index=True,column_config={"Year": st.column_config.TextColumn("Year")})
