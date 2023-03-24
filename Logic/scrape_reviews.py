import json
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

custom_headers = {
    "accept-language": "en-GB,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

        
def scraping_review(link, limit):
    """
    Scraping from all the reviews
    """
    # initialize variables
    page_number = 1
    custom_headers = {'User-Agent': 'Mozilla/5.0'}

    # initialize dictionary
    data_dict = {'title_text': [], 'star_text': [], 'review_text': []}
    
    while  page_number<= int(limit):
        link_with_page = link + f"&pageNumber={page_number}"
        response = requests.get(link_with_page, headers=custom_headers)
        soup = BeautifulSoup(response.text, "html.parser")

        print(response.status_code)
        print(link_with_page)
        
        # find all review containers on page
        review_containers = soup.find_all('div', {'data-hook': 'review'})
        
        #if len(review_containers) == 0:
        #    print('Review con il primo metodo non disponibile')
        #    review_containers = soup.find('span', {'class': 'cr-original-review-content'})
        #else:
        print(review_containers) 

        title_containers = soup.find_all('span', {'data-hook': 'review-title'})
        if len(title_containers) == 0:
            print('Titolo con il primo metodo non disponibile')
            review_title = soup.find('a', {'data-hook': 'review-title'})
            if review_title:
                title_containers = review_title.find('span').text
                print(title_containers)
            else:
                print('Review title not found.')

        else:
            print(title_containers)

        star_containers = soup.find_all('i', {'data-hook': 'review-star-rating'})
        
        if len(star_containers) == 0:
            print('Numero di stelle con il primo metodo non disponibile')
            star_containers = soup.find_all('i', {'data-hook': 'cmps-review-star-rating'})

        else:
            print(star_containers)


        #print(len(review_containers))
        #print(len(title_containers))
        #print(len(star_containers))
        if title_containers is not None and star_containers is not None and review_containers is not None:
        # append values to dictionary
            for title, star, review in zip(title_containers, star_containers, review_containers):
                title_text = re.sub('<[^<]+?>', '', str(title))
                star_text = re.sub('<[^<]+?>', '', str(star))
                review_text = re.sub('<[^<]+?>', '', str(review))

                data_dict['title_text'].append(title_text)
                data_dict['star_text'].append(star_text)
                data_dict['review_text'].append(review_text)
                print("lunghezza del dizionario: "+str(len(data_dict)))
            # increment page number for next request
        page_number += 1

   
    # create dataframe
    df = pd.DataFrame.from_dict(data_dict)
    if not df.empty:
        df['review_text'] = df['review_text'].str.replace('\n', '')
        df['title_text'] = df['title_text'].str.replace('\n', '')
    print(df)
    return df

def getLink(link, limit):
    """
    Get the link from the button
    """
    response = requests.get(link, headers=custom_headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the <a> tag you're interested in
    # Find the <a> tag you're interested in
    link = soup.find('a', {'data-hook': 'see-all-reviews-link-foot'})

    # Get the value of the href attribute
    href_value = link['href']
    string = "https://amazon.com"+href_value
    print(string)
    return scraping_review(string, limit)

#getLink("https://www.amazon.it/12-regole-vita-antidoto-caos/dp/8863865825/ref=sr_1_1?crid=4FDIE8N0GFA7&keywords=12+regole+per+la+vita&qid=1678737099&sprefix=12+regole%2Caps%2C336&sr=8-1", 2)