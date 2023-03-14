import json
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

custom_headers = {
    "accept-language": "en-GB,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}


def scraping_from_principal_page(link, limit):
    """
    Scraping from the product page
    """
    response = requests.get(link, headers=custom_headers)
    soup = BeautifulSoup(response.text, "html.parser")

    review_containers = soup.find_all('div', {'data-hook': 'review-collapsed'})[:limit]
    #print(review_containers)
    
    title_containers = soup.find_all('a', {'data-hook': 'review-title'})[:limit]
    #print(title_containers)
    
    star_containers =   soup.find_all('i', {'data-hook': 'review-star-rating'})[:limit]
    #print(star_containers)
    
    data_dict = {}
    count = 1
    for title, star, review in zip(title_containers, star_containers, review_containers):
        title_text = re.sub('<[^<]+?>', '', str(title))
        star_text = re.sub('<[^<]+?>', '', str(star))
        review_text = re.sub('<[^<]+?>', '', str(review))
        
        print(review_text)
     

        data_dict["elem "+str(count)] = {
            "title":title_text.strip(),
            "star":star_text.strip(),
            "review":review_text.strip(),
        }
        count +=1

    print(json.dumps(data_dict, indent=4, ensure_ascii=False))
    
    mapdictionary(data_dict)

def scraping_review(link, limit):
    """
    Scraping from all the reviews
    """
    data_dict = {}
    count = 1
    page_number = 1

    while True:
        # construct URL with page number
        link_with_page = link + f"&pageNumber={page_number}"
        response = requests.get(link_with_page, headers=custom_headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # find all review containers on page
        review_containers = soup.find_all('span', {'data-hook': 'review-body'})[:limit]

        # if there are no more reviews on the page, break the loop
        if not review_containers:
            break

        title_containers = soup.find_all('a', {'data-hook': 'review-title'})[:limit]
        star_containers = soup.find_all('i', {'data-hook': 'review-star-rating'})[:limit]

        for title, star, review in zip(title_containers, star_containers, review_containers):
            title_text = re.sub('<[^<]+?>', '', str(title))
            star_text = re.sub('<[^<]+?>', '', str(star))
            review_text = re.sub('<[^<]+?>', '', str(review))

            data_dict[f"elem {count}"] = {
                "title": title_text.strip(),
                "star": star_text.strip(),
                "review": review_text.strip(),
            }
            count += 1

        # increment page number for next request
        page_number += 1

        # stop iterating if the total number of reviews has been reached
        if count > limit:
            break

    #print(json.dumps(data_dict, indent=4, ensure_ascii=False))
    mapdictionary(data_dict)

def mapdictionary(data_dict):
    df = pd.DataFrame(columns=['title', 'star', 'review'])
    for item in data_dict.items():
        title = item[1]['title']
        star = item[1]['star']
        review = item[1]['review']
        new_row = [title, star, review]
        df = df.append(pd.Series(new_row, index=df.columns), ignore_index=True)
    print(df)

#Try scraping_from_principal_page
#scraping_from_principal_page("https://www.amazon.it/Nilox-Batteria-Ricarica-Dimensioni-12x5x1/dp/B09HL19D41/ref=sr_1_1_sspa?__mk_it_IT=ÅMÅŽÕÑ&crid=3PLVZMB6348BT&keywords=nba&qid=1678624213&sprefix=n%2Caps%2C203&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1", 10)

# Try scraping_review
scraping_review("https://www.amazon.com/12-Rules-for-Life-audiobook/product-reviews/B0797Y87JC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews", 20)
#Mockup links
#https://www.amazon.com/12-Rules-for-Life-audiobook/product-reviews/B0797Y87JC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1
#https://www.amazon.com/12-Rules-for-Life-audiobook/product-reviews/B0797Y87JC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2
#https://www.amazon.it/Nilox-Batteria-Ricarica-Dimensioni-12x5x1/product-reviews/B09HL19D41/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=1
#https://www.amazon.it/Nilox-Batteria-Ricarica-Dimensioni-12x5x1/product-reviews/B09HL19D41/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2