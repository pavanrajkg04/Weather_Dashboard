import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime 

def main():
    st.title("Bengaluru Weather Dashboard")
    data = pd.read_excel('PK')
    st.write(datetime.now())
    st.write("Latitute : ",round(data['lat'].iloc[-1],2), 'Longitute : ',round(data['lon'].iloc[-1],2))
    st.line_chart(data=data,x='localtime',y='temp_c',x_label='Date',y_label='Temp C',color='#ffaa00',width=300,height=500,use_container_width=True)


main()