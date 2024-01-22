# Practical Applications in Machine Learning - Homework 0

The goal of this assignment is to demonstrate your programming skills and ability to build a simple application using the Streamlit library. As a machine learning (ML) practitioner, you are expected to have basic knowledge of programming, learning new programming languages, and making things work off-the-fly. You will build a basic user interface that walks users through an end-to-end ML pipeline for a case studies involving fundamental ML algorithms including regression, classification, clustering, and deep learning.

The <b>learning outcomes<b> for this assignment are to end an app using: 
* Text Elements
* Data elements
* Chart Elements
* Input Widgets
* Media Elements
* Layouts and Containers
* State Management

<b>Relevant Reading<b>: Chapter 2. End-to-End Machine Learning Project of Géron, Aurélien. Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow. " O'Reilly Media, Inc.", 2022.

<b>Group-work<b>: students will be assigned the groups and expected to complete the assignment together by splitting the work in front- and back-end tasks.

<b>End-to-End ML Pipeline<b>: Many ML projects are NOT used in production or NOT easily used by others including ML engineers interested in exploring prior ML models, testing their models on new datasets, and helping users explore ML models. To address this challenge, the goal of this assignment is to implement a front- and back-end ML project, to be used for future homework assignments. The hope is that the homework assignments help students fresh on programming skills, basic math skills, and ability to learn new concepts, and serves as an indication of your commitment to complete this course.

* <b>Due</b>:  Friday January 31, 2024 at 11:00PM 
* <b>What to turn in</b>: Submit responses on GitHub AutoGrader
* <b>Assignment Type</b>: Individual
* <b>Time Estimate</b>: 9 Hours
* <b>Join Github Classroom</b>: https://classroom.github.com/a/2Yp-ESOH

# Prerequisites

