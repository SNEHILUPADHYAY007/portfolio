import streamlit as st
import json
import os
from utils import get_github_stats, get_total_skills

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "config", "app_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Displaying the Search feature across all pages
prompt = st.text_input(config["app"]["search_placeholder"])
if prompt:  
    st.write(f"You entered: {prompt}")

# Page Setup - Load pages from config
app_config = config["navigation"]
pages_config = app_config["pages"]
pages_by_id = {page["id"]: page for page in pages_config}

# Create Page objects dynamically from config
page_objects = {}
for page_config in pages_config:
    page_objects[page_config["id"]] = st.Page(
        page=page_config["page_file"],
        title=page_config["title"],
        icon=page_config["icon"],
        default=page_config.get("default", False)
    )

# Build navigation structure from config
navigation_dict = {}
for section, page_ids in app_config["structure"].items():
    navigation_dict[section] = [page_objects[page_id] for page_id in page_ids]

# Navigation Setup
pg = st.navigation(navigation_dict)

# Logo and extra informations
app_conf = config["app"]
st.logo(app_conf["logo"], size=app_conf["logo_size"])

# Sidebar configuration from config with dynamic values
sidebar_conf = config["sidebar"]
container = st.sidebar.container(border=True)
with container:
    st.header(sidebar_conf["header"])
    
    try:
        # Get dynamic values
        github_stats = get_github_stats()
        total_skills = get_total_skills()
        
        # Display stats with dynamic values
        st.write(f"Projects Completed: {github_stats.get('total_repos')}")
        st.write(f"Years of Experience: 5")
        st.write(f"Skills Acquired: {total_skills}")
    except Exception as e:
        # Fallback to config values if dynamic fetch fails
        for stat in sidebar_conf["stats"]:
            st.write(f"{stat['label']}: {stat['value']}")

st.sidebar.text(sidebar_conf["footer"])
# Running the Navigation
pg.run()

# Note: The actual content of each page is defined in their respective files in the views directory.


