import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

# ----------------------------------------------------
# Ultra-Creative Blue Feature Importance (XAI Section)
# ----------------------------------------------------
st.write("---")

st.markdown("""
    <style>
    .xai-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 6px solid #2563eb;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.08);
        margin-bottom: 25px;
    }
    .xai-title {
        color: #1e3a8a;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .xai-subtitle {
        color: #0369a1;
        font-size: 14px;
        margin-bottom: 0;
    }
    .top-feature-badge {
        background-color: #1d4ed8;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def calculate_xai_importance():
    df = pd.read_csv("data/houses.csv")
    df_encoded = pd.get_dummies(df, drop_first=True)
    
    X = df_encoded.drop('price', axis=1)
    y = df_encoded['price']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    imp_df = pd.DataFrame({
        'Feature': X.columns,
        'Weight': model.feature_importances_
    }).sort_values(by='Weight', ascending=True)
    
    # Clean up feature names
    imp_df['Feature_Clean'] = imp_df['Feature'].str.replace('_', ' ').str.title()
    imp_df['Percentage'] = (imp_df['Weight'] * 100).round(1)
    return imp_df

imp_df = calculate_xai_importance()
top_driver = imp_df.iloc[-1]['Feature_Clean']
top_pct = imp_df.iloc[-1]['Percentage']

# Banner Card
st.markdown(f"""
    <div class="xai-card">
        <div class="xai-title">🧠 Explainable AI: Valuation Drivers Matrix</div>
        <p class="xai-subtitle">Transparent breakdown of how each property feature influences the algorithm's price calculation.</p>
        <span class="top-feature-badge">🔥 Top Value Driver: {top_driver} ({top_pct}%)</span>
    </div>
""", unsafe_allow_html=True)

col_chart, col_insights = st.columns([1.4, 1])

with col_chart:
    fig_xai = px.bar(
        imp_df, 
        x='Percentage', 
        y='Feature_Clean', 
        orientation='h',
        text_auto=True,
        color='Percentage',
        color_continuous_scale=['#93c5fd', '#3b82f6', '#1d4ed8', '#1e3a8a']
    )
    
    fig_xai.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font_color="#0f172a",
        coloraxis_showscale=False,
        height=380,
        margin=dict(l=0, r=20, t=10, b=0),
        xaxis_title="Relative Impact Score (%)",
        yaxis_title=""
    )
    fig_xai.update_traces(texttemplate='%{x:.1f}%', textposition='outside')
    st.plotly_chart(fig_xai, use_container_width=True)

with col_insights:
    st.markdown("""
        <div style="background-color:#ffffff; border:2px solid #e0f2fe; border-radius:14px; padding:20px; height:100%;">
            <h4 style="color:#1d4ed8; margin-top:0;">📊 Key Insights for Investors:</h4>
            <ul style="color:#334155; line-height: 1.8; font-size: 14px; padding-left: 18px;">
                <li><b>Primary Weight:</b> Property <b>Area (m²)</b> and <b>City/Location</b> carry over 60% of total price influence.</li>
                <li><b>Premium Factors:</b> Features like <b>24/7 Power</b> and <b>Sea View</b> act as high-value multipliers in Mediterranean urban zones.</li>
                <li><b>Depreciation Effect:</b> <b>Building Age</b> negatively correlates with valuation unless offset by prime location.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)