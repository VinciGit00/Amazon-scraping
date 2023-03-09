import streamlit as st
import requests
from Scraping import *
import pandas as pd

def graphics():
    st.write("# Amazon free web scraping tool")

    st.write("### Designed by Marco Vinciguerra")

    string = st.text_input("Enter an amazon link to scrape: (for example you can write https://www.amazon.it/s?k=headphones&__mk_it_IT=ÅMÅŽÕÑ&crid=1RGM8UT4RF3V5&sprefix=headphones%2Caps%2C118&ref=nb_sb_noss_1 )")

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

