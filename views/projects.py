import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "projects_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# File based Lottie loader
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name") 

# Top Section
with st.container():
    st.markdown(f'<h2 style="text-align: center;">{config["page_title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;">{config["page_subtitle"]}</p>', unsafe_allow_html=True)

# Load projects and their lottie animations
projects = []
for project in config["projects"]:
    lottie_key = project["lottie_key"]
    lottie_path = config["lottie_animations"].get(lottie_key)
    if lottie_path:
        try:
            lottie_data = load_lottiefile(lottie_path)
            project["lottie_url"] = lottie_data
        except:
            project["lottie_url"] = None
    projects.append(project)

for p in projects:
    with st.container(border=True, gap="medium"):
        col1, col2 = st.columns([1, 2], vertical_alignment="center")

        with col1:
            if p.get("lottie_url"):
                st_lottie(p["lottie_url"], height=180)

        with col2:
            st.subheader(p["project_name"])
            st.write(p["description"])
            st.link_button("🔗 View Project", p["link"])
            
        # Horizontal badge row using HTML & CSS flexbox for full text and even spacing
        st.markdown(
            "<div style='display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 10px'>"
            + "".join(
                f"<span style='background:#e7f3ff;border-radius:8px;padding:6px 16px;margin:0;font-size:14px;font-weight:500;color:#3384d0;display:inline-block;'>{tech}</span>"
                for tech in p["tech_stack"]
            )
            + "</div>", 
            unsafe_allow_html=True
        )

st.divider()

cta = config["cta_section"]
with st.container(border=True):
    st.markdown(f'<h2 style="text-align: center;">{cta["heading"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;">{cta["subheading"]}</p>', unsafe_allow_html=True)

    col_1, col_2 = st.columns([0.5, 0.5], vertical_alignment="center")
    # Left column -> centered button
    with col_1:
        left, center, right = st.columns([1, 3, 1])   # center sub-col is wider so button looks nicely centered
        with center:
            # use a unique key so Streamlit doesn't complain on reruns
            if st.button(cta["button_1_text"], key="contact_me", use_container_width=True):
                contact_form()

    # Right column -> centered link button
    with col_2:
        left, center, right = st.columns([1, 3, 1])
        with center:
            # st.link_button opens the URL — keep it Streamlit-native
            st.link_button(cta["button_2_text"], config["github_profile"])