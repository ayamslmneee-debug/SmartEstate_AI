import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
# Initialize Session State for Preferences
if "lang" not in st.session_state:
    st.session_state["lang"] = "English 🇬🇧"
if "theme" not in st.session_state:
    st.session_state["theme"] = "Light ☀️"

# Sidebar Controls for Theme & Language
st.sidebar.markdown("### ⚙️ Preferences / الإعدادات")

col_lang, col_theme = st.sidebar.columns(2)

with col_lang:
    selected_lang = st.selectbox(
        "🌐 Language",
        ["English 🇬🇧", "العربية 🇱🇧"],
        index=0 if st.session_state["lang"] == "English 🇬🇧" else 1,
        key="lang_select"
    )
    st.session_state["lang"] = selected_lang

with col_theme:
    selected_theme = st.radio(
        "🎨 Theme",
        ["Light ☀️", "Dark 🌙"],
        index=0 if st.session_state["theme"] == "Light ☀️" else 1,
        key="theme_radio",
        horizontal=True
    )
    st.session_state["theme"] = selected_theme

st.sidebar.markdown("---")

# Dynamic CSS Theme Injector
if st.session_state["theme"] == "Dark 🌙":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0f172a !important;
            color: #f8fafc !important;
        }
        .card-box, .stMarkdown, p, h1, h2, h3, label {
            color: #f8fafc !important;
        }
        div[data-testid="stSidebar"] {
            background-color: #1e293b !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #ffffff !important;
            color: #0f172a !important;
        }
        div[data-testid="stSidebar"] {
            background-color: #f8fafc !important;
        }
        </style>
    """, unsafe_allow_html=True)

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Light Theme CSS
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    
    .header-container {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        padding: 30px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(79, 70, 229, 0.15);
    }
    
    .css-card {
        background: #f8fafc;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
    
    .price-box {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        padding: 22px;
        border-radius: 14px;
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.2);
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        padding: 14px 28px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load & Train ML Model
@st.cache_data
def load_and_train():
    data = pd.read_csv("data/houses.csv")
    df_encoded = pd.get_dummies(data, columns=['parking', 'city'], drop_first=True)
    
    X = df_encoded.drop('price', axis=1)
    y = df_encoded['price']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return data, model, X.columns

data, model, feature_columns = load_and_train()

# 4. Header Banner
st.markdown("""
    <div class="header-container">
        <h1>🏠 SmartEstate AI</h1>
        <p style="font-size: 18px; opacity: 0.95;">AI-Powered Advanced Property Valuation & Analytics</p>
    </div>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

st.write(" ")

