import streamlit as st

st.set_page_config(page_title="About | SmartEstate AI", page_icon="💡", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff; 
        color: #0f172a; 
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        padding: 35px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.2);
    }
    
    .feature-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        height: 100%;
        transition: transform 0.2s;
    }
    
    .tech-badge {
        display: inline-block;
        background: #e0e7ff;
        color: #4338ca;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        margin: 4px;
    }
    
    .step-box {
        background: #ffffff;
        border-left: 4px solid #7c3aed;
        padding: 15px 20px;
        margin-bottom: 12px;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="hero-banner">
        <h1>✨ Discover SmartEstate AI</h1>
        <p style="font-size: 18px; opacity: 0.95;">Transforming Real Estate Valuation with Data Science & Intelligent Recommendations</p>
    </div>
""", unsafe_allow_html=True)

# Main Grid (2 Columns)
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🚀 Our Mission & Vision</h3>
        <p style="color: #475569; font-size: 16px; line-height: 1.6;">
            Finding the right property within a target budget can be overwhelming. <b>SmartEstate AI</b> solves this problem by utilizing advanced Machine Learning models to predict accurate house valuations and offer tailored alternative choices when market prices exceed your budget limits.
        </p>
        <hr style="border-top: 1px solid #e2e8f0; margin: 20px 0;">
        <h3>🔄 How It Works</h3>
        <div class="step-box"><b>1. Feature Input:</b> Specify property parameters (Area, Rooms, Location).</div>
        <div class="step-box"><b>2. Model Prediction:</b> RandomForest Regressor calculates property value.</div>
        <div class="step-box"><b>3. Budget Check & Recommendation:</b> Compares result with user budget & suggests affordable matches.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🛠️ Tech Stack & Engineering</h3>
        <p style="color: #64748b; margin-bottom: 15px;">Built using industry-standard Data Science and Machine Learning tools:</p>
        <div>
            <span class="tech-badge">🐍 Python 3.x</span>
            <span class="tech-badge">🤖 Scikit-Learn</span>
            <span class="tech-badge">📊 Pandas & NumPy</span>
            <span class="tech-badge">📈 Plotly Express</span>
            <span class="tech-badge">🎨 Streamlit Framework</span>
            <span class="tech-badge">🌲 Random Forest</span>
        </div>
        <hr style="border-top: 1px solid #e2e8f0; margin: 20px 0;">
        <h3>⭐ Key Highlights</h3>
        <ul>
            <li><b>Real-time Price Estimation</b></li>
            <li><b>Interactive 5-Year Market Trends</b></li>
            <li><b>Smart Budget Recommendation System</b></li>
            <li><b>Fully Responsive & Clean UI Design</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)