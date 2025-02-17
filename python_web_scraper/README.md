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
>parsed links output 

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
https://subslikescript.com//movie/The_Girl_on_a_Motorcycle-63013
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Taz_Quest_for_Burger-27469256
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Trust_Us-26009938
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Swooner_Crooner-37339
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Plane_Daffy-37180
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/A_Gruesome_Twosome-37753
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/I_Am_T-Rex-28117438
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Come_Into_My_World_How_to_Interact_with_a_Person_Who_Has_Dementia-11396186
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Shadow_Warriors-6975420
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/The_Young_Dragons-70801
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Tove-11007444
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/A_Not_So_Royal_Christmas-29593677
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Land_of_Fear-233234
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Daddy_Daughter_Trip-15367558
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/The_Projected_Man-62159
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Bunker_Hill_Bunny-42290
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/The_Night_Heaven_Fell-50193
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Violette_nei_capelli-34362
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Body_on_the_Beach-21155252
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Earth-7541728
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/The_Morning_After-17541886
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Hyde_Park-15727400
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Anthropophagus_II-13757762
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/Je_taime_moi_non_plus-73196
printing list of retrieved parsed links on page.
https://subslikescript.com//movie/How_to_Fall_in_Love_by_Christmas-29144851

Process finished with exit code 0

>
>
>