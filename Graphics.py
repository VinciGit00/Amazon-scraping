import streamlit as st
import requests
from Scraping import *
import pandas as pd
from PIL import Image
import base64

def download_button(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'
    return href

def graphics():
    st.write("# Amazon free web scraping tool")

    st.write("### Designed by Marco Vinciguerra")

    string = st.text_input("Enter an amazon link to scrape: (Look the following image to understand)")

    # Load image from a file
    image = Image.open("example.png")

    # Display the image in your app
    st.image(image, use_column_width=True)

    # Create a multi-choice menu
    options = ["1", "5", "10", "all"]
    selected_option = st.radio("Select the number of page to scrape:", options)

    print(selected_option)

    if st.button("Run the scraping algorithm"):
        try:
            response = requests.get(string)
            if(string != "" and "amazon" in string):
                st.write("Your link is: " + string)
                #search_url = "https://www.amazon.com/s?k=bose&rh=n%3A12097479011&ref=nb_sb_noss"
                data = parse_listing(string, selected_option)
                df = pd.DataFrame(data)
                print(df)
                #df = df.drop(['price'], axis=1)
                st.write(df)
                st.markdown(download_button(df), unsafe_allow_html=True)
            else:
                st.write("url not valid")
        except requests.exceptions.MissingSchema as e:
             st.write(f"Invalid URL: {e}")
        except requests.exceptions.HTTPError as e:
            st.write(f"The server returned an HTTP error: {e}")
        except requests.exceptions.RequestException as e:
             st.write(f"There was an error while making the request: {e}")
        except Exception as e:
            # handle any type of exception here
            st.write(f"An error occurred: {e}")

