import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Market Analytics | SmartEstate AI", page_icon="📈", layout="wide")

# 2. Ultra-Modern Blue Theme & White Background
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .market-banner {
        background: linear-gradient(135deg, #0284c7 0%, #1d4ed8 50%, #1e3a8a 100%);
        padding: 35px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(29, 78, 216, 0.2);
        margin-bottom: 30px;
    }
    
    .blue-stat-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border: 2px solid #bae6fd;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.05);
        transition: transform 0.3s ease;
    }
    .blue-stat-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
    }
    
    .stat-title {
        font-size: 14px;
        color: #0369a1;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stat-value {
        font-size: 28px;
        font-weight: 800;
        color: #1e3a8a;
        margin: 8px 0;
    }
    
    .blue-badge {
        background-color: #dbeafe;
        color: #1d4ed8;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Market Header
st.markdown("""
    <div class="market-banner">
        <h1 style="margin:0; font-weight:800; font-size:36px;">📈 Real Estate Market Intelligence</h1>
        <p style="font-size: 17px; opacity: 0.95; margin-top: 8px;">Explore price distributions, city benchmarks, and 5-year growth forecasts</p>
    </div>
""", unsafe_allow_html=True)

df = pd.read_csv("data/houses.csv")

# 4. Top Key Performance Metrics (KPI Cards)
c1, c2, c3, c4 = st.columns(4)

avg_price = df['price'].mean()
max_price = df['price'].max()
total_listings = len(df)
top_city = df.groupby('city')['price'].mean().idxmax()

with c1:
    st.markdown(f"""
        <div class="blue-stat-card">
            <div class="stat-title">Average Market Price</div>
            <div class="stat-value">${avg_price:,.0f}</div>
            <span class="blue-badge">National Avg</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="blue-stat-card">
            <div class="stat-title">Peak Valuation</div>
            <div class="stat-value">${max_price:,.0f}</div>
            <span class="blue-badge">Luxury Segment</span>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="blue-stat-card">
            <div class="stat-title">Active Index Listings</div>
            <div class="stat-value">{total_listings}</div>
            <span class="blue-badge">Properties Tracked</span>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="blue-stat-card">
            <div class="stat-title">Highest Value Region</div>
            <div class="stat-value">{top_city}</div>
            <span class="blue-badge">Prime Investment</span>
        </div>
    """, unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# 5. Visual Interactive Analytics Grid
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("📊 Average Price by City ($)")
    city_avg = df.groupby('city')['price'].mean().reset_index()
    fig1 = px.bar(
        city_avg, x='city', y='price', color='price',
        color_continuous_scale=['#93c5fd', '#2563eb', '#1e3a8a'],
        labels={'city': 'City / Region', 'price': 'Average Price ($)'},
        text_auto='.2s'
    )
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font_color="#0f172a",
        coloraxis_showscale=False,
        height=380
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_chart2:
    st.subheader("🔵 Property Area vs Price Correlation")
    fig2 = px.scatter(
        df, x='area', y='price', color='city', size='bedrooms',
        hover_data=['bathrooms'],
        color_discrete_sequence=['#1d4ed8', '#0284c7', '#3b82f6', '#60a5fa', '#1e40af', '#93c5fd'],
        labels={'area': 'Area (m²)', 'price': 'Price ($)'}
    )
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font_color="#0f172a",
        height=380
    )
    st.plotly_chart(fig2, use_container_width=True)

st.write("---")

# 6. Future Trend Projection Section
st.subheader("🚀 5-Year Regional Growth Forecast Matrix")
st.write("Estimated appreciation trends based on historic market momentum and location demand:")

forecast_data = []
years = ['2024', '2025', '2026', '2027', '2028']
base_cities = df['city'].unique()

for c in base_cities:
    base_val = df[df['city'] == c]['price'].mean()
    growth_rate = 1.05 if c in ['Beirut', 'Metn', 'Jounieh'] else 1.035
    for i, yr in enumerate(years):
        val = base_val * (growth_rate ** i)
        forecast_data.append({'City': c, 'Year': yr, 'Projected Avg Price ($)': round(val)})

forecast_df = pd.DataFrame(forecast_data)

fig3 = px.line(
    forecast_df, x='Year', y='Projected Avg Price ($)', color='City',
    markers=True,
    color_discrete_sequence=['#1e3a8a', '#2563eb', '#0284c7', '#3b82f6', '#60a5fa', '#93c5fd']
)
fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    font_color="#0f172a",
    height=400
)
st.plotly_chart(fig3, use_container_width=True)