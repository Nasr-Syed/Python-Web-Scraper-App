'''Welcome to my Python Web Scraper
in this practice project, I will loop through multiple pages of a movie website. practicing looping a website to scrape data from multiple pages.
'''
# built by Nasr Syed

'''

'''
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

# importing data from HTML using results and BeautifulSoup
url = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content, 'lxml')
soup.prettify()

#parse through website HTML blocks to find main block of code describing Movie title, description, transcript.

main_box = soup.find('article', class_="main-article")
title = main_box.find('h1').get_text(strip=True )
description = main_box.find('p', class_="plot").get_text(strip=True)
transcript = main_box.find('div', class_="full-script")

print(title, "\n", description, "\n", transcript)

# exporting into .txt file
with open(f'{title}.txt', 'w') as file:
    file.write(title, description, transcript)