import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Compare Properties",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .compare-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 58, 138, 0.88) 50%, rgba(37, 99, 235, 0.82) 100%), 
                    url('https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1600&q=80');
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

    .prop-card {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
        text-align: center;
    }

    .prop-header-blue {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%);
        color: white;
        padding: 12px;
        border-radius: 14px;
        font-weight: 800;
        font-size: 17px;
        margin-bottom: 15px;
    }

    .prop-img-container {
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 15px;
        border: 2px solid #e0f2fe;
        height: 220px;
    }

    .prop-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .stat-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px solid #f1f5f9;
        font-size: 14.5px;
    }

    .stat-label {
        color: #64748b;
        font-weight: 600;
    }

    .stat-value {
        color: #0f172a;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load Data & Attach Default Images
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
    
    # قائمة صور معمارية وفخمة للعقارات
    default_images = [
        "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80"
    ]
    
    if 'image_url' not in df.columns:
        df['image_url'] = [default_images[i % len(default_images)] for i in range(len(df))]
        
    df['price_per_m2'] = df['price'] / df['area']
    df['score'] = ((df['area'] / (df['distance_to_center_km'] + 1)) * 1.5 - (df['building_age'] * 0.8)).clip(10, 99).round(1)
    
    return df

df = load_data()

# 4. Hero Banner
st.markdown("""
    <div class="compare-hero">
        <h1 class="hero-title-text">⚖️ Side-by-Side Property Comparison</h1>
        <p class="hero-sub-text">Benchmark two properties head-to-head on specs, pricing, and visual aesthetics</p>
    </div>
""", unsafe_allow_html=True)

# 5. Property Selectors
col_sel1, col_sel2 = st.columns(2)

options = [f"ID: {row['id']} | {row['city']} | ${row['price']:,.0f} | {row['area']}m²" for _, row in df.iterrows()]

with col_sel1:
    idx1 = st.selectbox("Select Property A 🏠", range(len(options)), format_func=lambda x: options[x], index=0)

with col_sel2:
    idx2 = st.selectbox("Select Property B 🏢", range(len(options)), format_func=lambda x: options[x], index=min(1, len(options)-1))

propA = df.iloc[idx1]
propB = df.iloc[idx2]

st.write("---")

# 6. Side-by-Side Cards with Images
c1, c2 = st.columns(2)

def render_prop_card(prop, label):
    st.markdown(f"""
        <div class="prop-card">
            <div class="prop-header-blue">{label}: Property #{prop['id']} ({prop['city']})</div>
            <div class="prop-img-container">
                <img src="{prop['image_url']}" alt="Property Image">
            </div>
            <h2 style="color:#1d4ed8; margin: 0 0 15px 0; font-weight:900;">${prop['price']:,.0f}</h2>
            <div class="stat-row">
                <span class="stat-label">Area (m²)</span>
                <span class="stat-value">{prop['area']} m²</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Price / m²</span>
                <span class="stat-value">${prop['price_per_m2']:,.0f} / m²</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Bedrooms / Bathrooms</span>
                <span class="stat-value">{prop['bedrooms']} Beds / {prop['bathrooms']} Baths</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Distance to Center</span>
                <span class="stat-value">{prop['distance_to_center_km']} km</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Building Age</span>
                <span class="stat-value">{prop['building_age']} Years</span>
            </div>
            <div class="stat-row" style="border-bottom:none; margin-top:10px;">
                <span class="stat-label" style="color:#0284c7;">Investment Score</span>
                <span class="stat-value" style="color:#1d4ed8; font-size:18px;">{prop['score']} / 100</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c1:
    render_prop_card(propA, "Property A")

with c2:
    render_prop_card(propB, "Property B")

st.write(" ")

# 7. Radar Comparison Chart
st.subheader("📊 Multi-Attribute Benchmark Radar")

categories = ['Price Efficiency', 'Property Area', 'Value / m²', 'Proximity to Center', 'Building Youth']

max_price = df['price'].max()
max_area = df['area'].max()
max_dist = df['distance_to_center_km'].max()
max_age = max(df['building_age'].max(), 1)

valsA = [
    (1 - propA['price']/max_price)*100,
    (propA['area']/max_area)*100,
    (1 - propA['price_per_m2']/(max_price/100))*100 if max_price>0 else 50,
    (1 - propA['distance_to_center_km']/max_dist)*100 if max_dist>0 else 50,
    (1 - propA['building_age']/max_age)*100
]

valsB = [
    (1 - propB['price']/max_price)*100,
    (propB['area']/max_area)*100,
    (1 - propB['price_per_m2']/(max_price/100))*100 if max_price>0 else 50,
    (1 - propB['distance_to_center_km']/max_dist)*100 if max_dist>0 else 50,
    (1 - propB['building_age']/max_age)*100
]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=valsA,
    theta=categories,
    fill='toself',
    name=f"Property A (#{propA['id']})",
    line_color='#1d4ed8'
))

fig.add_trace(go.Scatterpolar(
    r=valsB,
    theta=categories,
    fill='toself',
    name=f"Property B (#{propB['id']})",
    line_color='#38bdf8'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100])
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#0f172a",
    height=420
)

st.plotly_chart(fig, use_container_width=True)