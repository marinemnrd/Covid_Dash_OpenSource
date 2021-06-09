import streamlit as st
import pandas as pd
# from plotly import plotly
import plotly.express as px
import numpy as np
#import datetime
import time
#import datetime
from datetime import datetime


#Titles and Mode selections
st.sidebar.title("Menu")
st.sidebar.radio("Navigate", ["Home", "Data", "Dashboard", "About"])
selectbox = st.sidebar.selectbox('Type',('death','case'))
st.sidebar.title("About")
st.sidebar.info(
    """
    Thus app is maintained by Team 6, Paul, Marine and Elizabeth.
    """
)
st.sidebar.title("Comment")
st.sidebar.info("Feel free to comment on our work. The github link can be found "
                "[here](https://github.com/marinemnrd/Covid_Dash_OpenSource)")


st.title("COVID DASHBOARD")
st.write("""
This web application will serve to analyze and visualize the spread of COVID-19""")
st.markdown("## Symptoms")
st.markdown(("* Fever or chills\n* Cough\n"
             "* Shortness of breath or difficulty breathing\n"
             "* Fatigue\n"
             "* Muscle or body aches\n"
             "* Headache\n"
             "* Loss of taste or smell\n"
             "* Sore throat\n"
             "* Congestion or runny nose\n"
             "* Nausea or vomiting\n"
             "* Diarrhea"))


st.image('monalisa.jpeg')

#Load Data
df_case = pd.read_csv(r'https://raw.githubusercontent.com/marinemnrd/Covid_Dash_OpenSource/main/Datas/Clean_Confirmed_Case.csv', parse_dates=['Date'])
df_case = df_case.set_index(['Date'])
df_Death = pd.read_csv(r'https://raw.githubusercontent.com/marinemnrd/Covid_Dash_OpenSource/main/Datas/Clean_Death.csv', parse_dates=['Date'])
df_Death = df_Death.set_index(['Date'])


#Chart the Datas
defaultcol = df_case['France']


if selectbox == 'case':
    st.title("Cumulative number of cases")
    min_ts = min(df_case.index).to_pydatetime()
    max_ts = max(df_case.index).to_pydatetime()

    # slider to chose date
    st.sidebar.subheader("Inputs")
    min_selection, max_selection = st.sidebar.slider("Timeline", min_value=min_ts, max_value=max_ts,
                                                     value=[min_ts, max_ts])
    df_case = df_case[(df_case.index >= min_selection) & (df_case.index <= max_selection)]
    case = st.multiselect('choose country', df_case.columns)



    print(case)

    #fig = px.line(df_case, x=df_case.index, y=case)
    fig = px.line(df_case, x=df_case.index, y=case)

    st.write(fig)
else:
    st.title("Cumulative number of deaths")
    min_ts = min(df_Death.index).to_pydatetime()
    max_ts = max(df_Death.index).to_pydatetime()
    # slider to chose date
    st.sidebar.subheader("Inputs")
    min_selection, max_selection = st.sidebar.slider("Timeline", min_value=min_ts, max_value=max_ts,
                                                     value=[min_ts, max_ts])
    df_Death = df_Death[(df_Death.index >= min_selection) & (df_Death.index <= max_selection)]
    death = st.multiselect('choose country', df_Death.columns)

    print(death)

    fig = px.line(df_Death, x=df_Death.index, y=death)
    st.write(fig)