Install [Streamlit](https://streamlit.io/)
```
pip install streamlit     # Install streamlit
streamlit hello           # Test installation
```

Next, let's update the libraries. First, let's update `conda` itself:
```
conda update -c defaults -n base conda
```

And recreate the environment:
```
conda env create -f environment.yml
```

Install Assignment Code
```
git clone https://github.com/Cornell-Tech-PAML-Course-2024/homework0
```

# Repository file structure

* intro_to_streamlit.ipynb: Shows introductory examples of streamlit. 
* intro_to_streamlit.py: HW1 assignment template using streamlit for web application UI and workflow of activties. 
* pages/*.py files: Contains code to explore data, preprocess it and prepare it for ML. It includes checkpoints for the homework assignment.
* datasets: folder that conatins the dataset used for HW1 in 'housing/housing.csv'
* notebooks: contains example notebooks for HW0 and introductory examples
* images/: contains images for readme

# 1. Build End-to-End ML Pipeline

The first part of HW1 focuses on ‘Building an End-to-End ML Pipeline’ which consists of creating modules that perform the following tasks: exploring and visualizing the data to gain insights and preprocess and prepare data for machine learning algorithms.

Create a general ML template to be used for regression, classification, and clustering homework assignments including: 
1) Data exploration
2) Preprocessing
3) Train models
4) Evaluate models
5) Deploy ML application

3-5 will not be covered in this assignment.

## California Housing Dataset

Create useful visualizations for machine learning tasks. This assignment focuses on visualizing features from a dataset given some input .csv file (locally or in the cloud), the application is expected to read the input dataset. Use the pandas read_csv function to read in a local file. Use Streamlit layouts to provide multiple options for interacting with and understanding the dataset.

This assignment involves testing the end-to-end pipeline in a web application using a California Housing dataset from the textbook: Géron, Aurélien. Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow. O’Reilly Media, Inc., 2022 [[GitHub](https://github.com/ageron/handson-ml2)]. The dataset was capture from California census data in 1990 and contains the following features:
* longitude - longitudinal coordinate
* latitude - latitudinal coordinate
* housing_median_age - median age of district
* total_rooms - total number of rooms per district
* total_bedrooms - total number of bedrooms per district
* population - total population of district
* households - total number of households per district'
* median_income - median income
* ocean_proximity - distance from the ocean
* median_house_value - median house value

We will explore these features further in the remaining sections, including in Reflection questions.

## 1. Explore and visualize the data to gain insights. 

Data exploration is the process of inspecting datasets with statistical and visualization methods. This step helps identifying patterns and problems in the dataset, as well as deciding which model or algorithm to use in subsequent steps. Although sometimes researchers tend to spend more time on model architecture design and parameter tuning, the importance of data exploration should not be ignored. For example, if your data breaks the assumption of your model or your data contains errors, you will not be able to get the desired results from your perfect model. Without data exploration, you may even spend most of your time checking your model without realizing the problem in the dataset.

<b>Step 1<b>: Import relevant libraries 

Import the following libraries needed for the assignment including:
* Streamlit library: `import streamlit as st`
* Pandas library: `import pandas as pd`
* Plotly library: `import plotly.express as px`

<b>Step 2<b>: Import/Restore dataset 

Next, use the Streamlit library to upload a CSV dataset file with `st.file_uploader` which returns the path to the dataset on your computer. Then, read the CSV file using Pandas read_csv function e.g., pandas.read_csv(path_to_file) which returns a Pandas dataframe with the dataset stored in it.

You need to ensure the data of the dataset variable is preserved as you navigate between pages. To handle this, store the dataset dataframe as a session_state variable using ‘st.session_state`.

<b>Step 3<b>: Display dataset features

Display the dataset on the webpage using the `st.markdown` function.

<b>Step 4<b>: Display dataset in a table for inspection

Display the dataset on the webpage using the `st.dataframe` function.

<b>Step 5<b>: Visualize features in histogram chart

* Create a sidebar for users to select features to visualize for inspection with the `st.sidebar’ function. In the sidebar,
* Create a header titled ‘Create Histogram Plot’ with `st.sidebar.header`.
* Create a header titled ‘Specify Input Parameters’ with `st.sidebar.header`.
* Create a menu to select features for inspection on the X-axis of the histogram with `st.sidebar.selectbox`. 
* Create a variable called numeric_columns to parse data with numerical data with `numeric_columns = list(df.select_dtypes(['float','int']).columns)`. 
* Set options variable in the selectbox function call to numeric_columns.
* Use the helper function called ‘sidebar_filter’ to display features on the sidebar with sliders for users to filter the features for inspection.
* Plot the data in a histogram using Plotly `px.histogram`

## 2. Preprocessing data for input to machine learning algorithms.

Real-world datasets for machine learning (ML) are highly susceptible to missing, inconsistent, and noise. Applying ML algorithms on this noisy data would not give quality results as they would fail to identify patterns effectively. Thus data preprocessing is important to improve the overall data quality to ensure ML algorithms learn patterns in the dataset.

<b>Step 1<b>: Import relevant libraries 

Import the following libraries needed for the assignment including:
* Streamlit library: `import streamlit as st`
* Pandas library: `import pandas as pd`

<b>Step 2<b>: Import/Restore dataset 

Repeat Step 2 from Section 1.

<b>Step 3<b>: Display dataset features

Repeat Step 4 from Section 1.

<b>Step 4<b>: Summarize missing values or invalid values in the dataset i.e., Not a number (Nan values)

Use Pandas functions to compute: 
* Number of categories with missing values using isna(), any(), and sum().
* Average number of missing values per category using isna(), and sum().
* Total number of missing values using isna() and sum().

Summary of Pandas functions:
* isna() returns a boolean array that indicates a missing or Nan with 1; otherwise it returns 0.
* any() returns False when values in a dataframe are False, otherwise it returns True
* sum() returns the sum of values in a dataframe or Series

Display the summary of missing values using the Streamlit markdown function `st.markdown`.

<b>Step 5<b>: Summarize descriptive statistics in the dataset

Display the dataset on the webpage using the `st.dataframe` function.

Create a menu for selecting multiple features using `st.multiselect`. Options include numerical values in the dataset (use numeric_columns from Step 4 and Section 1).

Create a second menu for selecting multiple statistics in a list using `st.multiselect`. Options include: 
* Mean - compute feature average
* Median - compute feature median 
* Max - compute feature maximum
* Min - compute feature minimum

Use the selected features and selected statistics to write a function that computes those statistics with Pandas mean(), median(), max(), and min() functions. Round the statistics to the second decimal place using the `round()` function. Then, display the statistics using the Streamlit `st.write` function.

3. Train models 

None for this assignment.

4. Evaluate models 

None for this assignment.

5. Deploy application 

None for this assignment.

# 2. Technical Report

None for this assignment.

# Further Issues and questions ❓

If you have issues or questions, don't hesitate to contact the teaching team:

* Angelique Taylor (amt298@cornell.edu) - Instructor
* Tauhid Tanjim (tt485@cornell.edu) - Teaching Assistant
* Olga Acuna Leanos (oea9@cornell.edu) - Grader