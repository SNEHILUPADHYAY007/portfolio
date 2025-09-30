import streamlit as st
import requests
import re

WEBHOOK_URL = ""


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Top Section
with st.container():
    st.markdown('<h2 style="text-align: center;">Get In Touch</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Let\'s discuss your next data engineering project</p>', unsafe_allow_html=True)

# Sample contact data
Contact = {
    "contact": [
        {
            "display-text": "Email Me",
            "contact-to": "snehilupadhyay007@gmail.com",
            "contact-type": "Email",
            "icon_url": "https://img.icons8.com/fluency/48/new-post.png",
        },
        {
            "display-text": "LinkedIn Profile",
            "contact-to": "https://www.linkedin.com/in/snehil-upadhyay-694099174/",
            "contact-type": "LinkedIn",
            "icon_url": "https://img.icons8.com/fluency/48/linkedin.png",
        },
        {
            "display-text": "Phone No.",
            "contact-to": "+91-9717001225",
            "contact-type": "Phone",
            "icon_url": "https://img.icons8.com/fluency/48/phone.png",
        }
    ]
}

# Render in 3 equal columns
cols = st.columns(len(Contact["contact"]), gap="large")

for idx, p in enumerate(Contact["contact"]):
    with cols[idx]:
        with st.container(border=True):
            
            if p["contact-type"].lower() == "email":
                link = f"mailto:{p['contact-to']}"
            elif p["contact-type"].lower() == "phone":
                link = f"tel:{p['contact-to']}"
            else:
                link = p["contact-to"]

            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 20px;">
                    <img src="{p['icon_url']}" width="40"><br>
                    <strong>{p['contact-type']}</strong><br>
                    <a href="{link}" target="_blank">{p['display-text']}</a>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

with st.container():
    st.markdown('<h2 style="text-align: center;">Send a Message</h2>', unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Your Name")
    email = st.text_input("Email", placeholder="Your Email")
    message = st.text_area("Message", placeholder="Your Message", height=150)
    submitted = st.form_submit_button("Send Message")
    if submitted:   
        if not WEBHOOK_URL:
            st.error("Email service is not set up. Please try again later.", icon="📧")
            st.stop()

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            st.success("Your message has been sent successfully! 🎉", icon="🚀")
        else:
            st.error("There was an error sending your message.", icon="😨")