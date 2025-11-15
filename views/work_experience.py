import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "work_experience_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

def render_gifs(URL):
    with open(URL, "rb") as f:
        return f.read()
    
@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name") 

# Top Section
with st.container():
    st.markdown(f'<h2 style="text-align: center;">{config["page_title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;">{config["page_subtitle"]}</p>', unsafe_allow_html=True)

# Load experience data with GIF content
experience_list = config["experience"]
gifs = config["gifs"]

for exp in experience_list:
    gif_key = exp["gif_key"]
    gif_path = gifs.get(gif_key)
    
    with st.container(border=True, gap="medium"):
        # col1, col2 = st.columns([1, 2], vertical_alignment="center")
        # 
        # with col1:
        #     if gif_path:
        #         st.image(render_gifs(gif_path))
        
        col2 = st.columns(1)[0]

        with col2:
            st.subheader(exp["organization"])
            st.write(exp["description"])
            
        # Horizontal badge row using HTML & CSS flexbox for full text and even spacing
        st.markdown(
            "<div style='display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 10px'>"
            + "".join(
                f"<span style='background:#e7f3ff;border-radius:8px;padding:6px 16px;margin:0;font-size:14px;font-weight:500;color:#3384d0;display:inline-block;'>{tech}</span>"
                for tech in exp["tech_stack"]
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
            # Download resume button
            with open(cta["resume_file"], "rb") as f:
                st.download_button(
                    label=cta["button_2_text"],
                    data=f,
                    file_name=cta["resume_filename"],
                    mime="application/pdf"
                )