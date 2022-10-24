from statistics import median_grouped
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')
st.title("California housing data(1990) by JingyangFeng")
df = pd.read_csv('housing.csv')

house_filter = st.sidebar.multiselect(
     'choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique()) 


income_filter = st.sidebar.radio('Choose income level',('Low', 'Medium', 'High'))
df = df[df.ocean_proximity.isin(house_filter)]
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income < 4.5) & (df.median_income > 2.5)]
else:
    df = df[df.median_income > 4.5]

pop_filter = st.slider('median house price',0,500001,100000)
df = df[df.median_house_value <= pop_filter]

st.subheader('See more filter in the sidebar')
st.map(df)

st.subheader('histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(40,20))
median_house_value=df.median_house_value
df.median_house_value.hist(bins=30)



st.pyplot(fig)

