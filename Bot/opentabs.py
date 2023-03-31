import time

# source env/bin/activate
# Video: https://www.youtube.com/watch?v=lT8XNpfo950
from selenium import webdriver

while True:
        driver = webdriver.Chrome()
      
        driver.get("https://vincigit00-amazon-scraping-app-nfzu99.streamlit.app")
        time.sleep(10)

        driver.get("https://vincigit00-nba-platform-main-ounnit.streamlit.app")
        time.sleep(10)

        driver.get("https://marco-vinciguerra-dev.onrender.com")
        time.sleep(10)
        driver.quit()
