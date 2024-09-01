import streamlit as st 
from scraper import scrape_website

# creating streamlit interface
st.title("AI web scraper")
url = st.text_input("Enter a website url..")

if st.button("scrape site"):
    st.write("Scraping website")
    result = scrape_website(url)
    # print(result)
    # print(type(result)) is string

