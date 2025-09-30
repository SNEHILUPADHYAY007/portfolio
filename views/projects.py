import streamlit as st
from streamlit_lottie import st_lottie
import json


concurrency_lottie_path = "./assets/lottie-logos/concurrency.json"
ecommerce_lottie_path = "./assets/lottie-logos/ecommerce.json"
rocket_lottie_path = "./assets/lottie-logos/Rocket_launch.json"

GITHUB_PROFILE = "https://github.com/SNEHILUPADHYAY007"

# File based Lottie loader
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name") 

# Top Section
with st.container():
    st.markdown('<h2 style="text-align: center;">My Projects</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">A collection of projects where I experiment with new technologies and concepts.</p>', unsafe_allow_html=True)


Projects = {
    "Programming Languages" : [
        {"project_name": "ForceOfConcurrency", 
         "description": "This repository demonstrates the use of Python's threading module to fetch data concurrently from the Star Wars API (SWAPI). The primary goal of the project is to compare different concurrency techniques, such as and multithreading, to optimize data retrieval and storage.", 
         "link": "https://github.com/SNEHILUPADHYAY007/ForceOfConcurrency",
         "lottie_url": load_lottiefile(concurrency_lottie_path),
         "tech_stack": ["Python", "Threading", "API", "GIT", "GITHUB", "Jupyter Notebook"]},
         {"project_name": "E-Commerce Data Pipeline", 
         "description": "This repository contains a set of Jupyter notebooks designed to facilitate the analysis of e-commerce data. The project is structured to include data preparation, database management, and a main execution pipeline using tools such as Polars, PyODBC, and others.", 
         "link": "https://github.com/SNEHILUPADHYAY007/ecommerce-data-pipeline",
         "lottie_url": load_lottiefile(ecommerce_lottie_path),
         "tech_stack": ["Python", "OOPS", "Polars", "PyODBC", "SQL Server", "Data Modelling"]},
         {"project_name": "Rocket-Launch-Images-Airflow", 
         "description": "The Rocket Launch Project is an example of an Apache Airflow-based ETL (Extract, Transform, Load) pipeline designed to pull data from a public API, process the data, and store it locally. The project demonstrates how to use Airflow's powerful scheduling and data pipeline capabilities within a Docker containerized environment. ", 
         "link": "https://github.com/SNEHILUPADHYAY007/get-images-airflow",
         "lottie_url": load_lottiefile(rocket_lottie_path),
         "tech_stack": ["Python", "Airflow", "Docker"]}
    ]
}

for p in Projects.get("Programming Languages"):
    with st.container(border=True, gap="medium"):
        col1, col2 = st.columns([1, 2], vertical_alignment="center")

        with col1:
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

with st.container(border=True):
    st.markdown('<h2 style="text-align: center;">Want to Work Together?</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">I\'m always interested in new data engineering challenges and opportunities.</p>', unsafe_allow_html=True)

    col_1, col_2 = st.columns([0.5, 0.5], vertical_alignment="center")
    # Left column -> centered button
    with col_1:
        left, center, right = st.columns([1, 3, 1])   # center sub-col is wider so button looks nicely centered
        with center:
            # use a unique key so Streamlit doesn't complain on reruns
            if st.button("📩 Contact Me", key="contact_me", use_container_width=True):
                contact_form()

    # Right column -> centered link button
    with col_2:
        left, center, right = st.columns([1, 3, 1])
        with center:
            # st.link_button opens the URL — keep it Streamlit-native
            st.link_button("🔗 GitHub Profile", GITHUB_PROFILE)