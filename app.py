# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv() # take enviroment variable from .env.

import streamlit as st
import os

## Function to load OpenAI model and get response

def get_openai_reponse(question):
    llm = OpenAI(openai_api_key = os.getenv('OPEN_API_KEY'),model_name = "gpt-3.5-turbo-instruct",temperature = 0.5)
    response = llm(question)
    return response

## Initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input:", key="input")
response = get_openai_reponse(input)

sumbit = st.button("Ask the Question")

# If ask button click 
if sumbit:
    st.subheader("The Response is")
    st.write(response)