import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

custom_headers = {
    "accept-language": "en-GB,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

#Link for link analysis
def get_product_info(url):
    response = requests.get(url, headers=custom_headers)
    if response.status_code != 200:
        print("Error in getting webpage")
        exit(-1)
    
    #print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    title_element = soup.select_one("#productTitle")
    title = title_element.text.strip() if title_element else None

    price_element = soup.select_one("#a-price-whole")
    price = price_element.text if price_element else None

    rating_element = soup.select_one("#acrPopover")
    rating_text = rating_element.attrs.get("title") if rating_element else None
    rating = rating_text.replace("out of 5 stars", "") if rating_text else None

    image_element = soup.select_one("#landingImage")
    image = image_element.attrs.get("src") if image_element else None

    description_element = soup.select_one("#productDescription")
    description = description_element.text.strip() if description_element else None

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.select_one('span.a-price-whole').text

    # Print the extracted price
    print(price)

    print()
    return {
        "title": title,
        "price": price,
        "rating": rating,
        "image": image,
        "description": description,
        "url": url,
    }

#Takes all the links
def parse_listing(listing_url, n_iterations):

    response = requests.get(listing_url, headers=custom_headers)
    soup_search = BeautifulSoup(response.text, "lxml")
    link_elements = soup_search.select("[data-asin] h2 a")
    page_data = []
    count = 0
    for link in link_elements:
        if count == int(n_iterations):
            break
        full_url = urljoin(listing_url, link.attrs.get("href"))
        print(f"Scraping product from {full_url[:100]}", flush=True)
        product_info = get_product_info(full_url)
        page_data.append(product_info)
        count = count + 1
    return page_data
