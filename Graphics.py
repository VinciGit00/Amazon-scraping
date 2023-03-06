import streamlit as st
import requests
from Scraping import *
import pandas as pd

def graphics():
    st.write("# Amazon free web scraping tool")
    st.write("### Designed by Marco Vinciguerra")

    string = st.text_input("Enter an amazon link to scrape:")

    # Create a multi-choice menu
    options = ["Option 1", "Option 2", "Option 3"]
    selected_options = st.multiselect("Select options:", options)

    # Show the selected options
    st.write("You selected:", selected_options)

    if st.button("Run the scraping algorithm"):
        try:
            response = requests.get(string)
            if(string != "" and "amazon" in string and response.status_code == 200):
                st.write("Your link is: " + string)
                search_url = "https://www.amazon.com/s?k=bose&rh=n%3A12097479011&ref=nb_sb_noss"
                data = parse_listing(search_url)
                df = pd.DataFrame(data)
                print(df)
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

