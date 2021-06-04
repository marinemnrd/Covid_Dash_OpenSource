import streamlit as st
import pandas as pd
# from plotly import plotly
import plotly.express as px
import numpy as np
import datetime
import time

st.sidebar.title("Menu")
st.sidebar.radio("Navigate", ["Home", "Data", "Dashboard", "About"])
st.sidebar.title("About")
st.sidebar.info(
    """
    Thus app is maintained by Team 6, Paul, Marine and Elizabeth.
    """
)
st.sidebar.title("Comment")
st.sidebar.info("Feel free to comment on our work. The github link can be found "
                "[here](https://github.com/marinemnrd/Covid_Dash_OpenSource)")


st.title("OUR FIRST DASHBOARD HEHE")
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

df_case = pd.read_csv(r'C:\Users\CRI User\Documents\GitHub\Covid_Dash_OpenSource\Datas\Clean_Case.csv',header=1)
df_case = df_case.T
df_case.columns = df_case.iloc[1]
df_case= df_case.reset_index()
df_case=df_case.drop([0,1])
df_case=df_case.rename(columns={"index": "Date"})
st.title("OUR FIRST DASHBOARD HEHE")

st.checkbox('first checkbox')
print(df_case)


case = st.selectbox('choose country',df_case.columns)

print(case)

fig = px.line(df_case, x=df_case['Date'], y=case)
st.write(fig)
#Checking that everything works 
