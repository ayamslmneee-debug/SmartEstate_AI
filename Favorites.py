import streamlit as st
import pandas as pd

st.set_page_config(page_title="Favorites & Search | SmartEstate AI", page_icon="❤️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .fav-header {
        background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    .prop-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# قائمة صور عقارات عالية الجودة
property_images = [
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1600585152220-90363fe7e115?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80"
]

if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.markdown("""
    <div class="fav-header">
        <h1>❤️ Saved Favorites & Property Finder</h1>
        <p>Search, filter, view photos, and save your favorite real estate listings</p>
    </div>
""", unsafe_allow_html=True)

df = pd.read_csv("data/houses.csv")

tab1, tab2 = st.tabs(["🔍 Search & Browse", f"❤️ Saved Properties ({len(st.session_state.favorites)})"])

with tab1:
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        selected_city = st.multiselect("Filter by City", options=df['city'].unique(), default=df['city'].unique())
    with col_f2:
        max_price = st.slider("Filter by Max Price ($)", min_value=30000, max_value=500000, value=350000, step=10000)
        
    filtered_df = df[(df['city'].isin(selected_city)) & (df['price'] <= max_price)]
    
    st.write(f"Showing **{len(filtered_df)}** properties:")
    st.write("---")
    
    for idx, row in filtered_df.iterrows():
        # ربط كل عقار بصورة مميزة بناءً على الـ index
        img_url = property_images[idx % len(property_images)]
        
        col_img, col_info = st.columns([1, 2])
        
        with col_img:
            st.image(img_url, use_container_width=True)
            
        with col_info:
            sea_view = row.get('sea_view', 'N/A')
            power = row.get('electricity_247', 'N/A')
            
            st.markdown(f"""
                <div class="prop-card">
                    <h2 style="color:#e11d48; margin-top:0;">📍 {row['city']} — ${row['price']:,}</h2>
                    <p style="font-size:16px;">📐 <b>Area:</b> {row['area']} m² | 🛏️ <b>Bedrooms:</b> {row['bedrooms']} | 🛁 <b>Bathrooms:</b> {row['bathrooms']}</p>
                    <p style="font-size:14px; color:#64748b;">🌊 <b>Sea View:</b> {sea_view} | ⚡ <b>24/7 Electricity:</b> {power}</p>
                </div>
            """, unsafe_allow_html=True)
            
            fav_button_label = "❤️ Save to Favorites"
            if row.to_dict() in st.session_state.favorites:
                fav_button_label = "✅ Saved in Favorites"
                
            if st.button(fav_button_label, key=f"btn_{idx}"):
                if row.to_dict() not in st.session_state.favorites:
                    st.session_state.favorites.append(row.to_dict())
                    st.rerun()
        st.write("---")

with tab2:
    if not st.session_state.favorites:
        st.info("No saved properties yet. Browse the listings to add your favorites!")
    else:
        fav_df = pd.DataFrame(st.session_state.favorites)
        st.dataframe(fav_df, use_container_width=True)
        
        if st.button("🗑️ Clear All Favorites"):
            st.session_state.favorites = []
            st.rerun()