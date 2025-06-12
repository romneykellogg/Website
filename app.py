from pathlib import Path

import streamlit as st

from PIL import Image

# --- Path Settings ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Kellogg_Resume_2025.pdf"
profile_pic = current_dir / "assets" / "RomneyHeadshotPalmWalk1.jpg"
media_pic1 = current_dir / "assets" / "RomneyMedia1.jpg"
media_pic2 = current_dir / "assets" / "RomneyMedia2.jpg"

# --- General Settings ----

PAGE_TITLE = "Digital CV | Romney Kellogg"
PAGE_ICON = ":wave:"
EMAIL_ICON = ":email:"
NAME = "Romney Kellogg"
DESCRIPTION = " Recent PhD Graduate"

EMAIL = "romnkello@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/r-kellogg/",
}
PROJECTS = {
    ":desert_island: USTDA Fiji Project to Electrify 75 Rural Sites":"https://www.youtube.com/watch?v=P1Hva7hnrTw",
    # ":energy: Energy Exhibit ":"link",
    # ":wave: Haboob Simulator":"link",
    ":snake: Foldable Robotics-Snake Rectilinear Motion":"https://www.youtube.com/watch?v=gsyXnS8U5l4&t=175s",
    ":mag_right: TPI Composites Investigation":"https://www.youtube.com/watch?v=7bNRF8twaAA",
}
MEDIA = {
    "ASU and the USTDA - collaborating to provide energy and employment globally":"https://www.youtube.com/watch?v=P1Hva7hnrTw",
    "Empowering Minds and Energizing Communities":"https://leaps.asu.edu/2023/12/empowering-minds-and-energizing-communities/",
    "ASU News: Character first, robotics second":"https://news.asu.edu/20220510-character-first-robotics-second",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title("Hello there!")

# --- LoaD CSS, PDF & Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
media_pic1 = Image.open(media_pic1)
media_pic2 = Image.open(media_pic2)

# ---- Hero Section ---
col1, col2 =st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=":page_facing_up: Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL_ICON, EMAIL)

# ---- Social Media Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Education
st.write("#")
st.subheader("Education")
col1, col2 =st.columns(2, gap="small")
with col1:
    st.write("PhD Systems Engineering")
    st.write("MSE Robotics and Automated Systems")
    st.write("BSE Robotics Engineering ")
    st.write("Associate of Arts")

with col2:
    st.write("Arizona State University, AZ | 2025")
    st.write("Arizona State University, AZ | 2022")
    st.write("Arizona State University, AZ | 2021")
    st.write("Clark College, WA | 2015")
# # ---- Experience & Qualifications ---
# st.write("#")
# st.subheader("Experience & Qualifications")
# st.write(
#     """
#     - :heavy_check_mark: things
#     - :heavy_check_mark: things
#     - :heavy_check_mark: things
#     """
#
# )

# --- Skills
st.write("#")
st.subheader("Skills")
col1, col2 =st.columns(2, gap="small")
with col1:
    st.write(
    """
    -  MATLAB
    -  Python
    -  Data Analysis
    -  Excel
    -  PCB Design
    
    """

)
with col2:
    st.write(
        """
        -  Xendee
        -  SolidWorks (CSWA 2021)
        -  HAM Radio (KK7CUZ)
        -  Technical Writing
        -  B1 Spanish
        """

    )

# --- Project Experience ---
st.write("#")
st.subheader("Project Experience")
st.write("---")

# --- Project 1
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("USTDA Fiji Project to Electrify 75 Rural Sites")
with col2:
    st.write(" 2022 - Present ")
st.write(
    """
    - Led techno-economic and load profile creation subgroup                                                                                
    - Created Python code to run 75+ sites in batch optimization analysis with the Xendee API
    - Developed modeling methods that reduce load estimation analysis time by 80%
    - Designed and ran test scenarios to justify project assumptions
    - Co-authored 6 project reports relating to load demand
    - Managed 2 student workers on data analysis and python activities
    """
)

# --- Project 2
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("Energy Exhibit ")
with col2:
    st.write("2023")
st.write(
    """
    - Consulted with design students to demonstrate function of wind power and power plants                                                                                
    - Designed electrical system and user interface for 2 interactive systems
    - Reviewed and updated educational design to ensure appropriate representations of energy systems
    
    """
)

# --- Project 3
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("Haboob Simulator")
with col2:
    st.write("2022")
st.write(
    """
    - Designed and implemented an electrical system for a haboob simulator for a children’s museum                                                                                
    - Coded and tested the haboob simulator
    - Lead software design and development to include user interface

    """
)

# --- Project 4
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("Rectilinear Locomotion Robot ")
with col2:
    st.write("2020")
st.write(
    """
    - Designed and implemented an electrical system for a foldable robot                                                                                
    - Lead the software development for the control system

    """
)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- Job 1
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("ASU LEAPS Graduate Research Assistant ")
with col2:
    st.write(" 2022 - Present ")
st.write(
    """
    - Conducts research in energy system planning for off-grid systems globally                                                                                
    - Codes in MATLAB and Python to optimize large-scale energy control systems
    - Creates learning and training content on electricity and energy systems for all ages

    """
)

# --- Job 2
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("ASU LEAPS Research Assistant")
with col2:
    st.write(" 2019 - 2022 ")
st.write(
    """
    - Created workforce development content within the microgrid and energy field
    - Created K-12 content within the microgrid and energy field  
    - Provided consultation with microgrid testbeds for military applications
    - Tested and maintained large-scale energy assets 


    """
)

# --- Volunteer Experience
st.write("#")
st.subheader("Volunteer Experience")
st.write("---")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("FRC Team 6471 Mechanical Mentor ")
with col2:
    st.write(" 2021 - Present")
st.write(
    """
    - Mentors 20 high school students in engineering design, mechanical design, fabrication, manual and CNC machining
    """
)

# --- Projects
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Achievements:
st.write("#")
st.subheader("Achievements")
col1, col2 =st.columns(2, gap="small")
with col1:
    st.write("ASU LEAPS Scholarship Recipient")
    st.write("SCI4DI Nominee")
    st.write("Dean's Fellowship Recipient")
with col2:
    st.write("2025")
    st.write("2024")
    st.write("2022")
# --- Media
st.write("#")
st.subheader("Media")
st.write("---")
col1, col2 =st.columns(2, gap="small")
with col1:
    st.image(media_pic1, width=230)
with col2:
    st.image(media_pic2, width=230)
for project, link in MEDIA.items():
    st.write(f"[{project}]({link})")