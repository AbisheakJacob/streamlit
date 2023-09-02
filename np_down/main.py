# importing the packages
import streamlit as st
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import gdown
import os
import datetime
import time
from selenium import webdriver

# page title
st.title("Newspaper Downloader")

if st.button("Download Economic Times"):
    st.text("Wait for the programmer to finish programming")

    # initialize the browser
    browser = webdriver.Chrome()

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
