import streamlit as st
from streamlit_option_menu import option_menu
import json
import pandas as pd

# Sidebar menu
with st.sidebar:
    
    selected = option_menu(
        "Menu",
        ["Home", "Overview", "Visualization", "Explore"],
        icons=["house", "book", "bar-chart", "search"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#111"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#6c6c6c"},
            "nav-link-selected": {"background-color": "red"},
        },
       
    )
    st.logo("E://repos//Airbnb-Analysis//logoairbnb.png",size="large")
   

# Page content
if selected == "Home":
   
    st.markdown("<h1 style='color: red;'>AIRBNB ANALYSIS</h1>", unsafe_allow_html=True)   
        
    st.write("### Domain : Travel Industry, Property Management, and Tourism")
    st.write("### Technologies used : Python, Pandas, Plotly, Streamlit, MongoDB")
    st.write("### Overview : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and...")
    
    # Add an image
    #st.image("https://logos-world.net/wp-content/uploads/2020/11/Airbnb-Emblem.png", width=300)
    st.image("E://repos//Airbnb-Analysis//logo.jpg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    with open('airbnbdata.json', 'r') as file:
        data = json.load(file)

# Print the data
    df = pd.DataFrame(data)
    df.to_excel("data.xlsx",)

elif selected == "Overview":
    st.write("### Overview content goes here.")

elif selected == "Visualization":
    
# Open and read the JSON file

    dataFile = st.file_uploader("Upload the Image", type= ["xlsx"])
    if dataFile is not None:
        df = pd.DataFrame(dataFile)

    

elif selected == "Explore":
    st.write("### Explore content goes here.")