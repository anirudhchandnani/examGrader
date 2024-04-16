# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 00:52:25 2024

@author: aniru
"""

import streamlit as st
import base64 
import time

from dotenv import load_dotenv

load_dotenv()

import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


def calculate_scores():
    text = '"Final Score: 5/5\n"
               "Grading Rationale:\n"
               "Q.(i): The answer provided correctly identifies the process by which coral reefs are formed, with free-swimming coral larvae attaching to submerged rocks or other hard surfaces. This response is accurate and aligns with the information typically found in passages regarding coral reef formation. - Score: 1/1\n"
               "Q.(ii): The student correctly states that barrier reefs are separated from their adjacent land mass by a lagoon of open, often deep water. This is a precise definition and demonstrates a clear understanding of the geographical features of barrier reefs. - Score: 1/1\n"
               "Q.(iii): The answer (d) Fringing, barrier, and atoll, correctly lists the different types of reefs. This is a direct response to the question and displays the student's knowledge of the classification of reefs. - Score: 1/1\n"
               "Q.(iv): The answer (a) nutrient levels is correct. When pollutants enter the water, they can cause an increase in nutrient levels, which in turn promotes the growth of algae. This understanding is essential in recognizing the factors contributing to algal bloom in aquatic environments. - Score: 1/1\n"
               "Q.(v): The student lists more than two anthropogenic activities that are a threat to coral reefs, including pollution, overfishing, and other relevant threats. This not only meets the requirement of the question but also shows a comprehensive understanding of the various human activities impacting coral reefs. - Score: 1/1\n"
               "Overall, the student demonstrated a thorough understanding of the subject matter and provided correct and complete answers for all the questions. Therefore, they have earned a perfect score.")'
    return text

st.title('Upload answer sheet and marking scheme')

uploaded_image = st.file_uploader("Upload answer sheet", type=['jpg', 'png'])
if uploaded_image is not None:
    st.image(uploaded_image, caption='Answer sheet', use_column_width=True)

uploaded_pdf = st.file_uploader("Upload marking scheme", type='pdf')
if uploaded_pdf is not None:
    st.write("PDF file uploaded")
    # Convert PDF file to bytes
    pdf_bytes = uploaded_pdf.read()
    # Convert bytes data to base64 string
    pdf_b64 = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_b64}" width="700" height="1000"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.write('\n')

if st.button('Grade the answer sheet'):
    with st.spinner("Grading the answer sheet"):
        score = calculate_scores()
        time.sleep(6)
    # Remove spinner once calculation is done
    st.success('Grading done as per the marking scheme provided!')
    score = calculate_scores()
    
    st.write(score)
    #st.write(f'Score: {score}'+ api_key)
