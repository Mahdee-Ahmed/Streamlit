import streamlit as st
import pandas as pd

st.title("Excel File Viewer 📊")

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls",])

if uploaded_file is not None:
    # Read file into DataFrame
    df = pd.read_excel(uploaded_file)

    st.subheader("Preview")
    st.dataframe(df)  # Interactive table
else:
    st.info("Please upload an Excel file to view.")

