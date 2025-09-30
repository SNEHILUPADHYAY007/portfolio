import streamlit as st

# Displaying the Search feature across all pages
prompt = st.text_input("Search for skills, projects, or experience:")
if prompt:  
    st.write(f"You entered: {prompt}")
# Page Setup

about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = "👤",
    default = True
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact Me",
    icon = "📞"
)

projects_page = st.Page(
    page = "views/projects.py",
    title = "Projects",
    icon = "📁"
)

skills_page = st.Page(
    page = "views/skills.py",
    title = "Skills",
    icon = "🛠️"
)

work_experience_page = st.Page(
    page = "views/work_experience.py", 
    title = "Work Experience",
    icon = "💼"
)

# Navigation Setup
pg = st.navigation(
    {
        "OVERVIEW": [about_page, skills_page],
        "WORK": [projects_page, work_experience_page],
        "CONNECT": [contact_page]
    }
)

# Logo and extra informations
st.logo("assets/logo.png", size="large")
container = st.sidebar.container(border=True)
with container:
    st.header("Quick Stats")
    st.write("Projects Completed: 10")
    st.write("Years of Experience: 5")
    st.write("Skills Acquired: 15")

st.sidebar.text("Made with ❤️ by Snehil")
# Running the Navigation
pg.run()

# Note: The actual content of each page is defined in their respective files in the views directory.


