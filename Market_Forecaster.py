import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | AI Market Forecaster",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Royal Blue & Clean White Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .forecast-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.88) 0%, rgba(30, 58, 138, 0.90) 50%, rgba(37, 99, 235, 0.85) 100%), 
                    url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        padding: 50px 30px;
        border-radius: 26px;
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 12px 30px rgba(37, 99, 235, 0.22);
    }
    
    .hero-title-text {
        font-size: 42px;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(90deg, #ffffff 0%, #93c5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-sub-text {
        font-size: 18px;
        color: #e0f2fe;
        margin-top: 10px;
        opacity: 0.95;
    }

    .prop-card-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
    }

    .prop-img-wrapper {
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 15px;
        border: 2px solid #e0f2fe;
        height: 250px;
    }

    .prop-img-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .stat-badge {
        background: #f0f9ff;
        border: 1px solid #bae6fd;
        padding: 12px 18px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 12px;
    }

    .stat-badge-val {
        font-size: 24px;
        font-weight: 900;
        color: #1d4ed8;
    }

    .stat-badge-lbl {
        font-size: 12px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load Data & Attach Photos
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/houses.csv")
    except:
        df = pd.DataFrame({
            'id': [101, 102, 103, 104],
            'city': ['Beirut', 'Jounieh', 'Beirut', 'Byblos'],
            'price': [220000, 185000, 310000, 150000],
            'area': [160, 140, 210, 120],
            'bedrooms': [3, 2, 4, 2],
            'bathrooms': [2, 2, 3, 2],
            'distance_to_center_km': [2.0, 12.0, 1.5, 25.0],
            'building_age': [4, 8, 2, 12]
        })
    
    if 'id' not in df.columns:
        df['id'] = df.index + 101
        
    photos = [
        "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80"
    ]
    
    if 'image_url' not in df.columns:
        df['image_url'] = [photos[i % len(photos)] for i in range(len(df))]
        
    return df

df = load_data()

# 4. Hero Banner
st.markdown("""
    <div class="forecast-hero">
        <h1 class="hero-title-text">🔮 5-Year AI Price Trend Forecaster</h1>
        <p class="hero-sub-text">Predict future market appreciation and asset trajectory over the next 5 years</p>
    </div>
""", unsafe_allow_html=True)

# 5. Property & Forecast Inputs
col_left, col_right = st.columns([1.1, 1.9])

options = [f"Property #{row['id']} | {row['city']} | ${row['price']:,.0f}" for _, row in df.iterrows()]

with col_left:
    st.markdown('<div class="prop-card-box">', unsafe_allow_html=True)
    selected_idx = st.selectbox("Select Property for AI Simulation 🏢", range(len(options)), format_func=lambda x: options[x], index=0)
    selected_prop = df.iloc[selected_idx]
    
    st.markdown(f"""
        <div class="prop-img-wrapper" style="margin-top: 15px;">
            <img src="{selected_prop['image_url']}" alt="Property Photo">
        </div>
        <h3 style="color:#0f172a; margin:0 0 5px 0; font-weight:800;">{selected_prop['city']} Property #{selected_prop['id']}</h3>
        <p style="color:#2563eb; font-size:22px; font-weight:900; margin-bottom:15px;">${selected_prop['price']:,.0f}</p>
    """, unsafe_allow_html=True)
    
    st.markdown("##### ⚙️ Economic Growth Parameters")
    annual_growth = st.slider("Expected Market Growth (% / Year)", min_value=1.0, max_value=12.0, value=5.0, step=0.5)
    inflation = st.slider("Estimated Inflation Rate (%)", min_value=0.5, max_value=8.0, value=2.5, step=0.5)
    
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Calculations & Charts
net_annual_appreciation = annual_growth - (inflation * 0.3)
years = np.array([0, 1, 2, 3, 4, 5])

# Monte Carlo / Scenario Projections
base_price = selected_prop['price']
baseline_projection = base_price * ((1 + (net_annual_appreciation / 100)) ** years)
optimistic_projection = base_price * ((1 + ((net_annual_appreciation + 2.5) / 100)) ** years)
pessimistic_projection = base_price * ((1 + (max(0.5, net_annual_appreciation - 2.0) / 100)) ** years)

with col_right:
    # Summary Stat Badges
    b1, b2, b3 = st.columns(3)
    
    with b1:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-badge-lbl">Current Price</div>
                <div class="stat-badge-val">${base_price:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with b2:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-badge-lbl">5-Year Projected Price</div>
                <div class="stat-badge-val" style="color:#16a34a;">${baseline_projection[-1]:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with b3:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-badge-lbl">Expected Equity Gain</div>
                <div class="stat-badge-val" style="color:#0284c7;">+${baseline_projection[-1] - base_price:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)

    # Line Chart with Scenarios
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[f"Year {y}" for y in years], y=optimistic_projection,
        mode='lines+markers', name='Bull Market Scenario (+2.5%)',
        line=dict(color='#16a34a', width=3, dash='dot')
    ))

    fig.add_trace(go.Scatter(
        x=[f"Year {y}" for y in years], y=baseline_projection,
        mode='lines+markers', name='AI Baseline Forecast',
        line=dict(color='#1d4ed8', width=4)
    ))

    fig.add_trace(go.Scatter(
        x=[f"Year {y}" for y in years], y=pessimistic_projection,
        mode='lines+markers', name='Conservative Scenario',
        line=dict(color='#dc2626', width=2, dash='dash')
    ))

    fig.update_layout(
        title="5-Year Property Value Trajectory ($)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#0f172a",
        height=380,
        margin=dict(l=0, r=0, t=40, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Year-by-Year Table
    st.markdown("##### 📅 Year-by-Year Projected Values")
    df_yearly = pd.DataFrame({
        'Timeline': [f"Year {y}" for y in years],
        'Conservative ($)': [f"${val:,.0f}" for val in pessimistic_projection],
        'AI Baseline ($)': [f"${val:,.0f}" for val in baseline_projection],
        'Bull Market ($)': [f"${val:,.0f}" for val in optimistic_projection]
    })
    st.dataframe(df_yearly, use_container_width=True, hide_index=True)