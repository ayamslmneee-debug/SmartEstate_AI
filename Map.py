import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Property Map | SmartEstate AI", page_icon="🗺️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .map-header {
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="map-header">
        <h1>🗺️ Interactive Property Map</h1>
        <p style="font-size: 16px; opacity: 0.95;">Explore real estate distribution and average market prices across regions</p>
    </div>
""", unsafe_allow_html=True)

# Coordinates dictionary for cities
city_coords = {
    'Beirut': [33.8938, 35.5018],
    'Jounieh': [33.9808, 35.6178],
    'Byblos': [34.1228, 35.6517],
    'Saida': [33.5631, 35.3689],
    'Tripoli': [34.4367, 35.8497]
}

data = pd.read_csv("data/houses.csv")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 City Summary")
    city_summary = data.groupby('city').agg(
        Avg_Price=('price', 'mean'),
        Property_Count=('price', 'count')
    ).reset_index()
    
    for idx, row in city_summary.iterrows():
        st.info(f"**{row['city']}**: Avg Price: **${row['Avg_Price']:,.0f}** ({row['Property_Count']} listings)")

with col2:
    # Initialize Folium Map centered on Lebanon
    m = folium.Map(location=[33.9000, 35.5300], zoom_start=9)
    
    for idx, row in data.iterrows():
        coords = city_coords.get(row['city'], [33.8938, 35.5018])
        # Slight random shift so pins don't overlap exactly
        lat = coords[0] + (idx % 3) * 0.005
        lon = coords[1] + (idx % 2) * 0.005
        
        popup_text = f"<b>{row['city']}</b><br>Price: ${row['price']:,}<br>Area: {row['area']}m²<br>Rooms: {row['bedrooms']} Bed | {row['bathrooms']} Bath"
        
        folium.Marker(
            location=[lat, lon],
            popup=popup_text,
            tooltip=f"{row['city']} - ${row['price']:,}",
            icon=folium.Icon(color="blue" if row['price'] > 150000 else "green", icon="home", prefix="fa")
        ).add_to(m)
        
    st_folium(m, width=700, height=500)