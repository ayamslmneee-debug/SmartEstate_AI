import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Financial & ROI",
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
    
    .roi-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 58, 138, 0.88) 50%, rgba(37, 99, 235, 0.82) 100%), 
                    url('https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1600&q=80');
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

    .metric-card-blue {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%);
        padding: 22px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 20px rgba(29, 78, 216, 0.22);
    }

    .metric-card-light {
        background: #f0f9ff;
        border: 2px solid #bae6fd;
        padding: 22px;
        border-radius: 20px;
        color: #0f172a;
        text-align: center;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.05);
    }

    .metric-val {
        font-size: 32px;
        font-weight: 900;
        margin: 5px 0;
    }

    .metric-lbl {
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .input-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 6px 18px rgba(2, 132, 199, 0.05);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Header
st.markdown("""
    <div class="roi-hero">
        <h1 class="hero-title-text">📈 Investment ROI & Mortgage Engine</h1>
        <p class="hero-sub-text">Calculate projected rental yields, mortgage payments, and 5-year capital growth</p>
    </div>
""", unsafe_allow_html=True)

# 4. Inputs Section
st.subheader("⚙️ Financial Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    st.markdown("##### 🏦 Property & Mortgage Details")
    prop_price = st.number_input("Property Purchase Price ($)", value=250000, step=10000)
    down_payment_pct = st.slider("Down Payment (%)", min_value=10, max_value=80, value=20, step=5)
    interest_rate = st.slider("Mortgage Interest Rate (%)", min_value=1.0, max_value=12.0, value=6.5, step=0.1)
    loan_years = st.selectbox("Loan Tenure (Years)", [10, 15, 20, 25, 30], index=3)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    st.markdown("##### 🔑 Rental Income & Appreciation")
    monthly_rent = st.number_input("Expected Monthly Rent ($)", value=1800, step=100)
    occupancy_rate = st.slider("Occupancy Rate (%)", min_value=50, max_value=100, value=92, step=1)
    annual_appreciation = st.slider("Expected Annual Price Growth (%)", min_value=1.0, max_value=15.0, value=4.5, step=0.5)
    maintenance_pct = st.number_input("Annual Maintenance & Taxes (% of Price)", value=1.5, step=0.1)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. Calculations
down_payment = prop_price * (down_payment_pct / 100)
loan_amount = prop_price - down_payment

# Monthly Mortgage Calculation (PMI formula)
monthly_rate = (interest_rate / 100) / 12
num_payments = loan_years * 12

if monthly_rate > 0:
    monthly_mortgage = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / (((1 + monthly_rate)**num_payments) - 1)
else:
    monthly_mortgage = loan_amount / num_payments

# Annual Cashflows
annual_gross_rent = (monthly_rent * 12) * (occupancy_rate / 100)
annual_maintenance = prop_price * (maintenance_pct / 100)
annual_mortgage = monthly_mortgage * 12
annual_net_cashflow = annual_gross_rent - annual_mortgage - annual_maintenance

gross_roi = (annual_gross_rent / prop_price) * 100
net_roi = (annual_net_cashflow / down_payment) * 100 if down_payment > 0 else 0

# 6. Top Metrics Dashboard
st.write("---")
st.subheader("📊 Investment Yield Summary")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
        <div class="metric-card-blue">
            <div class="metric-lbl">Monthly Mortgage</div>
            <div class="metric-val">${monthly_mortgage:,.0f}</div>
            <span style="font-size:12px; opacity:0.85;">Principal + Interest</span>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
        <div class="metric-card-light">
            <div class="metric-lbl" style="color:#0369a1;">Gross Rental Yield</div>
            <div class="metric-val" style="color:#1d4ed8;">{gross_roi:.2f}%</div>
            <span style="font-size:12px; color:#475569;">Annual Gross / Price</span>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
        <div class="metric-card-light">
            <div class="metric-lbl" style="color:#0369a1;">Cash-on-Cash ROI</div>
            <div class="metric-val" style="color:{'#16a34a' if net_roi >= 0 else '#dc2626'};">{net_roi:.2f}%</div>
            <span style="font-size:12px; color:#475569;">Net Cash / Down Payment</span>
        </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
        <div class="metric-card-blue">
            <div class="metric-lbl">Net Annual Cashflow</div>
            <div class="metric-val" style="color:{'#86efac' if annual_net_cashflow >= 0 else '#fca5a5'};">${annual_net_cashflow:,.0f}</div>
            <span style="font-size:12px; opacity:0.85;">After Mortgage & Tax</span>
        </div>
    """, unsafe_allow_html=True)

st.write(" ")

# 7. 5-Year Capital Growth Forecasting Chart
st.subheader("🔮 5-Year Value & Equity Projection")

years = list(range(0, 6))
property_values = [prop_price * ((1 + (annual_appreciation / 100)) ** y) for y in years]
equity_values = [down_payment + (property_values[y] - prop_price) for y in years]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=years, y=property_values,
    mode='lines+markers',
    name='Projected Property Value',
    line=dict(color='#1d4ed8', width=4),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=years, y=equity_values,
    mode='lines+markers',
    name='Estimated Investor Equity',
    line=dict(color='#0284c7', width=3, dash='dash'),
    marker=dict(size=7)
))

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#0f172a",
    xaxis=dict(title="Years in Investment", tickmode='linear'),
    yaxis=dict(title="Value ($)"),
    height=380,
    margin=dict(l=0, r=0, t=20, b=0),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)