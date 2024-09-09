import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_icon="☠️",
    page_title="Pokemon Dashboard"
)

@st.cache_data
def load_data():
    file="Pokemon.csv"
    data=pd.read_csv(file)
    return data

def main():
    st.markdown('''
    <style>
        .stApp{
            background_color :#111;
        }
    </style>
    ''',unsafe_allow_html=True)
    st.image("hero_image1.jpg",use_column_width=True)
    with st.spinner("Loading Pokemon..."):
        df=load_data()
        st.snow()
    rows,columns=df.shape
    col_name=df.columns.tolist()

    c1,c2,c3=st.columns(3)
    c1.subheader(f"Total Rows: {rows}")
    c2.subheader(f"Total Column: {columns}")
    c3.subheader(f"Columns: {",".join(col_name)}")
    

if __name__=="__main__":
    main()


