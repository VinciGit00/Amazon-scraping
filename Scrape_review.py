import streamlit as st
from PIL import Image
from download import *
import requests
import pandas as pd
from Home import *

def scraping_page():
    
    if st.sidebar.button("Scraping the category"):
        HomePage()

    st.write("# Scraping the reviews")

    string = st.text_input("Enter an amazon link to scrape: (Look the following image to understand)")
    # Load image from a file
    image = Image.open("12_rules.png")

    # Display the image in your app
    st.image(image, use_column_width=True)

 # Create a multi-choice menu
    options = ["1", "5", "10", "48", "all"]
    selected_option = st.radio("Select the number of items to scrape:", options)

    print(selected_option)

    if st.button("Run the scraping algorithm"):
        try:
           print("TODO")
           '''
            response = requests.get(string)
            if(string != "" and "amazon" in string):
              
                st.write("Your link is: " + string)
                data = parse_listing(string, int(selected_option))
                df = pd.DataFrame(data)
                print(df)
                st.write(df)
                st.markdown(download_button(df), unsafe_allow_html=True)
            else:
                st.write("url not valid")'''
        except requests.exceptions.MissingSchema as e:
            st.write(f"Invalid URL: {e}")