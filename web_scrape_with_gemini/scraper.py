from selenium.webdriver.chrome.service import Service
import selenium.webdriver as webdriver

from bs4 import BeautifulSoup

from dotenv import load_dotenv
import os
import time


def scrape_website(website: str):
    """
    This function scrapes the given website url then returns the source code.
    Parameters:
        website: url of the website passed as string.
    Returns:
        source code of the webpage
    """
    print("Lauching browser..")
    chrome_driver_path = "./chromedriver-win64/chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()

