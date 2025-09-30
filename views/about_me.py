import streamlit as st
import time

# Utility functions

# small_desc = """
#     GCP Data Engineer with 4+ years of experience in designing, developing, and deploying data solutions on Google Cloud Platform.
# """

# def stream_data():
#     for word in small_desc.split(" "):
#         yield word + " "
#         time.sleep(0.01)


@st.dialog("Contact Me")
def contact_form():
    st.text_input("First Name")

col_1, col_2 = st.columns(2, gap = "small", vertical_alignment = "center")

with col_1:
    st.image("assets/profile_pic.jpeg", width=230)    

with col_2:
    st.title("Snehil Upadhyay", anchor=False)
    st.write("Data Engineer @EXL | Ex-Accenture | GCP")
    st.write("""
        GCP Data Engineer with 4+ years of experience in designing, developing, and deploying data solutions on Google Cloud Platform. 
    """)
    
    c_1, c_2 = st.columns([1,2], vertical_alignment="center")
    with c_1:
        st.badge("📍 Noida, India")
    with c_2:
        st.badge("✔️ Available for Opportunities", width = "stretch")

st.divider()

# Belive in Section

st.markdown('<h2 style="text-align: center;">What I Believe In</h2>', unsafe_allow_html=True)

beliefs = [
    {
        "icon": "⏰",
        "title": "Data-Driven Decisions",
        "desc": "I believe in letting data guide every decision, from architecture choices to business strategy."
    },
    {
        "icon": "🔔",
        "title": "Scalable Solutions",
        "desc": "Building systems that can grow with business needs while maintaining performance and reliability."
    },
    {
        "icon": "👥",
        "title": "Collaborative Innovation",
        "desc": "The best solutions come from diverse teams working together towards common goals."
    },
    {
        "icon": "📖",
        "title": "Continuous Learning",
        "desc": "Technology evolves rapidly, and I am committed to staying at the forefront of innovation."
    }
]

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
                                {belief['desc']}
                            </p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


st.divider()

# Key Achievements Section

st.markdown('<h2 style="text-align: center;">Key Achievements</h2>', unsafe_allow_html=True)

achievements = [
    {
        "icon": "🏆",
        "title": "Pinnacle Award",
        "desc": "High performer across the Delivery Unit (DU) – FY23"
    },
    {
        "icon": "🌟",
        "title": "Star of the Month",
        "desc": "Recognized across the Delivery Unit (DU) – July FY22"
    },
    {
        "icon": "🎖️",
        "title": "Leadership Recognitions",
        "desc": "25+ awards from Accenture Leadership, Business Stakeholders & Tech Architects."
    }
]

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
                        {ach['desc']}
                    </p>
                </div>
            </div>
            
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

with st.container(border=True):
    st.markdown('<h2 style="text-align: center;">Fun Facts About Me</h2>', unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3, gap="large", vertical_alignment="center")
    with col_1:
        st.metric("Projects Completed", "10", delta="2 this year")
    with col_2:
        st.metric("GitHub Contributions", "120+", delta="31 this year")
    with col_3:
        st.metric("Coffee Consumed", "100+", delta="20 this month")