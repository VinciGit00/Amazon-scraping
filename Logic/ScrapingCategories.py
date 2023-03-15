from bs4 import BeautifulSoup
import requests

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