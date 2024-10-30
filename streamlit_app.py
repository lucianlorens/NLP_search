import streamlit as st
import pandas as pd
import numpy as np


# personal libraries
import search_engine as se
import voice_recognition as vr
import utilities as utilities

# Environmental vars
import os 
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

st.title('NLP Search Engine')
st.subheader('Your voice is my command.')

#-----------------

# TODO: insert interface for loading data or use one example
separator = st.text_input("insert the character of your separator", max_chars = 1)
raw_df = st.file_uploader("upload your .csv file, ")
df = utilities.load_csv(raw_df, separator)

#TODO: make interface to choose the column you want to search:
column_name = st.text_input("type the exact name of the column you want to search")

#TODO: make the column a dropdown menu
### -------------------

if st.button("Voice Search"):
    query = vr.get_speech_input()
else:
    query = st.text_input("or type here the most likely terms of your dataset.")
### =========================================


# show results
if query:
    try:
        with st.spinner("O_O searching..."):
            relevant_datapoints = se.search_dataset(query, df, column_name) #change to news_df if you want to see everything
        
        st.write("Most relevant content:")
        for index, row in relevant_datapoints.iterrows():
            #st.write(f"**Palavras chaves**: {row['keywords']}")
            st.write(f"**Similarity Rate**: {row['similarity']:.4f}")
            st.write("---")

    except Exception as e:
        st.error("❌ Sorry, I had an error with your search. Can you try again please?")
        print("There was an error with the search T_T")
        print(e)

if query:
    st.subheader("Most similar data points:")

    col1, col2 = st.columns(2)

    with col1:
        
        st.write(relevant_datapoints[0])

        st.write(relevant_datapoints[1])

    with col2:
        st.write(relevant_datapoints[2])

        st.write(relevant_datapoints[4])
