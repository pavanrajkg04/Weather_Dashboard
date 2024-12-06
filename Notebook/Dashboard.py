import pandas as pd
import streamlit as st
import duckdb as ddb


conn = ddb.connect('../weatherdata')
print(conn)

conn.close()

