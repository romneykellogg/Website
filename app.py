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

# ---- Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - :heavy_check_mark: things
    - :heavy_check_mark: things
    - :heavy_check_mark: things
    """

)

# --- Skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - :heavy_check_mark: things
    - :heavy_check_mark: things
    - :heavy_check_mark: things
    """

)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- Job 1
st.write("job name")
st.write(" 05/2020 - Present ")
st.write("---")

# --- Projects & Accomplishments
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Projects & Accomplishments
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