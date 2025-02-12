'''Welcome to my Python Web Scraper
in this project I will test web scraping from Indeed job searches, to gain insights and gather job data for faster, effective understanding of the job market.
'''
# built by Nasr Syed

'''
url structure:
"q=" describes the "what" field on the page.
salary is parsed by %24, then number, then comma broken by %20. ie: %2450%2C000 = $50,000
"&l=" is the start of the string for city. "+" is used to split multiple word cities.
"&start=" is the positional placeholder for result.
'''
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())

