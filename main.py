import pandas as pd
import streamlit as st
import pandas as pd
# from plotly import plotly
import plotly.express as px
import numpy as np
import datetime
import time

df_case = pd.read_csv(r'C:\Users\CRI User\Documents\GitHub\Covid_Dash_OpenSource\Datas\Clean_Case.csv',header=1)
st.title("OUR FIRST DASHBOARD HEHE")

st.checkbox('first checkbox')
print(df_case)


case = st.selectbox('choose country',df_case['Date'])

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df_case, x=df.columns, y=case)
st.write(fig)