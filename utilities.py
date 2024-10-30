from datetime import datetime, timedelta
import pandas as pd 
import streamlit as st
def load_csv(filepath, separator):
    try:
        
        df = pd.read_csv(filepath, sep=separator, on_bad_lines='skip')

        st.write("successfully loaded your dataframe")
        return df
    except Exception as e1:
        print("❌ error on your dataframe!")
        print(e1)
    pass
