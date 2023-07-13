import streamlit as st 
import plotly.express as px
import pandas as pd
from streamlit_extras.stoggle import stoggle

st.set_page_config(page_title="Explore our code 😉",page_icon="😉",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Explore our code 😉]')
st.write("*Are you interested in how we brought this application to life? Let's take a look at our code right down there!*")
st.markdown("---")

option = st.selectbox(
    'Which page would you like to learn more about?',
    ('Homepage', '👋 The USA and things you should know', '🙍‍♂️ Unemployment in the USA','📖 Learn about our dataset'))

st.caption(f"You selected: {option}")

if option == 'Homepage':
    code = '''import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
import streamlit as st
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🧡", layout="wide")
st.subheader("Group 2.1")
st.title("PYTHON 2 - BUSINESS IT 2 :orange_heart:")
st.write("We are a group of business students who are interested in the economical situation in the world. Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades.")

stoggle(
    "Group information",
    """
    \n 1. Dinh Ha Tu Van - 10622045
    \n 2. Bui Cam Ha Quyen - 10622023
    \n 3. Mai Hong Hanh - 10622014""",
)

st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link&ouid=114022649098492793407&rtpof=true&sd=true)")

rain(
    emoji="🔍",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

colored_header(
    label="Group members introduction",
    description="Get to know about our group",
    color_name="light-blue-70",)

tv1, tv2 = st.columns(2)
with tv1:
    tuvan = Image.open('3.png')
    st.image(tuvan)
with tv2:
    st.subheader("**Full name: Dinh Ha Tu Van (Group leader)**")
    st.write("Student ID: 10622045")
    st.write("Email: 10622045@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 077 6209215")

st.write(" ")

hq1, hq2 = st.columns(2)
with hq1:
    haquyen = Image.open('2.png')
    st.image(haquyen)
with hq2:
    st.subheader("**Full name: Bui Cam Ha Quyen**")
    st.write("Student ID: 10622023")
    st.write("Email: 10622023@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")
    st.write("Phone number: 090 8784370")

st.write(" ")

mh1, mh2 = st.columns(2)
with mh1:
    maihanh = Image.open('1.png')
    st.image(maihanh)
with mh2:
    st.subheader("**Full name: Mai Hong Hanh**")
    st.write("Student ID: 10622014")
    st.write("Email: 10622014@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("039 2230636")

st.markdown("---")

st.subheader("💬 Leave us your message!")

st.caption("Let us know if you have any recommendations")

contactform = """<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email address" required>
     <textarea name="message" placeholder="What do you think?"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(contactform,unsafe_allow_html=True)

def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)
local_css("style.css")'''
    st.code(code, language='python')

if option == '👋 The USA and things you should know':
    code2 = '''import streamlit as st 
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
    annotated_text(("United States","🇺🇸","#8CC0DE"),", officially United States of America, abbreviated U.S. or U.S.A., byname America, country in North America, a federal republic of 50 states. Besides the 48 conterminous states that occupy the middle latitudes of the continent, the United States includes the state of Alaska, at the northwestern extreme of North America, and the island state of Hawaii, in the mid-Pacific Ocean. The conterminous states are bounded on the north by Canada, on the east by the Atlantic Ocean, on the south by the Gulf of Mexico and Mexico, and on the west by the Pacific Ocean. The United States is the fourth largest country in the world in area (after Russia, Canada, and China).",("The national capital is Washington","📍","#8CC0DE"),", which is coextensive with the District of Columbia, the federal capital region created in 1790.")

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
'''
    st.code(code2, language='python')

if option == '🙍‍♂️ Unemployment in the USA':
    code3 = '''import streamlit as st 
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
'''
    st.code(code3, language='python')

if option == '📖 Learn about our dataset':
    code4 = '''import streamlit as st 
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
    st.dataframe(load2)'''
    st.code(code4, language='python')