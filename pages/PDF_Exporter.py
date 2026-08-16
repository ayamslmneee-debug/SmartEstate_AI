import streamlit as st
import pandas as pd
from fpdf import FPDF

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Export PDF Report",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Royal Blue Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .pdf-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.88) 0%, rgba(30, 58, 138, 0.90) 50%, rgba(37, 99, 235, 0.85) 100%), 
                    url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        padding: 45px 30px;
        border-radius: 26px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 12px 30px rgba(37, 99, 235, 0.22);
    }
    
    .hero-title-text {
        font-size: 40px;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(90deg, #ffffff 0%, #93c5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-sub-text {
        font-size: 17px;
        color: #e0f2fe;
        margin-top: 8px;
        opacity: 0.95;
    }

    .card-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
        margin-bottom: 25px;
    }

    .prop-img-box {
        border-radius: 18px;
        overflow: hidden;
        border: 2px solid #bae6fd;
        height: 260px;
        margin-bottom: 15px;
    }

    .prop-img-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load Data & Images
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
    <div class="pdf-hero">
        <h1 class="hero-title-text">📄 Visual Investment PDF Report</h1>
        <p class="hero-sub-text">Generate professional client-ready investment teardowns instantly</p>
    </div>
""", unsafe_allow_html=True)

# 5. Form & Preview Layout
col_input, col_preview = st.columns([1.1, 0.9])

options = [f"Property #{row['id']} | {row['city']} | ${row['price']:,.0f}" for _, row in df.iterrows()]

with col_input:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("⚙️ Select Parameters")
    
    selected_idx = st.selectbox("Select Property 🏢", range(len(options)), format_func=lambda x: options[x], index=0)
    selected_prop = df.iloc[selected_idx]
    
    investor_name = st.text_input("Investor / Client Name", value="Valued Client")
    monthly_rent = st.number_input("Expected Monthly Rent ($)", value=1800, step=100)
    down_payment_pct = st.slider("Down Payment (%)", 10, 80, 20, 5)
    interest_rate = st.slider("Mortgage Interest Rate (%)", 1.0, 12.0, 6.5, 0.1)
    holding_years = st.selectbox("Investment Horizon (Years)", [3, 5, 10], index=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col_preview:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("🖼️ Property Preview")
    
    st.markdown(f"""
        <div class="prop-img-box">
            <img src="{selected_prop['image_url']}" alt="Property Preview Photo">
        </div>
        <h3 style="color:#1d4ed8; margin:0 0 5px 0; font-weight:800;">Property #{selected_prop['id']} - {selected_prop['city']}</h3>
        <p style="color:#0f172a; font-size:22px; font-weight:900; margin-bottom:10px;">${selected_prop['price']:,.0f}</p>
        <p style="color:#64748b; font-size:14px; margin:0;">📐 {selected_prop['area']} m² | 🛏️ {selected_prop['bedrooms']} Beds | 🛁 {selected_prop['bathrooms']} Baths</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. PDF Generator Class
class InvestmentPDF(FPDF):
    def header(self):
        self.set_fill_color(30, 58, 138)
        self.rect(0, 0, 210, 35, 'F')
        self.set_font('Arial', 'B', 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, 'SMARTESTATE AI', 0, 1, 'C')
        self.set_font('Arial', '', 11)
        self.cell(0, 6, 'Official Property Investment & Valuation Report', 0, 1, 'C')
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Generated by SmartEstate AI Engine | Confidential Investment Teardown', 0, 0, 'C')

def create_pdf(prop, client_name, rent, down_pct, int_rate, years):
    pdf = InvestmentPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, f"Prepared For: {client_name}", 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f"Property ID: #{prop['id']} | Location: {prop['city']}", 0, 1, 'L')
    pdf.ln(5)
    
    # Section 1
    pdf.set_fill_color(224, 242, 254)
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(29, 78, 216)
    pdf.cell(190, 8, "  1. PROPERTY SPECIFICATIONS", 0, 1, 'L', fill=True)
    pdf.ln(2)
    
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(15, 23, 42)
    
    specs = [
        ("Purchase Price:", f"${prop['price']:,.0f}"),
        ("Property Area:", f"{prop['area']} sq. meters"),
        ("Bedrooms / Bathrooms:", f"{prop['bedrooms']} Beds / {prop['bathrooms']} Baths"),
        ("Distance to City Center:", f"{prop['distance_to_center_km']} km"),
        ("Building Age:", f"{prop['building_age']} Years")
    ]
    
    for label, val in specs:
        pdf.cell(95, 7, f"  {label}", border='B')
        pdf.cell(95, 7, f"{val}", border='B', ln=1)
        
    pdf.ln(8)
    
    # Section 2
    price = prop['price']
    down_payment = price * (down_pct / 100)
    loan_amount = price - down_payment
    annual_gross_rent = rent * 12
    gross_yield = (annual_gross_rent / price) * 100
    projected_future_val = price * ((1 + 0.045) ** years)
    
    pdf.set_fill_color(224, 242, 254)
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(29, 78, 216)
    pdf.cell(190, 8, "  2. FINANCIAL & ROI BREAKDOWN", 0, 1, 'L', fill=True)
    pdf.ln(2)
    
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(15, 23, 42)
    
    fin_specs = [
        ("Down Payment Required:", f"${down_payment:,.0f} ({down_pct}%)"),
        ("Mortgage Loan Amount:", f"${loan_amount:,.0f}"),
        ("Estimated Interest Rate:", f"{int_rate}%"),
        ("Expected Monthly Rent:", f"${rent:,.0f}"),
        ("Gross Rental Yield:", f"{gross_yield:.2f}% / Year"),
        (f"Projected Value ({years} Years):", f"${projected_future_val:,.0f}")
    ]
    
    for label, val in fin_specs:
        pdf.cell(95, 7, f"  {label}", border='B')
        pdf.cell(95, 7, f"{val}", border='B', ln=1)
        
    pdf.ln(10)
    
    pdf.set_font('Arial', 'I', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.multi_cell(0, 5, "Notice: This report is generated automatically by SmartEstate AI based on machine learning predictions and historical trend data. Projections serve as estimates for decision support.")
    
    return pdf.output(dest='S').encode('latin-1')

# 7. Download Button
st.write("---")
col_center = st.columns([1, 2, 1])

with col_center[1]:
    pdf_bytes = create_pdf(
        selected_prop, investor_name, monthly_rent,
        down_payment_pct, interest_rate, holding_years
    )
    
    st.download_button(
        label="📥 Download Official Investment PDF Report",
        data=pdf_bytes,
        file_name=f"SmartEstate_Report_Prop_{selected_prop['id']}.pdf",
        mime="application/pdf",
        use_container_width=True
    )