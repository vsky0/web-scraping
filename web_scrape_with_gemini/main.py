import streamlit as st 

from scraper import (
    scrape_website, 
    extract_body_content, 
    clean_body_content, 
    split_dom_content
    )
from parser import parse_with_gemini

# creating streamlit interface
st.title("AI web scraper")
url = st.text_input("Enter a website url..")

# scrape website
if st.button("scrape site"):
    st.write("Scraping website.........")
    dom_content = scrape_website(url)
    body_content = extract_body_content(dom_content)
    cleaned_content = clean_body_content(body_content)

    # storing the dom content in streamlit session
    st.session_state.dom_content = cleaned_content

    #display the dom content in exapandable text box
    with st.expander("View the Dom Content,here"):
        st.text_area("dom content",cleaned_content,height=300)
    
# ask the relevant questions
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want,")
    if parse_description:
        st.write("Parsing the content ....")

        # parse the content with Gemini
        dom_chunks = split_dom_content(st.session_state.dom_content)
        parsed_result = parse_with_gemini(dom_chunks,parse_description)
        st.write(parsed_result)

