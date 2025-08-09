import streamlit as st
import pandas as pd
import numpy as np


st.checkbox('I agree I will not be offended at any cost')
st.title("Excel File Viewer 📊")

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls",])
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
if uploaded_file is not None:
    # Read file into DataFrame
    df = pd.read_excel(uploaded_file,header=0)
    rows_count=len(df)
    col_name = list(df.columns)

    st.subheader("Preview")
    st.dataframe(df)  # Interactive table


    with tab1:


                #---  **text** = bold ---
            st.write(f"**Columns:** {col_name}")
            st.write(f'**Total rows of data generated:** {rows_count}')

    with tab2:
                for x in col_name :
                    null_count = df[x].isnull().sum()
                    st.write(f'**Total null value in {x}**: {null_count}')
else:
    st.info("Please upload an Excel file to view.")
    st.write('Please select data to see further analysis')


if st.sidebar.button("Click me"):
    st.sidebar.write("Button clicked!")
else:
    st.sidebar.write("Waiting for click...")
