import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("CSV Data Visualizer")

# Create a file uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("Data Preview:")
    st.dataframe(df)

    # Select a column for the x-axis and y-axis
    x_axis = st.selectbox("Select X-axis Column", df.columns)
    y_axis = st.selectbox("Select Y-axis Column", df.columns)

    # Create a line chart
    if st.button("Generate Line Chart"):
        plt.figure(figsize=(10, 5))
        plt.plot(df[x_axis], df[y_axis], marker='o')
        plt.title(f'{y_axis} vs {x_axis}')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.grid()

        # Display the plot
        st.pyplot(plt)
