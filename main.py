import pandas as pd
import streamlit as st
import pandas as pd
# from plotly import plotly
import plotly.express as px
import numpy as np
import datetime
import time

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