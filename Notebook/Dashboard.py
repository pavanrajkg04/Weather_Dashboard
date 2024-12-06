import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

def main():
    st.title("Bengaluru Weather Dashboard")

    # Load the data
    data_url = 'https://raw.githubusercontent.com/pavanrajkg04/Weather_Dashboard/main/Notebook/data_table.xlsx'
    data = pd.read_excel(data_url)

    # Show current time and weather information
    st.write("Current Time: ", datetime.now())
    st.write("Latitude: ", round(data['lat'].iloc[-1], 2), 'Longitude: ', round(data['lon'].iloc[-1], 2))

    # Line chart of temperature over time
    st.line_chart(data=data, x='localtime', y='temp_c', use_container_width=True)

# Main Streamlit app execution
if __name__ == '__main__':
    main()

