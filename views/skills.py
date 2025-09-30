import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

py_lottie_path = "./assets/lottie-logos/Python logo.json"
sql_lottie_path = "./assets/lottie-logos/SQL.json"
gcp_lottie_path = "./assets/lottie-logos/Google Logo.json"
db_lottie_path = "./assets/lottie-logos/database.json"
code_lottie_path = "./assets/lottie-logos/Coding.json"
scala_lottie_path = "./assets/lottie-logos/programming.json"
polars_lottie_path = "./assets/lottie-logos/Polars.json"
big_data_lottie_path = "./assets/lottie-logos/big_data.json"
cloud_lottie_path = "./assets/lottie-logos/Google_Cloud.json"
de_lottie_path = "./assets/lottie-logos/DE.json"
orch_lottie_path = "./assets/lottie-logos/Automation.json"
github_lottie_path = "./assets/lottie-logos/gitHub.json"
familiar_lottie_path = "./assets/lottie-logos/Checklist.json"

# SVG icons from Google Cloud (check current links)
BIGQUERY_PNG = './assets/google_logos/Bigquery.png'
STORAGE_PNG = './assets/google_logos/Storage.png'
COMPOSER_PNG = './assets/google_logos/Composer.png'
DATAPROC_PNG = './assets/google_logos/Dataproc.png'
CLOUD_FUNCTIONS_PNG = './assets/google_logos/CloudFunctions.png'
PUBSUB_PNG = './assets/google_logos/PubSub.png'
DEVOPS_PNG = './assets/google_logos/devops.png'
DATA_MODELLING_PNG = './assets/google_logos/data_modelling.png'
DATA_PIPELINE_PNG = './assets/google_logos/data_pipeline.png'
AIRFLOW_PNG = './assets/google_logos/Apache_Airflow.png'
GIT_PNG = './assets/google_logos/git.png'
GITHUB_PNG = './assets/google_logos/github.png'
LANGCHAIN_PNG = './assets/google_logos/langchain.png'
VERTEX_AI_PNG = './assets/google_logos/vertex-ai.png'
LLM_PNG = './assets/google_logos/llm.png'
PROMPT_PNG = './assets/google_logos/prompt.png' 
RAG_PNG = './assets/google_logos/rag.png'
STREAMLIT_PNG = './assets/google_logos/streamlit.png'


# File based Lottie loader
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

    
paths = [load_lottiefile(code_lottie_path), 
         load_lottiefile(big_data_lottie_path), 
         load_lottiefile(cloud_lottie_path), 
         load_lottiefile(de_lottie_path),
         load_lottiefile(orch_lottie_path),
         load_lottiefile(github_lottie_path),
         load_lottiefile(familiar_lottie_path)]

skills = {
    "Programming Languages" : [
        {"name": "Python", "level": "Expert", "lottie_url": load_lottiefile(py_lottie_path)},
        {"name": "SQL", "level": "Expert", "lottie_url": load_lottiefile(sql_lottie_path)},
        {"name": "Scala", "level": "Intermediate", "lottie_url": load_lottiefile(scala_lottie_path)},
        # {"name": "Data Engineering", "level": "Expert", "lottie_url": load_lottiefile(db_lottie_path)},
    ],
    "Big Data Technologies" : [
        {"name": "Apache Spark", "level": "Expert", "lottie_url": load_lottiefile(db_lottie_path)},
        {"name": "Polars", "level": "Intermediate", "lottie_url": load_lottiefile(polars_lottie_path)},
        # {"name": "", "level": "Intermediate", "lottie_url": load_lottiefile(code_lottie_path)},
    ],
    "Cloud Computing" : [
        {"name": "BigQuery", "level": "Expert", "lottie_url": BIGQUERY_PNG},
        {"name": "Composer", "level": "Intermediate", "lottie_url": COMPOSER_PNG},
        {"name": "Dataproc", "level": "Intermediate", "lottie_url": DATAPROC_PNG},
        {"name": "Cloud Functions", "level": "Intermediate", "lottie_url": CLOUD_FUNCTIONS_PNG},
        {"name": "Pub/Sub", "level": "Intermediate", "lottie_url": PUBSUB_PNG},
        {"name": "Cloud Storage", "level": "Intermediate", "lottie_url": STORAGE_PNG},
    ],
    "Data Engineering Tools" : [
        {"name": "Azure Devops", "level": "Expert", "lottie_url": DEVOPS_PNG},
        {"name": "Data Modelling", "level": "Intermediate", "lottie_url": DATA_MODELLING_PNG},
        {"name": "ETL/ELT Pipeline", "level": "Intermediate", "lottie_url": DATA_PIPELINE_PNG},
    ],
    "Workflow Orchestration" : [
        {"name": "Apache Airflow", "level": "Intermediate", "lottie_url": AIRFLOW_PNG},
    ],
    "Version Control" : [
        {"name": "Git", "level": "Expert", "lottie_url": GIT_PNG},
        {"name": "GitHub", "level": "Expert", "lottie_url": GITHUB_PNG},
    ],
    "Familiar With" : [
        {"name": "LangChain", "level": "Beginner", "lottie_url": LANGCHAIN_PNG},
        {"name": "VERTEX AI", "level": "Beginner", "lottie_url": VERTEX_AI_PNG},
        {"name": "LLM Models", "level": "Beginner", "lottie_url": LLM_PNG},
        {"name": "Prompt Engineering", "level": "Beginner", "lottie_url": PROMPT_PNG},
        {"name": "RAG", "level": "Beginner", "lottie_url": RAG_PNG},
        {"name": "Streamlit", "level": "Beginner", "lottie_url": STREAMLIT_PNG},
    ]
}
# Top Section
with st.container():
    st.markdown('<h2 style="text-align: center;">Skills & Technologies</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">A comprehensive overview of my technical expertise across data engineering, cloud platforms, and modern development practices</p>', unsafe_allow_html=True)
    

path_ind = 0

for key, value in skills.items():
    with st.container(border=True, gap="medium", height = "content"):
        o_1, o_2 = st.columns([0.1,0.9], vertical_alignment="top")
        with o_1:
            st.lottie(paths[path_ind], width=50, height=50)
        with o_2:
            st.subheader(key)
        cols = st.columns(3)
        for i, skill in enumerate(value):
            
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
                        if key in ["Cloud Computing", "Data Engineering Tools", "Workflow Orchestration", "Version Control", "Familiar With"]:
                            st.image(skill['lottie_url'])
                        else:
                            st_lottie(skill["lottie_url"], width=40, height=40)

    path_ind += 1
            
st.divider()

with st.container(border=True):
    st.markdown('<h2 style="text-align: center;">Current Learning Focus</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("AI/ML", anchor=False)
        st.write("Exploring AI/ML concepts and their applications")

    with col2:
        st.subheader("Certifications", anchor=False)
        st.write("Pursuing Google Cloud Professional Data Engineer certification")


        
