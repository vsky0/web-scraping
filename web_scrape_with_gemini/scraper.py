# from selenium.webdriver.chrome.service import Service
# import selenium.webdriver as webdriver - used for local chrome browsers to scrape.

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

from bs4 import BeautifulSoup

import os
from dotenv import load_dotenv
load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER1")



def scrape_website(website: str):
    """
    This function scrapes website using bright data remote browser the given website url then returns the source code.
    Parameters:
        website: url of the website passed as string.
    Returns:
        source code of the webpage
    """
    print("Lauching browser..")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER,"goog","chorme")
    with Remote(sbr_connection,options=ChromeOptions()) as driver:
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd":"Captcha.waitForSolve",
                "params":{"detectTimeout":10000},
            },
        )

    print("Captcha solve status:",solve_res["value"]["status"])
    print("Page Loaded, scraping the page content...")
    html = driver.page_source
    return html

def extract_body_content(html_content: str) -> str:
    """
    The function returns the body content from the passed `html_content`, using the soup object, if no body content is found then return empty string.

    Parameters:
        the `html_content` is a string, which has html content.
    Returns:
        the function returns the body content in body tag, as `body_content` .
    """
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    """
    This function cleans the body conent, we use the soup object to parse the html `body_content`, 
    then get the text from the soup object.

    Arguments:
        `body_content:` is string, which has body content.
    Returns:
        the cleaned text content from the `body_content`.

    """
    soup = BeautifulSoup(body_content,"html.parser")
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content,max_length=5000):
    """
    This function is used for splitting the content based on the `max_length`,
    which will passed as the batch of text `max_length`

    Arguments:
        dom_content: extracted content.
    Returns:
        returns the dom content in batches of `max_length`
    """
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]

    

