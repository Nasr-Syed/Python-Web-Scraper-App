# Python Web Scraper Project
### By: Nasr Syed

In this project, I will browse through a movie website that holds transcripts for thousands of movies. The code has 2 versions. 

- The first one parses through a single page on the website. 
- The second site wide version of the code parses through each link, and page, thus successfully scraping an entire site containing thousands of movie links. 
- The files are then written to a .txt file for data storage. 

### The Python web scraper uses BeautifulSoup to retrieve HTML data from a website, and parse through it's content.
```
import os
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

# importing data from HTML using requests and BeautifulSoup
root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# parse through website HTML blocks to find main block of code describing Movie title, description, transcript.
main_box = soup.find('article', class_="main-article")
title = main_box.find('h1').get_text(strip=True)
links = main_box.find_all('a', href=True)
```

### As seen below, the following code snippet parses and retrieves a list of all links displayed on the website ready to be parsed by BeautifulSoup.
```
# obtaining list of all movie links
list = []
for link in links:
    list.append(link['href'])
# parsing through each movie link with BeautifulSoup

for link in list:
    print("retrieves list of retrieved parsed links on page.")
    print(f"{root}/{link}")
    result = requests.get(f"{root}/{link}")
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
```
### Output
parsed links output 

C:\Users\nasrs\Documents\Python-Projects\python_web_scraper\venv\Scripts\python.exe C:/Users/nasrs/Documents/Python-Projects/python_web_scraper/web_scraper_site_wide.py
printing list of retrieved parsed links on page.

https://subslikescript.com//movie/Kalevala_-_uusi_aika-2192882
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Face_Off_The_Walking_Guests-10187348
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Revenge_of_the_First_Wives-16244948
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/The_London_Nobody_Knows-61914
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Building_Ireland-14350334
printing list of retrieved parsed links on page.

(prints about 2000 links which are cut short in README for brevity)
...
...
...

Process finished with exit code 0
