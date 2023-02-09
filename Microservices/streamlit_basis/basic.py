# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title('Uber pickups in NYC')

# Define constants
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Define a function to load and process the data
@st.cache
def load_data(nrows):
    # Load the data using pandas
    data = pd.read_csv(DATA_URL, nrows=nrows)
    
    # Convert column names to lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    
    # Convert date/time column to datetime data type
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data

# Display a text widget to indicate that data is being loaded
data_load_state = st.text('Loading data...')

# Load the data
data = load_data(10000)

# Update the text widget to indicate that data has been loaded
data_load_state.text("Done! (using st.cache)")

# Add a checkbox to allow the user to display raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Calculate and display the number of pickups by hour
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Add a slider to allow the user to filter the data by hour
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# The last two lines were unclear, I ask more details to ChatGPT:
"""give further details for # Add a slider to allow the user to filter the data by hour
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
The code creates a slider widget that allows the user to filter the data by hour. The st.slider function creates the slider with the following parameters:

'hour' is the label for the slider.
0 is the minimum value that the slider can have.
23 is the maximum value that the slider can have.
17 is the default value of the slider.
The value of the slider is stored in the hour_to_filter variable.

The filtered_data variable holds the data that corresponds to the selected hour. It is created by using boolean indexing on the data dataframe, with the condition data[DATE_COLUMN].dt.hour == hour_to_filter. This condition filters the data to include only the rows where the value of the DATE_COLUMN (which has been converted to a datetime data type) is equal to the selected hour.
"""
# Display a map of all pickups at the selected hour
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
