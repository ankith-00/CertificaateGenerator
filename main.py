import streamlit as st 
from PIL import Image, ImageDraw, ImageFont
import os
import time

# LOADING CERTIFICATE IMAGE 
image = Image.open('src/certificateDemo.png')
draw = ImageDraw.Draw(image)



# FONT FAMILY SETTING 
font = ImageFont.truetype("src/InriaSans-Bold.ttf", size=50) 

# POSITION OF TEXT
position_1 = (1200, 550)  
position_2 = (415, 670) 
position_3 = (384, 889)


# CERTIFICATE GENERATOR 
def generateCertificate(candidateName, collageName, event):
    draw.text(position_1, candidateName, fill="black", font=font)
    draw.text(position_2, collageName, fill="black", font=font)
    draw.text(position_3, event, fill="black", font=font)
    image.save(f'{candidateName}.png')

# 
def delete_image_after_delay(image_path, delay_seconds):
    time.sleep(delay_seconds) 
    if os.path.exists(image_path):
        os.remove(image_path)  
    else:
        print("Image not found!")



# INNOVEX LOGO
imgCol1 , imgCol2 , imgCol3 = st.columns(3)
with imgCol2:
    st.image('src/innovexLogo.png' ,use_container_width=True)



msg = False


# INPUT FIELDS
event = st.selectbox(
    ' ',
    ("Quiz", "Gamming BGMI", "Gamming FF", "Coding and Debugging", "Short Movie Making", "12Hrs Hackathon", "Elocution" , "Startup Pitch" , "Mock Interview"),
    index=None,
    placeholder="Select Event",
)

candidateName = st.text_input(' ', placeholder='Name')
collageName = st.text_input(' ', placeholder='Collage Name')


# SUBMIT BUTTON
if st.button('Generate' ,use_container_width=True , type="primary"):
    generateCertificate(candidateName.upper(), collageName.upper(), event.upper())
    st.image(f'{candidateName}.png')

    delete_image_after_delay(f'{candidateName}.png', delay_seconds=5) 
