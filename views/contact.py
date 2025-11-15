import streamlit as st
import requests
import re
import json
import os

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "contact_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

WEBHOOK_URL = config["webhook_url"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Top Section
with st.container():
    st.markdown(f'<h2 style="text-align: center;">{config["page_title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;">{config["page_subtitle"]}</p>', unsafe_allow_html=True)

# Render contact cards
contacts = config["contacts"]
cols = st.columns(len(contacts), gap="large")

for idx, contact in enumerate(contacts):
    with cols[idx]:
        with st.container(border=True):
            
            contact_type = contact["contact_type"]
            contact_value = contact["contact_value"]
            
            if contact_type.lower() == "email":
                link = f"mailto:{contact_value}"
            elif contact_type.lower() == "phone":
                link = f"tel:{contact_value}"
            else:
                link = contact_value

            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 20px;">
                    <img src="{contact['icon_url']}" width="40"><br>
                    <strong>{contact_type}</strong><br>
                    <a href="{link}" target="_blank">{contact['display_text']}</a>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# Contact Form Section
contact_form_config = config["contact_form"]
with st.container():
    st.markdown(f'<h2 style="text-align: center;">{contact_form_config["title"]}</h2>', unsafe_allow_html=True)

with st.form(contact_form_config["form_id"]):
    name = st.text_input("Name", placeholder=contact_form_config["placeholders"]["name"])
    email = st.text_input("Email", placeholder=contact_form_config["placeholders"]["email"])
    message = st.text_area("Message", placeholder=contact_form_config["placeholders"]["message"], height=150)
    submitted = st.form_submit_button(contact_form_config["submit_button_text"])
    
    if submitted:   
        errors = contact_form_config["validation_errors"]
        
        if not WEBHOOK_URL:
            st.error(errors["webhook_not_set"], icon="📧")
            st.stop()

        if not name:
            st.error(errors["no_name"], icon="🧑")
            st.stop()

        if not email:
            st.error(errors["no_email"], icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error(errors["invalid_email"], icon="📧")
            st.stop()

        if not message:
            st.error(errors["no_message"], icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            st.success(contact_form_config["success_message"], icon="🚀")
        else:
            st.error(contact_form_config["error_message"], icon="😨")