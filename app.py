import pathlib
import textwrap
import google.generativeai as genai 

from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st 
from PIL import Image

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))



# function to load gemini pro
def get_gemini_response(input, image, prompt):
    #loading the model 
    model = genai.GenerativeModel('gemini-vision-pro')
    response = model.generate_content([input, image[0], prompt])
    return response.text



# image upload setup
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # read the file
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                'mime_type': uploaded_file.type, 
                'data': bytes_data
            }
        ]
        return image_parts
    else:
        raise ERROR("No file uploaded")
    
    



# initalize the streamlit applicatiion
st.set_page_config(page_title = "Invoice Extractor")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input" )
uploaded_file = st.file_uploader("choose an image", type={"jpg", "jpeg", "png"})
image= ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption= "Uploaded file", use_column_width = True)
submit = st.button("Tell me about the invoice")

input_prompt = """
You are expert in understanding the invoices,
you will receive an input images as invoices and you will understand what is in the image and answer the question asked by the user. 
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Response is")
    st.write(response)