import pandas as pd
import streamlit as st
import duckdb as ddb


conn = ddb.connect('../weatherdata')

data_table = conn.execute('''
                          select * from raw.DAILY_WEATHER_DATA
                          ''').fetch_df()

print(data_table.head)