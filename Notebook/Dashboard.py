import streamlit as st
import pandas as pd

# URL of the raw data file in GitHub repository
github_raw_url = 'https://raw.githubusercontent.com/username/repository/branch/path/to/your/file.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(github_raw_url)

# Display the DataFrame in Streamlit
st.title('Data from GitHub')
st.write(df)
