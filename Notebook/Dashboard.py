import pandas as pd
import streamlit as st
import duckdb as ddb


conn = ddb.connect('GitHub\Weather_Dashboard\weatherdata')
print(conn)

conn.close()

