import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./vehicles_us.csv')  # Adjust path if necessary

# Header
st.header("Car Advertisement Data Dashboard")

# Histogram of car prices
st.subheader("Distribution of Car Prices")
fig = px.histogram(df, x='price', nbins=30, title="Distribution of Car Prices")
st.plotly_chart(fig)

# Scatter plot of price vs. odometer (mileage)
st.subheader("Price vs. Odometer (Mileage)")
fig = px.scatter(df, x='odometer', y='price', title="Price vs. Odometer of Cars")
st.plotly_chart(fig)

# Checkbox to toggle additional details
if st.checkbox("Show Price vs. Model Year Scatterplot"):
    fig = px.scatter(df, x='model_year', y='price', title="Price vs. Model Year of Car")
    st.plotly_chart(fig)
