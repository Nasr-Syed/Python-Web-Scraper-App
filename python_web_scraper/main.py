'''Welcome to my Python Web Scraper - Nasr Syed

for my own practice and curiosity, I will loop through multiple pages of a movie website. practicing looping a website to scrape data from multiple pages. I will append them to a text file to create a local database.
'''

import os
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

# importing data from HTML using requests and BeautifulSoup

url = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content, 'lxml')
soup.prettify()

# parse through website HTML blocks to find main block of code describing Movie title, description, transcript.

main_box = soup.find('article', class_="main-article")
title = main_box.find('h1').get_text(strip=True)
description = main_box.find('p', class_="plot").get_text(strip=True)
transcript = main_box.find('div', class_="full-script").get_text(strip=True)

print(title, "\n", description, "\n", transcript)
base_path = r"C:\Users\nasrs\Documents\Python-Projects\python_web_scraper\movies_database"

file_path = base_path + "/" + title + ".txt"

# cleanup from past runs
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
else:
    print(f"File '{file_path}' not found. Continuing data appendage.")

# exporting into .txt file
with open(f'{file_path}', 'a') as file:
    file.write(description)
    file.write(" ")
    file.write(transcript)
