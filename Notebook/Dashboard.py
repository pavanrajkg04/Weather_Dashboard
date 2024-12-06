import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# @st.cache_data
# def load_data(file):
#     df = pd.read_csv(file)
#     return df




def display_cards(data):
    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    # Card content for column 1
    with col1:
        card_html_1 = f"""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; margin: 10px; width: 100%; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 18px; color: #555;">Temperature (c) : {round(data['temp_c'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">UV index : {round(data['uv'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">Heat Index (c): {round(data['heatindex_c'].iloc[-1],2)}</p>
        </div>
        """
        st.markdown(card_html_1, unsafe_allow_html=True)

    # Card content for column 2
    with col2:
        card_html_2 = f"""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; margin: 10px; width: 100%; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 18px; color: #555;">Temperature: {round(data['temp_c'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">Humidity: {round(data['humidity'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">Wind speed Kph: {round(data['wind_kph'].iloc[-1],2)}</p>
        </div>
        """
        st.markdown(card_html_2, unsafe_allow_html=True)

    # Card content for column 3
    with col3:
        card_html_3 = f"""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; margin: 10px; width: 100%; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 18px; color: #555;">Temperature: {round(data['temp_c'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">Humidity: {round(data['humidity'].iloc[-1],2)}</p>
            <p style="font-size: 18px; color: #555;">Wind speed Kph: {round(data['wind_kph'].iloc[-1],2)}</p>
        </div>
        """
        st.markdown(card_html_3, unsafe_allow_html=True)


def main():
    st.title("Bengaluru Weather Dashboard")
    
    # file = "data_table.xlsx"
    # data = load_data(file)

    # Load the data
    data_url = 'data_table.xlsx'
    data = pd.read_excel(data_url)

    # Show current time and weather information
    st.write("Current Time: ", datetime.now())
    st.write("Latitude: ", round(data['lat'].iloc[-1], 2), 'Longitude: ', round(data['lon'].iloc[-1], 2))
    display_cards(data)
    

    # Line chart of temperature over time
    st.line_chart(data=data, x='localtime', y='temp_c', width=100,height=200,)

# Main Streamlit app execution
while True:
        main()
        time.sleep(100)
        st.rerun()
        
        
