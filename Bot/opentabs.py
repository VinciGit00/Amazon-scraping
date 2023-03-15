import time
from selenium import webdriver

#Run the script
def webBot():

  
    while True:
        # Initialize the webdriver
        driver = webdriver.Chrome()
        # Navigate to a website
        driver.get("https://vincigit00-amazon-scraping-app-nfzu99.streamlit.app")
        time.sleep(10)

        driver.get("https://vincigit00-nba-platform-main-ounnit.streamlit.app")
        time.sleep(10)

        driver.get("https://marco-vinciguerra-dev.onrender.com")
        time.sleep(10)

        # Close the browser
        driver.quit()
        time.sleep(3600)

if __name__ == "__main__":
    webBot()