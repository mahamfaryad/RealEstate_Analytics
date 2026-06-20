import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Setup
st.set_page_config(page_title="Real Estate Analytics", layout="wide")
st.title("🏠 Real Estate Market Insights & Price Predictor")
st.markdown("Interactive property valuation data model and regional price trends.")

# Synthetic Real Estate Data Generator
@st.cache_data
def load_housing_data():
    np.random.seed(10)
    locations = ['Gulberg', 'DHA Phase 6', 'Johar Town', 'Samundri Road', 'Canal Road']
    data = {
        'Property_ID': [f"PRP-{i:04d}" for i in range(501, 801)],
        'Location': np.random.choice(locations, size=300),
        'Area_SqFt': np.random.randint(800, 4500, size=300),
        'Bedrooms': np.random.randint(1, 6, size=300),
        'Price_PKR_Lakhs': np.random.randint(40, 650, size=300),
        'Property_Type': np.random.choice(['House', 'Apartment', 'Plot'], size=300, p=[0.6, 0.3, 0.1])
    }
    return pd.DataFrame(data)

df_house = load_housing_data()

# Layout split into interactive Predictor and Analytics
col_input, col_chart = st.columns([1, 2])

with col_input:
    st.subheader("💡 Smart Price Calculator")
    loc = st.selectbox("Select Location", df_house['Location'].unique())
    size = st.slider("Select Area (SqFt)", 800, 4500, 1800)
    beds = st.number_input("Number of Bedrooms", min_value=1, max_value=6, value=3)
    
    # Simple Analytical Prediction Logic
    base_price = df_house[df_house['Location'] == loc]['Price_PKR_Lakhs'].mean()
    predicted_price = base_price * (size / 2000) * (beds / 3)
    
    st.success(f"Estimated Market Value: **{predicted_price:.2f} Lakhs PKR**")

with col_chart:
    st.subheader("📈 Regional Price Distribution")
    fig_box = px.box(df_house, x='Location', y='Price_PKR_Lakhs', color='Property_Type',
                     title="Property Pricing Range by Location & Type",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_box, use_container_width=True)

# Secondary Insight Chart
st.markdown("---")
st.subheader("📊 Property Size vs Pricing Correlation")
fig_trend = px.scatter(df_house, x='Area_SqFt', y='Price_PKR_Lakhs', color='Location',
                       size='Bedrooms', hover_data=['Property_Type'])
st.plotly_chart(fig_trend, use_container_width=True)