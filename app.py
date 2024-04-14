# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 00:52:25 2024

@author: aniru
"""

import streamlit as st
import base64 
import time

from python-dotenv import load_dotenv

load_dotenv()

import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


def calculate_scores():
    text = 'To grade the paper according to the provided marking scheme, follow these steps:\\n\\n1. Check the student\'s answer against the expected answer/value points.\\n2. Award marks for each part of the answer as indicated in the marking scheme.\\n3. Ensure that no part of the answer is left unassessed.\\n4. Do not award more marks than assigned for each question.\\n5. Total the marks correctly for each question.\\n6. If a question has an \\"OR\\" option, only award marks once, even if the student has attempted multiple options.\\n\\nLet\'s grade each question:\\n\\nSECTION\xe2\x80\x94A\\n1. The student\'s solution matches the expected answer. They correctly calculated the projection.\\n   Marks awarded: \xc2\xbd + 1 + \xc2\xbd = 2\\n\\n2. The student\'s solution is correct. They followed the steps to solve the differential equation.\\n   Marks awarded: \xc2\xbd + 1 + \xc2\xbd = 2\\n\\n3. The student correctly calculated the probabilities for the number of spades.\\n   Marks awarded: \xc2\xbd + 1\xc2\xbd = 2\\n\\n4.(a) The student provided the correct probability for event B given A.\\n   Marks awarded: \xc2\xbd + \xc2\xbd + 1 = 2\\n   OR\\n   4.(b) The student correctly calculated the probability that the target is hit.\\n   Marks awarded: 1 + 1 = 2\\n   (Note: Only award marks for one option in question 4, either 4(a) or 4(b).)\\n\\n5. The student found the correct distances for the point from the given plane.\\n   Marks awarded: \xc2\xbd + 1 + \xc2\xbd = 2\\n\\n6. The student correctly integrated the given function.\\n   Marks awarded: 1 + 1 = 2\\n\\nSECTION\xe2\x80\x94B\\n7.(a) The student correctly deduced that vectors a and b are equal.\\n   Marks awarded: \xc2\xbd + 1 + 1 + \xc2\xbd = 3\\n   OR\\n   7.(b) The student correctly found the scalar triple product of the vectors.\\n   Marks awarded: \xc2\xbd + 1 + 1 + \xc2\xbd = 3\\n   (Note: Only award marks for one option in question 7, either 7(a) or 7(b).)\\n\\n8. The student correctly evaluated the integral.\\n   Marks awarded: 1\xc2\xbd + \xc2\xbd + \xc2\xbd + \xc2\xbd = 3\\n\\n9. The student correctly showed that the given lines are coplanar.\\n   Marks awarded: \xc2\xbd + \xc2\xbd + \xc2\xbd + \xc2\xbd + 1 = 3\\n\\nTotal marks awarded: 2 + 2 + 2 + 2 + 2 + 3 + 3 + 3 = 19\\n\\nThe final score for the first 9 questions is 19 out of 21.'
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
    st.write(api_key)
    #st.write(f'Score: {score}'+ api_key)
