import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from PIL import Image
import base64
import time

def download_button(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'
    return href

def parse_listing(url, num_items):
    data = {'name': [], 'url': [], 'price': [], 'rating': []}
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    for i in range(min(num_items, len(results))):
        result = results[i]
        try:
            name = result.find('h2').get_text().strip()
            url = "https://www.amazon.com" + result.find('a')['href']
            price = result.find('span', {'class': 'a-offscreen'}).get_text().strip()
            rating = result.find('span', {'class': 'a-icon-alt'}).get_text().strip()
            data['name'].append(name)
            data['url'].append(url)
            data['price'].append(price)
            data['rating'].append(rating)
        except AttributeError:
            continue
    return data


def graphics():
    st.write("# Amazon free web scraping tool")

    st.write("### Designed by Marco Vinciguerra")

    string = st.text_input("Enter an amazon link to scrape: (Look the following image to understand)")

    # Load image from a file
    image = Image.open("example.png")

    # Display the image in your app
    st.image(image, use_column_width=True)

    # Create a multi-choice menu
    options = ["1", "5", "10", "48", "all"]
    selected_option = st.radio("Select the number of items to scrape:", options)

    print(selected_option)

    if st.button("Run the scraping algorithm"):
        try:
            response = requests.get(string)
            if(string != "" and "amazon" in string):
                st.write("Your link is: " + string)
                data = parse_listing(string, int(selected_option))
                df = pd.DataFrame(data)
                print(df)
                st.write(df)
                st.markdown(download_button(df), unsafe_allow_html=True)
            else:
                st.write("url not valid")
        except requests.exceptions.MissingSchema as e:
             st.write(f"Invalid URL: {e}")
