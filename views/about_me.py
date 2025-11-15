import streamlit as st
import time
import json
import os
from utils import *

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "about_me_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

profile = config["profile"]

@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name")

col_1, col_2 = st.columns(2, gap = "small", vertical_alignment = "center")

with col_1:
    st.image(profile["profile_image"], width=profile["profile_image_width"])    

with col_2:
    st.title(profile["name"], anchor=False)
    st.write(profile["title"])
    st.write(profile["bio"])
    
    c_1, c_2 = st.columns([1,2], vertical_alignment="center")
    with c_1:
        st.badge(profile["location"])
    with c_2:
        st.badge(profile["availability"], width = "stretch")

st.divider()

# Beliefs Section
st.markdown('<h2 style="text-align: center;">What I Believe In</h2>', unsafe_allow_html=True)

beliefs = config["beliefs"]

# Two rows with two columns each
for i in range(0, len(beliefs), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        if i + j < len(beliefs):
            belief = beliefs[i + j]
            with col:
                st.markdown(
                    f"""
                    <div style="
                        background-color: #ffffff;
                        border-radius: 12px;
                        padding: 20px;
                        margin: 10px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                        display: flex;
                        align-items: flex-start;
                        ">
                        <div style="font-size:30px; margin-right:15px;">{belief['icon']}</div>
                        <div>
                            <div style="font-weight:600; font-size:18px; margin:0; color:#000000;">
                                {belief['title']}
                            </div>
                            <p style="margin:5px 0 0; color:#444444; font-size:14px;">
                                {belief['description']}
                            </p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


st.divider()

# Key Achievements Section

st.markdown('<h2 style="text-align: center;">Key Achievements</h2>', unsafe_allow_html=True)

achievements = config["achievements"]

# Display cards in a single column
for ach in achievements:
    st.markdown(
        f"""
        <div style="
            background-color: #ffffff;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            justify-content: space-between;
        ">
            <!-- Left side -->
            <div style="display:flex; align-items:center;">
                <div style="
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    font-size: 22px;
                    width: 48px;
                    height: 48px;
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 15px;
                ">{ach['icon']}</div>
                <div>
                    <div style="font-weight:500; font-size:18px; color:#000000;">
                        {ach['title']}
                    </div>
                    <p style="margin:5px 0 0; color:#444444; font-size:14px;">
                        {ach['description']}
                    </p>
                </div>
            </div>
            
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# GitHub Stats Fragment - Loads in Background
@st.fragment
def display_github_metrics():
    """Fragment to load GitHub metrics in background"""
    with st.container(border=True):
        st.markdown('<h2 style="text-align: center;">Fun Facts About Me</h2>', unsafe_allow_html=True)
        col_1, col_2, col_3 = st.columns(3, gap="large", vertical_alignment="center")
        
        try:
            github_stats = get_github_stats()
            github_contributions = get_github_contributions()
            
            with col_1:
                st.metric(
                    f"Projects Completed", 
                    str(github_stats.get("total_repos")), 
                    delta=str(github_contributions.get("contributions_this_year")) + " this year"
                )
            with col_2:
                st.metric("GitHub Contributions", "120+", delta="31 this year")
            with col_3:
                st.metric("Coffee Consumed", "100+", delta="20 this month")
        except Exception as e:
            with col_1:
                st.metric("Projects Completed", "N/A", delta="...")
            with col_2:
                st.metric("GitHub Contributions", "120+", delta="31 this year")
            with col_3:
                st.metric("Coffee Consumed", "100+", delta="20 this month")

# Call the fragment to display GitHub metrics
display_github_metrics()