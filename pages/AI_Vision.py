import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="SmartEstate AI | AI Vision & Staging",
    page_icon="🎨",
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
    
    .vision-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.90) 0%, rgba(30, 58, 138, 0.92) 50%, rgba(37, 99, 235, 0.88) 100%), 
                    url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1600&q=80');
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

    .gallery-card {
        border: 2px solid #e0f2fe;
        border-radius: 16px;
        overflow: hidden;
        text-align: center;
        margin-bottom: 10px;
    }

    .gallery-img {
        width: 100%;
        height: 140px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load Data & Photos
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/houses.csv")
    except:
        df = pd.DataFrame({
            'id': [101, 102, 103, 104],
            'city': ['Beirut', 'Jounieh', 'Beirut', 'Byblos'],
            'price': [220000, 185000, 310000, 150000],
            'area': [160, 140, 210, 120]
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
    <div class="vision-hero">
        <h1 class="hero-title-text">✨ AI Property Vision & Staging</h1>
        <p class="hero-sub-text">Visualize future renovations, interior styles, and architectural renders powered by AI</p>
    </div>
""", unsafe_allow_html=True)

# 5. Preset Inspiration Gallery
st.markdown('<div class="card-box">', unsafe_allow_html=True)
st.subheader("🖼️ Inspiration Gallery (Design Styles)")

g1, g2, g3, g4 = st.columns(4)

with g1:
    st.markdown("""
        <div class="gallery-card">
            <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=600&q=80" class="gallery-img">
            <p style="font-weight:700; color:#1d4ed8; margin:8px 0;">Modern Royal Blue</p>
        </div>
    """, unsafe_allow_html=True)

with g2:
    st.markdown("""
        <div class="gallery-card">
            <img src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=600&q=80" class="gallery-img">
            <p style="font-weight:700; color:#1d4ed8; margin:8px 0;">Ultra Luxury Marble</p>
        </div>
    """, unsafe_allow_html=True)

with g3:
    st.markdown("""
        <div class="gallery-card">
            <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=600&q=80" class="gallery-img">
            <p style="font-weight:700; color:#1d4ed8; margin:8px 0;">Minimalist White</p>
        </div>
    """, unsafe_allow_html=True)

with g4:
    st.markdown("""
        <div class="gallery-card">
            <img src="https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=600&q=80" class="gallery-img">
            <p style="font-weight:700; color:#1d4ed8; margin:8px 0;">Villa & Infinity Pool</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. Controls & Live Render Engine
col_controls, col_display = st.columns([1.1, 0.9])

options = [f"Property #{row['id']} | {row['city']} | ${row['price']:,.0f}" for _, row in df.iterrows()]

with col_controls:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("🎨 Custom AI Generator")
    
    selected_idx = st.selectbox("Select Property 🏢", range(len(options)), format_func=lambda x: options[x], index=0)
    selected_prop = df.iloc[selected_idx]
    
    # Original Image Preview
    st.image(selected_prop['image_url'], caption=f"Original Photo - Property #{selected_prop['id']}", use_container_width=True)
    
    room_type = st.selectbox("Target Area 🏠", ["Luxury Living Room", "Modern Master Bedroom", "Ultra-Modern Kitchen", "Villa Exterior & Garden", "Infinity Pool Balcony View"])
    
    design_style = st.select_slider(
        "Design Aesthetic 🛋️",
        options=["Minimalist White", "Scandinavian Warm", "Modern Royal Blue & Gold", "Ultra Luxury Marble", "Futuristic Architectural"]
    )
    
    lighting = st.radio("Lighting ☀️", ["Golden Hour Sunset", "Bright Natural Daylight", "Cozy Evening Warm Lighting"], horizontal=True)
    
    generate_btn = st.button("🚀 Generate AI Property Render", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

def generate_ai_image(prompt_text):
    formatted_prompt = requests.utils.quote(f"high-end real estate render, {prompt_text}, architectural photography, 8k resolution, photorealistic, interior design magazine style")
    image_url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=1024&height=768&seed=42&nologo=true"
    
    response = requests.get(image_url)
    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content)), image_url
    return None, None

with col_display:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("🖼️ Generated Vision Output")
    
    if generate_btn:
        full_prompt = f"{room_type} for apartment in {selected_prop['city']}, {design_style} style, {lighting}"
        
        with st.spinner("✨ AI is rendering your property vision... Please wait..."):
            img, img_url = generate_ai_image(full_prompt)
            
            if img:
                st.image(img, caption=f"AI Generated Vision for Property #{selected_prop['id']}", use_container_width=True)
                
                buf = io.BytesIO()
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="📥 Download High-Res Render",
                    data=byte_im,
                    file_name=f"SmartEstate_Vision_Prop_{selected_prop['id']}.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
            else:
                st.error("Failed to generate image. Please try again.")
    else:
        st.info("👈 Choose your desired design preferences on the left and click **'Generate AI Property Render'**.")
        st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=80", caption="Sample Render Output", use_container_width=True)
        
    st.markdown('</div>', unsafe_allow_html=True)