# 5. Inputs Layout (Advanced ML Features)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.subheader("📋 Property Features")
    area = st.number_input("Area (m²)", min_value=10, value=120)
    bedrooms = st.number_input("Bedrooms 🛏️", min_value=1, value=3)
    bathrooms = st.number_input("Bathrooms 🛁", min_value=1, value=2)
    city = st.selectbox("City / Region 📍", data['city'].unique())
    parking = st.selectbox("Parking Spot 🚗", ["Yes", "No"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.subheader("⚙️ Location & Building Details")
    distance = st.slider("Distance to City Center (km) 📍", min_value=0.5, max_value=20.0, value=2.5, step=0.5)
    age = st.number_input("Building Age (Years) 🏢", min_value=0, max_value=50, value=5)
    budget = st.number_input("Your Maximum Budget ($) 💰", min_value=10000, value=200000, step=5000)
    st.markdown('</div>', unsafe_allow_html=True)

st.write(" ")
predict_btn = st.button("✨ Calculate Valuation & AI Score")

# 6. Prediction & Results
if predict_btn:
    input_data = pd.DataFrame(0, index=[0], columns=feature_columns)
    input_data['area'] = area
    input_data['bedrooms'] = bedrooms
    input_data['bathrooms'] = bathrooms
    input_data['distance_to_center_km'] = distance
    input_data['building_age'] = age
    
    if f"parking_{parking}" in input_data.columns:
        input_data[f"parking_{parking}"] = 1
    if f"city_{city}" in input_data.columns:
        input_data[f"city_{city}"] = 1
        
    predicted_price = model.predict(input_data)[0]
    
    # Calculate Investment Score (Simple AI Algorithm)
    score = round(max(10, min(99, (area / (distance + 1)) * 1.5 - (age * 0.8))), 1)
    
    st.markdown("---")
    
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        st.markdown(f"""
            <div class="price-box">
                <p style="font-size: 15px; margin:0; opacity:0.9;">Estimated Market Price</p>
                ${predicted_price:,.0f}
            </div>
        """, unsafe_allow_html=True)
        
        st.write(" ")
        st.metric(label="🌟 Smart Investment Score", value=f"{score} / 100")
        
        if predicted_price <= budget:
            st.success("✅ Fits comfortably within your budget.")
        else:
            st.warning(f"⚠️ Over Budget by ${predicted_price - budget:,.0f}")

    with res_col2:
        city_avg = data[data['city'] == city]['price'].mean()
        fig_df = pd.DataFrame({
            'Category': ['Your Property', f'Avg in {city}'],
            'Price ($)': [predicted_price, city_avg]
        })
        fig = px.bar(
            fig_df, x='Category', y='Price ($)', color='Category', 
            color_discrete_sequence=['#7c3aed', '#2563eb'], 
            title=f"Price Comparison vs {city} Average"
        )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#0f172a")
        st.plotly_chart(fig, use_container_width=True)

    if predicted_price > budget:
        st.subheader("🏡 Recommended Alternatives Within Your Budget")
        recommendations = data[(data['price'] <= budget) & (data['city'] == city)].sort_values(by='price', ascending=False)
        
        if recommendations.empty:
            recommendations = data[data['price'] <= budget].sort_values(by='price', ascending=False)
            
        if not recommendations.empty:
            st.dataframe(recommendations, use_container_width=True)
        else:
            st.info("No properties found matching your budget limits.")

st.set_page_config(
    page_title="SmartEstate AI | Real Estate Intelligence",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Global Styling
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; color: #0f172a; }
    .main-header {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 58, 138, 0.92) 50%, rgba(37, 99, 235, 0.88) 100%),
                    url('https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        padding: 55px 35px;
        border-radius: 26px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 12px 30px rgba(37, 99, 235, 0.22);
    }
    .main-title {
        font-size: 44px;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(90deg, #ffffff 0%, #93c5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .main-subtitle { font-size: 18px; color: #e0f2fe; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Preferences & Mortgage Calculator
st.sidebar.title("🏢 SmartEstate AI")
st.sidebar.markdown("---")
st.sidebar.subheader("🌐 App Preferences")
lang = st.sidebar.radio("Language / اللغة", ["English 🇬🇧", "العربية 🇱🇧"], horizontal=True)

st.sidebar.markdown("---")
st.sidebar.subheader("🧮 Quick Mortgage Calculator")
home_price = st.sidebar.number_input("Property Price ($)", value=200000, step=10000)
down_payment_pct = st.sidebar.slider("Down Payment (%)", min_value=10, max_value=50, value=20)
loan_years = st.sidebar.selectbox("Loan Duration (Years)", [10, 15, 20, 25, 30], index=2)
interest_rate = st.sidebar.slider("Interest Rate (%)", min_value=2.0, max_value=12.0, value=6.5, step=0.5)

loan_amount = home_price * (1 - down_payment_pct / 100)
monthly_interest = (interest_rate / 100) / 12
total_months = loan_years * 12

if monthly_interest > 0:
    monthly_payment = loan_amount * (monthly_interest * (1 + monthly_interest)**total_months) / ((1 + monthly_interest)**total_months - 1)
else:
    monthly_payment = loan_amount / total_months

st.sidebar.metric("Estimated Monthly Payment", f"${monthly_payment:,.0f} / mo")
st.sidebar.caption(f"Down Payment: ${home_price * (down_payment_pct/100):,.0f} | Loan: ${loan_amount:,.0f}")

# Main Welcome Section
st.markdown("""
    <div class="main-header">
        <h1 class="main-title">SmartEstate AI Platform</h1>
        <p class="main-subtitle">AI-Driven Real Estate Analytics, Property Valuation, and Virtual Staging Suite</p>
    </div>
""", unsafe_allow_html=True)

st.info("👈 Please select a module from the sidebar navigation menu to begin.")          
