import streamlit as st
from streamlit_lottie import st_lottie
import json

accenture_gif = "./assets/GIFS/accenture.gif"
exl_gif = "./assets/GIFS/exl.gif"

def render_gifs(URL):
    with open(URL, "rb") as f:
        return f.read()
    
@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name") 

# Top Section
with st.container():
    st.markdown('<h2 style="text-align: center;">Work Experience</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">My Professional journey in Data Engineering</p>', unsafe_allow_html=True)

    
Experience = {
    "experience" : [
        {
            "organization": "EXL - Healthcare Analytics", 
            "description": "Data Engineer specializing in Python automation for complex data extraction and standardization, transforming disparate Excel rosters into structured, analysis-ready formats to drive efficient downstream workflows.", 
            "gif_url": render_gifs(exl_gif),
            "tech_stack": ["Python", "Pandas", "Openpyxl", "Prompt Engineering", "GCP"]
        },
        {
             "organization": "Accenture - CIO(Marketing Analytics)", 
            "description": "Senior Data Engineer at Accenture building optimized data platforms on GCP. Expertise in pipeline orchestration (Airflow), performance optimization (Polars), and applying GENAI (Vertex AI) to solve complex data challenges.",
            "gif_url": render_gifs(accenture_gif),
            "tech_stack": ["Data Engineering", "Apache Spark", "GCP", "ELT", "Apache Airflow", "SQL"]
        }
         
    ]
}
    

for p in Experience.get("experience"):
    with st.container(border=True, gap="medium"):
        col1, col2 = st.columns([1, 2], vertical_alignment="center")

        with col1:
            st.image(p["gif_url"])

        with col2:
            st.subheader(p["organization"])
            st.write(p["description"])
            # st.link_button("🔗 View Project")
            
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

with st.container(border=True):
    st.markdown('<h2 style="text-align: center;">Ready for New Opportunities</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">I\'m passionate about solving complex data challenges and building scalable systems.</p>', unsafe_allow_html=True)

    col_1, col_2 = st.columns([0.5, 0.5], vertical_alignment="center")
    # Left column -> centered button
    with col_1:
        left, center, right = st.columns([1, 3, 1])   # center sub-col is wider so button looks nicely centered
        with center:
            # use a unique key so Streamlit doesn't complain on reruns
            if st.button("📩 Get in Touch", key="contact_me", use_container_width=True):
                contact_form()

    # Right column -> centered link button
    with col_2:
        left, center, right = st.columns([1, 3, 1])
        with center:
            # st.link_button opens the URL — keep it Streamlit-native
            
            with open("./assets/Resume/Snehil_Upadhyay_Resume.pdf", "rb") as f:
                st.download_button(
                    label="⬇️ Download Resume",
                    data=f,
                    file_name="Snehil_Upadhyay_Resume.pdf",
                    mime="application/pdf"
                )