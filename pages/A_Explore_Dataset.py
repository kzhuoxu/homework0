import streamlit as st                  
import pandas as pd
import plotly.express as px

#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 0 - Introduction to Streamlit")

#############################################

st.markdown('# Explore Dataset')

###################### FETCH DATASET #######################

# Dataset upload
st.markdown('### Read Dataset')
col1, col2 = st.columns([1, 1])

with(col1):
    data = st.file_uploader("Choose a file")
    if data:
        col1.line_chart(data['longitude'])
    else:
        data = pd.read_csv('.././datasets/housing_paml.csv')
with(col2):
    url = st.text_input('Enter URL')
    st.write('You entered: '+url)

###################### EXPLORE DATASET #######################

st.markdown('### Explore Dataset')

# Restore dataset if already in memory

# Display feature names and descriptions 
st.write('Features of the dataset: ', data.columns)

# Display dataframe as table
st.dataframe(data)

#X = df

###################### VISUALIZE DATASET #######################

# Collect user plot selection

# Specify Input Parameters

# Plot Histogram

# Create a sidebar for users to select features to visualize for inspection with the `st.sidebar’ function. In the sidebar,
with st.sidebar:
    st.sidebar.header('Create Histogram Plot')
    st.sidebar.header('Specify Input Parameters')
    numeric_columns = list(data.select_dtypes(['float','int']).columns)
    x_axis = st.sidebar.selectbox(
        'What features you would like to visualize?',
        numeric_columns)
    values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)
    filtered_data = 

def sidebar_filter(data, x_axis, values):
    filtered_data = data[x_axis]

    

# Create a header titled ‘Create Histogram Plot’ with st.sidebar.header.
# Create a header titled ‘Specify Input Parameters’ with st.sidebar.header.
# Create a menu to select features for inspection on the X-axis of the histogram with st.sidebar.selectbox.
# Create a variable called numeric_columns to parse data with numerical data with numeric_columns = list(df.select_dtypes(['float','int']).columns).
# Set options variable in the selectbox function call to numeric_columns.
# Use the helper function called ‘sidebar_filter’ to display features on the sidebar with sliders for users to filter the features for inspection.
# Plot the data in a histogram using Plotly px.histogram