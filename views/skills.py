import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import os

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "skills_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# File based Lottie loader
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Get asset path dynamically
def get_asset_path(asset_key, asset_type="image"):
    if asset_type == "lottie":
        return config["lottie_animations"].get(asset_key, "")
    else:
        return config["asset_images"].get(asset_key, "")

# Load section icons (lottie animations)
section_lottie_keys = config["section_order"]
lottie_animations = {}
for key in section_lottie_keys:
    path = config["lottie_animations"].get(key)
    if path:
        lottie_animations[key] = load_lottiefile(path)

# Build skills data with asset paths resolved
skills_data = {}
for section_name, section_data in config["skills"].items():
    skills_list = []
    for skill in section_data["skills"]:
        asset_key = skill["asset_key"]
        asset_path = config["asset_images"].get(asset_key) or config["lottie_animations"].get(asset_key)
        
        # Pre-load lottie if it's a lottie file
        if asset_path and asset_path.endswith('.json'):
            try:
                asset_content = load_lottiefile(asset_path)
            except:
                asset_content = asset_path
        else:
            asset_content = asset_path
        
        skills_list.append({
            "name": skill["name"],
            "level": skill["level"],
            "asset": asset_content,
            "is_lottie": asset_path and asset_path.endswith('.json')
        })
    
    skills_data[section_name] = {
        "lottie_key": section_data["lottie_key"],
        "skills": skills_list
    }

# Top Section
with st.container():
    st.markdown(f'<h2 style="text-align: center;">{config["page_title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;">{config["page_subtitle"]}</p>', unsafe_allow_html=True)
    

# Initialize section index
section_index = 0

# Display skills by section
for section_name, section_data in skills_data.items():
    lottie_key = section_data["lottie_key"]
    section_lottie = lottie_animations.get(lottie_key)
    
    with st.container(border=True, gap="medium", height="content"):
        o_1, o_2 = st.columns([0.1, 0.9], vertical_alignment="top")
        with o_1:
            if section_lottie:
                st.lottie(section_lottie, width=50, height=50)
        with o_2:
            st.subheader(section_name)
        
        cols = st.columns(3)
        for i, skill in enumerate(section_data["skills"]):
            with cols[i % 3]:
                with st.container(border=True, gap="large"):
                    # row layout inside the card
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(
                            f"<div style='font-weight:600; font-size:18px;'>{skill['name']}</div>",
                            unsafe_allow_html=True,
                        )
                        st.markdown(
                            f"<div style='color:#666; font-size:14px;'>{skill['level']}</div>",
                            unsafe_allow_html=True,
                        )
                    with c2:
                        if skill['is_lottie']:
                            st_lottie(skill['asset'], width=40, height=40)
                        else:
                            st.image(skill['asset'])
            
st.divider()

with st.container(border=True):
    st.markdown('<h2 style="text-align: center;">Current Learning Focus</h2>', unsafe_allow_html=True)

    learning_focus = config["learning_focus"]
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader(learning_focus["section_1"]["title"], anchor=False)
        st.write(learning_focus["section_1"]["description"])

    with col2:
        st.subheader(learning_focus["section_2"]["title"], anchor=False)
        st.write(learning_focus["section_2"]["description"])
