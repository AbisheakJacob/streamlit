# importing the packages
import streamlit as st
from bs4 import BeautifulSoup
import gdown
import os
import datetime
import time
from selenium import webdriver

# get todays date in the format "14 August"
today_date = datetime.datetime.now().strftime("%d %B")
todays_date = today_date.replace(" ", "  ")
todays_date = todays_date.lstrip("0") + " "

# finding the current location
here = os.path.dirname(os.path.abspath(__file__))

# page title
st.title("Newspaper Downloader")

if st.button("Download Economic Times"):
    # initialize the browser
    browser = webdriver.Chrome("./chromedriver")

    # the base url for the site
    url = "https://epaperpdf.download/the-economic-times/"

    # go to the required page
    browser.get(url)

    # wait for 3 seconds
    time.sleep(5)

    # get the html_source of the webpage
    html_source = browser.page_source

    # close the web browser
    browser.quit()

    # parse the webpage content using beautifulsoup
    soup = BeautifulSoup(html_source, "html.parser")

    # Find all the <p> tags with today's date as text
    matching_paragraphs = [p for p in soup.find_all("p") if todays_date in p.get_text()]

    # Extract and print the links from the matching paragraphs
    for p in matching_paragraphs:
        link = p.find("a")
        if link:
            href = link.get("href")
    try:
        # Google Drive file ID from the link
        file_id = href[32:-18]

        # Local file path to save the downloaded file
        file_name = "Economic Times "

        # Output file name for downloaded file
        output_file_name = file_name + todays_date + ".pdf"

        # Construct the full file path
        output_file_path = os.path.join(here, output_file_name)

        # Construct the download URL
        download_url = f"https://drive.google.com/uc?id={file_id}"

        # Download the file
        gdown.download(download_url, output_file_path, quiet=False)
        with open(output_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        if st.download_button(
            label="Download", data=pdf_bytes, file_name=output_file_name, key="pdf"
        ):
            st.success("The Download was successful")
    except:
        st.error("The Download Failed")
