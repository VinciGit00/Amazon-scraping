import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from PIL import Image
import base64
import time
from Home import *
from Scrape_review import *


def graphics():
    # Create a container for the sidebar
    st.sidebar.title("Options")

    if st.sidebar.button("Scraping the reviews"):
        scraping_page()
    elif st.sidebar.button("Scraping the categories"):
        HomePage()
    else:       
        HomePage()
        