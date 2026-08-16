import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Premier Real Estate Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Ultra-Modern Blue & Pure White Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.82) 0%, rgba(30, 58, 138, 0.85) 50%, rgba(37, 99, 235, 0.8) 100%), 
                    url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        padding: 70px 30px;
        border-radius: 28px;
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 15px 35px rgba(29, 78, 216, 0.22);
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: 900;
        letter-spacing: -0.5px;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #ffffff 0%, #93c5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 20px;
        opacity: 0.95;
        max-width: 800px;
        margin: 0 auto 25px auto;
        color: #e0f2fe;
        line-height: 1.6;
    }
    
    .pill-tag {
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(10px);
        color: #ffffff;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .feature-card {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 20px;
        padding: 28px 22px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(2, 132, 199, 0.05);
        transition: all 0.35s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: #2563eb;
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.15);
    }
    
    .feature-icon-wrapper {
        width: 65px;
        height: 65px;
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 18px auto;
        font-size: 30px;
        color: #1d4ed8;
    }
    
    .feature-title {
        color: #1e3a8a;
        font-weight: 800;
        font-size: 21px;
        margin-bottom: 10px;
    }
    
    .feature-desc {
        color: #475569;
        font-size: 14px;
        line-height: 1.65;
    }

    .visual-section {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 24px;
        padding: 35px;
        border: 2px solid #bae6fd;
        margin: 40px 0;
    }

    .stat-badge {
        background: #ffffff;
        border: 2px solid #93c5fd;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.06);
    }
    .stat-number {
        font-size: 32px;
        font-weight: 800;
        color: #1d4ed8;
    }
    .stat-label {
        font-size: 13px;
        color: #0369a1;
        font-weight: 700;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Creative Hero Header
st.markdown("""
    <div class="hero-banner">
        <span class="pill-tag">✨ Next-Gen Real Estate AI</span>
        <div class="hero-title">SmartEstate AI</div>
        <div class="hero-subtitle">
            Empowering real estate investors, buyers, and developers with instant valuation predictions and advanced market analytics.
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Feature Showcase Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon-wrapper">🤖</div>
            <div class="feature-title">AI Price Prediction</div>
            <div class="feature-desc">
                High-precision machine learning valuation tailored to area, structural specs, distance, and luxury features.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon-wrapper">📊</div>
            <div class="feature-title">Market Intelligence</div>
            <div class="feature-desc">
                Interactive price distributions, city benchmark comparisons, and 5-year future growth forecasting metrics.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon-wrapper">📍</div>
            <div class="feature-title">Spatial Mapping</div>
            <div class="feature-desc">
                Geographical cluster maps pinpointing listings and location-based investment performance indicators.
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. Visual Showcase & Image Banner Section
st.markdown("""
    <div class="visual-section">
        <div style="text-align: center; margin-bottom: 25px;">
            <h2 style="color: #1e3a8a; font-weight: 800; margin: 0;">🏡 Premium Real Estate Insights</h2>
            <p style="color: #0369a1; font-size: 15px; margin-top: 5px;">Driven by advanced Random Forest regression models</p>
        </div>
""", unsafe_allow_html=True)

img_col1, img_col2 = st.columns(2)

with img_col1:
    st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.caption(" Modern Architecture & Urban Living Standards")

with img_col2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.caption(" Waterfront & Prime Location Valuations")

st.markdown("</div>", unsafe_allow_html=True)

# 6. Live Metrics Counter
try:
    df = pd.read_csv("data/houses.csv")
    
    st.subheader("🌐 Live Data Metrics Tracked")
    
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-number">{len(df)}</div>
                <div class="stat-label">Properties Indexed</div>
            </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-number">${df['price'].mean():,.0f}</div>
                <div class="stat-label">Avg Property Price</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-number">{df['area'].mean():,.0f} m²</div>
                <div class="stat-label">Average Size</div>
            </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
            <div class="stat-badge">
                <div class="stat-number">{df['city'].nunique()}</div>
                <div class="stat-label">Key Cities Covered</div>
            </div>
        """, unsafe_allow_html=True)

except Exception:
    pass

st.write("---")
st.info("👈 Use the sidebar navigation menu to switch pages and test the AI prediction engine!")

st.set_page_config(page_title="SmartEstate AI | Overview", page_icon="🏠", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; color: #0f172a; }
    .card-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 Market Dashboard & Live Ticker")

# Live Market Indices Section
st.markdown("### 📊 Live Real Estate Market Indices (Price / m²)")
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(label="📍 Beirut Central", value="$2,450 / m²", delta="+3.2% YoY")
with m2:
    st.metric(label="📍 Jounieh Coast", value="$1,580 / m²", delta="+1.8% YoY")
with m3:
    st.metric(label="📍 Byblos Historic", value="$1,220 / m²", delta="+2.4% YoY")
with m4:
    st.metric(label="📍 Metn Heights", value="$1,750 / m²", delta="-0.5% YoY", delta_color="inverse")

st.markdown("---")

col_left, col_right = st.columns([1.2, 0.8])

with col_left:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("💡 Welcome to SmartEstate AI")
    st.write("""
        SmartEstate AI is a next-generation real estate intelligence platform designed for buyers, 
        investors, and brokers. Utilize advanced machine learning models to forecast prices, calculate 
        investment returns, dynamically stage properties, and generate formal PDF reports.
    """)
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80", caption="Luxury Villa Portfolio", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("🚀 Platform Modules")
    st.markdown("""
    - **🤖 Property Predictor**: Accurate ML valuation engine.
    - **📈 Market Analytics**: Interactive distribution & scatter plots.
    - **💰 Investment ROI**: Cash flow & cap rate calculations.
    - **🎨 AI Vision & Staging**: Virtual interior rendering.
    - **⚔️ Property Battle**: Side-by-side comparison engine.
    - **📞 Contact Us**: Direct inquiries & booking.
    """)
    st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80", caption="Modern Living Room", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)