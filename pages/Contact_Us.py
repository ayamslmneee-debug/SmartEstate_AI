import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Contact Us",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Styling (Royal Blue & Clean White)
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        color: #0f172a; 
    }
    
    .contact-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.90) 0%, rgba(30, 58, 138, 0.92) 50%, rgba(37, 99, 235, 0.88) 100%), 
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

    .contact-card {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }

    .contact-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
    }

    .icon-box {
        font-size: 40px;
        margin-bottom: 15px;
    }

    .contact-title {
        font-size: 16px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .contact-value {
        font-size: 20px;
        font-weight: 800;
        color: #1d4ed8;
    }

    .form-box {
        background: #ffffff;
        border: 2px solid #e0f2fe;
        border-radius: 22px;
        padding: 30px;
        box-shadow: 0 8px 24px rgba(2, 132, 199, 0.06);
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Banner
st.markdown("""
    <div class="contact-hero">
        <h1 class="hero-title-text">📬 Get in Touch with Us</h1>
        <p class="hero-sub-text">Have questions, partnership inquiries, or interested in acquiring SmartEstate AI?</p>
    </div>
""", unsafe_allow_html=True)

# 4. Contact Information Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="contact-card">
            <div class="icon-box">📧</div>
            <div class="contact-title">Direct Email</div>
            <div class="contact-value"><a href="mailto:ayamslmneee@gmail.com" style="color:#1d4ed8; text-decoration:none;">ayamslmneee@gmail.com</a></div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="contact-card">
            <div class="icon-box">📱</div>
            <div class="contact-title">Phone & WhatsApp</div>
            <div class="contact-value"><a href="https://wa.me/96176460259" target="_blank" style="color:#1d4ed8; text-decoration:none;">+961 76 460 259</a></div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="contact-card">
            <div class="icon-box">📍</div>
            <div class="contact-title">Headquarters</div>
            <div class="contact-value" style="color:#0f172a;">Beirut, Lebanon</div>
        </div>
    """, unsafe_allow_html=True)

# 5. Direct Message Form
st.markdown('<div class="form-box">', unsafe_allow_html=True)
st.subheader("💬 Send Us a Direct Message")

col_form1, col_form2 = st.columns(2)

with col_form1:
    client_name = st.text_input("Your Full Name")
    client_email = st.text_input("Your Email Address")

with col_form2:
    client_phone = st.text_input("Your Phone Number")
    inquiry_type = st.selectbox("Inquiry Type", ["Property Purchase Inquiry", "Software Licensing / Buy Project", "Investor Partnership", "General Question"])

message_body = st.text_area("Your Message", height=120 , placeholder="Write your message here...")

if st.button("🚀 Send Message Now", type="primary", use_container_width=True):
    if client_name and client_email and message_body:
        st.success("✅ Thank you! Your message has been received successfully. We will get back to you shortly!")
    else:
        st.warning("⚠️ Please fill in your name, email, and message before sending.")

st.markdown('</div>', unsafe_allow_html=True)