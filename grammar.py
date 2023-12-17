import streamlit as st
import google.generativeai as genai
from api import api

# Configure the API key
genai.configure(api_key=api)

defaults = {
    "model": "models/text-bison-001",
    "temperature": 0.4,
    "candidate_count": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 1024,
    "stop_sequences": [],
    "safety_settings": [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": "BLOCK_LOW_AND_ABOVE"},
        {"category": "HARM_CATEGORY_TOXICITY", "threshold": "BLOCK_LOW_AND_ABOVE"},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ],
}

# Set page title and description
st.set_page_config(page_title="Grammar Rewriter", page_icon="✍️", layout="wide")

# Set a custom background color for the entire app
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Center the title using Markdown and HTML
st.markdown(
    "<h1 style='text-align: center; color: #1f4d80;'>Grammar Rewriter</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h5 style='text-align: center; color: #1f4d80;'>Enter a sentence, and I'll help you rewrite it with improved grammar.</h5>",
    unsafe_allow_html=True,
)
# st.write("Enter a sentence, and I'll help you rewrite it with improved grammar.")

# Input text area
prompt = st.text_area("Enter your sentence:")

# Button to generate the rephrased sentence
if st.button("Generate"):
    with st.spinner("Generating..."):
        response = genai.generate_text(
            **defaults,
            # prompt=(
            #     f"Based on this sentence, check for grammar errors in each word. Provide a detailed explanation of each grammar error, fix the issues, and rewrite the new corrected sentence. Original Sentence: {prompt}"
            # ),

            prompt=(
                f"Identify and explain any grammar errors in the following sentence: '{prompt}'. Provide corrections and explanations for each identified error."
            ),
        )
    st.subheader("Rephrased Sentence:")
    st.write(response.result)
