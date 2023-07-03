import streamlit as st
from src.extraction import Extraction

st.set_page_config(layout="wide")

def main():
    df = Extraction.load_data()

    st.dataframe(df)
    
if __name__ == '__main__':
    main()