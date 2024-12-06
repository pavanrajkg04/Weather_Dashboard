import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    st.title("Weather Data Dashboard")

    # File uploader
    uploaded_file = pd.read_excel('data_table.xlsx')

    if uploaded_file:
        # Load data
        data = uploaded_file

        # Display the dataframe
        st.subheader("Data Overview")
        st.write(data)

        # Select columns for filtering and visualization
        st.sidebar.header("Filter Options")
        regions = st.sidebar.multiselect(
            "Select Regions:", options=data["region"].unique(), default=data["region"].unique()
        )
        countries = st.sidebar.multiselect(
            "Select Countries:", options=data["country"].unique(), default=data["country"].unique()
        )

        # Apply filters
        filtered_data = data[(data["region"].isin(regions)) & (data["country"].isin(countries))]

        # Display filtered data
        st.subheader("Filtered Data")
        st.write(filtered_data)

        # Visualizations
        st.subheader("Visualizations")

        # Temperature distribution
        temp_fig = px.histogram(
            filtered_data, x="temp_c", nbins=20, title="Temperature Distribution (°C)"
        )
        st.plotly_chart(temp_fig)

        # Wind direction analysis
        wind_dir_fig = px.pie(
            filtered_data, names="wind_dir", title="Wind Direction Distribution"
        )
        st.plotly_chart(wind_dir_fig)

        # Scatter plot: Temperature vs Humidity
        scatter_fig = px.scatter(
            filtered_data, x="temp_c", y="humidity", color="region",
            title="Temperature vs Humidity"
        )
        st.plotly_chart(scatter_fig)

        # Map visualization (if lat/lon are available)
        if "lat" in filtered_data.columns and "lon" in filtered_data.columns:
            st.subheader("Geographical Map")
            map_fig = px.scatter_geo(
                filtered_data,
                lat="lat",
                lon="lon",
                hover_name="name",
                color="temp_c",
                title="Temperature by Location"
            )
            st.plotly_chart(map_fig)

    else:
        st.info("Please upload a Excel file to start.")

if __name__ == "__main__":
    main()