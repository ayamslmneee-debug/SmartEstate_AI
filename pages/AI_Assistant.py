import streamlit as st
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | Smart Assistant",
    page_icon="💎",
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
    
    .chat-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.88) 0%, rgba(30, 58, 138, 0.90) 50%, rgba(37, 99, 235, 0.85) 100%), 
                    url('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1600&q=80');
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

    /* Property Card inside Chat */
    .chat-prop-card {
        background: #f0f9ff;
        border: 2px solid #bae6fd;
        border-radius: 18px;
        padding: 16px;
        margin-top: 10px;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.08);
    }

    .chat-prop-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
    }

    .quick-chip-btn {
        background: #f0f9ff;
        border: 1px solid #2563eb;
        color: #1d4ed8;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13.5px;
        font-weight: 700;
        cursor: pointer;
        margin-right: 8px;
        margin-bottom: 10px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load Property Data & Images
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
    <div class="chat-hero">
        <h1 class="hero-title-text">🤖 Smart Estate AI Advisor</h1>
        <p class="hero-sub-text">Ask questions, find personalized properties with photos, or get investment insights</p>
    </div>
""", unsafe_allow_html=True)

# 5. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm your **SmartEstate AI Assistant**. How can I help you today? You can ask me to find properties, evaluate budgets, or compare city prices!",
            "card": None
        }
    ]

# 6. Sidebar & Quick Prompts
with st.sidebar:
    st.markdown("### 💡 Recommended Prompts")
    st.info("Click any prompt to instantly ask the AI assistant:")
    
    q1 = st.button("🌊 Show me properties under $200k")
    q2 = st.button("🏙️ Best property for investment in Beirut?")
    q3 = st.button("📊 How does the AI calculate prices?")

# Handle Quick Prompt Clicks
prompt_input = None
if q1:
    prompt_input = "Show me properties under $200k"
elif q2:
    prompt_input = "Best property for investment in Beirut?"
elif q3:
    prompt_input = "How does the AI calculate prices?"

# 7. Render Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        # Render visual property card if present
        if msg.get("card"):
            p = msg["card"]
            st.markdown(f"""
                <div class="chat-prop-card">
                    <img src="{p['image_url']}" class="chat-prop-img" />
                    <h4 style="color:#1d4ed8; margin:10px 0 4px 0; font-weight:800;">Property #{p['id']} - {p['city']}</h4>
                    <p style="color:#0f172a; font-weight:800; font-size:18px; margin:0 0 8px 0;">${p['price']:,.0f}</p>
                    <p style="color:#64748b; font-size:13px; margin:0;">📐 {p['area']} m² | 🛏️ {p['bedrooms']} Beds | 🛁 {p['bathrooms']} Baths</p>
                </div>
            """, unsafe_allow_html=True)

# 8. User Input Processing
user_prompt = st.chat_input("Type your question here...") or prompt_input

if user_prompt:
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": user_prompt, "card": None})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # AI Reasoning Logic
    reply_text = ""
    suggested_card = None
    lower_p = user_prompt.lower()

    if "under" in lower_p or "budget" in lower_p or "200" in lower_p or "$" in lower_p:
        cheap_props = df[df['price'] <= 200000]
        if not cheap_props.empty:
            p = cheap_props.iloc[0]
            reply_text = f"Here is an excellent option matching your budget criteria! **Property #{p['id']}** in **{p['city']}** offers high value at **${p['price']:,.0f}**."
            suggested_card = p.to_dict()
        else:
            reply_text = f"I searched the database! Our lowest price property starts at **${df['price'].min():,.0f}** in {df.loc[df['price'].idxmin()]['city']}."
            suggested_card = df.loc[df['price'].idxmin()].to_dict()

    elif "beirut" in lower_p or "investment" in lower_p or "best" in lower_p:
        beirut_props = df[df['city'].str.contains("Beirut", case=False, na=False)]
        if not beirut_props.empty:
            p = beirut_props.iloc[0]
            reply_text = f"For top investment ROI in **Beirut**, check out **Property #{p['id']}**. It's located just **{p['distance_to_center_km']} km** from the center with strong projected appreciation!"
            suggested_card = p.to_dict()
        else:
            p = df.iloc[0]
            reply_text = f"Here is our top recommended property for investment score: **Property #{p['id']}** in **{p['city']}**!"
            suggested_card = p.to_dict()

    elif "calculate" in lower_p or "how" in lower_p or "ai" in lower_p:
        reply_text = "Our **SmartEstate AI** uses a **Random Forest Regressor** trained on real estate parameters including area (m²), distance to city center, building age, bedrooms, and premium amenities."

    else:
        p = df.sample(1).iloc[0]
        reply_text = f"I found a featured listing that might interest you! **Property #{p['id']}** in **{p['city']}** priced at **${p['price']:,.0f}**."
        suggested_card = p.to_dict()

    # Simulate AI Typing
    time.sleep(0.4)

    # Append Assistant Reply
    st.session_state.messages.append({"role": "assistant", "content": reply_text, "card": suggested_card})
    
    # Rerun to update chat screen instantly
    st.rerun()