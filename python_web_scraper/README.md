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
```
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
```
### Parsing multiple page links and scraping data for each link via bs4:
```
# parsing through each movie link with BeautifulSoup and scraping data
for link in list:
    print(f"{root}{link}")
    result = requests.get(f"{root}{link}")
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    print(f"created soup for {link}")
    # parsing through each link and scraping data.
    main_box = soup.find('article', class_="main-article")
    title = main_box.find('h1').get_text(strip=True)
    try:
        description = main_box.find('p', class_="plot").get_text(strip=True)
    except AttributeError:
        continue
    transcript = main_box.find('div', class_="full-script").get_text(strip=True)
    print(f"Parsed {link}")
```
### Output
```
C:\Users\nasrs\Documents\Python-Projects\python_web_scraper\venv\Scripts\python.exe C:/Users/nasrs/Documents/Python-Projects/python_web_scraper/web_scraper_site_wide.py
List of Movie Names
['Kalevala - uusi aika (2013)', 'Face Off: The Walking Guests ()', 'Revenge of the First Wives (1997)', 'The London Nobody Knows (1968)', 'Building Ireland (2017)', 'The Girl on a Motorcycle (1968)', 'Taz: Quest for Burger (2023)', 'Trust Us (2022)', 'Swooner Crooner (1944)', 'Plane Daffy (1944)', 'A Gruesome Twosome (1945)', 'I Am T-Rex (2022)', 'Come Into My World: How to Interact with a Person Who Has Dementia (2009)', 'Shadow Warriors (1980)', 'The Young Dragons (1974)', 'Tove (2020)', 'A Not So Royal Christmas (2023)', 'Land of Fear (1999)', 'Daddy Daughter Trip (2022)', 'The Projected Man (1966)', 'Bunker Hill Bunny (1950)', 'The Night Heaven Fell (1958)', 'Violette nei capelli (1942)', 'Body on the Beach ()', 'Earth ()', 'The Morning After (2023)', 'Hyde Park (2022)', 'Anthropophagus II (2022)', "Je t'aime moi non plus (1976)", 'How to Fall in Love by Christmas (2023)']
List of movie links
['/movie/Kalevala_-_uusi_aika-2192882', '/movie/Face_Off_The_Walking_Guests-10187348', '/movie/Revenge_of_the_First_Wives-16244948', '/movie/The_London_Nobody_Knows-61914', '/movie/Building_Ireland-14350334', '/movie/The_Girl_on_a_Motorcycle-63013', '/movie/Taz_Quest_for_Burger-27469256', '/movie/Trust_Us-26009938', '/movie/Swooner_Crooner-37339', '/movie/Plane_Daffy-37180', '/movie/A_Gruesome_Twosome-37753', '/movie/I_Am_T-Rex-28117438', '/movie/Come_Into_My_World_How_to_Interact_with_a_Person_Who_Has_Dementia-11396186', '/movie/Shadow_Warriors-6975420', '/movie/The_Young_Dragons-70801', '/movie/Tove-11007444', '/movie/A_Not_So_Royal_Christmas-29593677', '/movie/Land_of_Fear-233234', '/movie/Daddy_Daughter_Trip-15367558', '/movie/The_Projected_Man-62159', '/movie/Bunker_Hill_Bunny-42290', '/movie/The_Night_Heaven_Fell-50193', '/movie/Violette_nei_capelli-34362', '/movie/Body_on_the_Beach-21155252', '/movie/Earth-7541728', '/movie/The_Morning_After-17541886', '/movie/Hyde_Park-15727400', '/movie/Anthropophagus_II-13757762', '/movie/Je_taime_moi_non_plus-73196', '/movie/How_to_Fall_in_Love_by_Christmas-29144851']
https://subslikescript.com/movie/Kalevala_-_uusi_aika-2192882
created soup for /movie/Kalevala_-_uusi_aika-2192882
Parsed /movie/Kalevala_-_uusi_aika-2192882
https://subslikescript.com/movie/Face_Off_The_Walking_Guests-10187348
created soup for /movie/Face_Off_The_Walking_Guests-10187348
https://subslikescript.com/movie/Revenge_of_the_First_Wives-16244948
created soup for /movie/Revenge_of_the_First_Wives-16244948
Parsed /movie/Revenge_of_the_First_Wives-16244948
https://subslikescript.com/movie/The_London_Nobody_Knows-61914
created soup for /movie/The_London_Nobody_Knows-61914
Parsed /movie/The_London_Nobody_Knows-61914
https://subslikescript.com/movie/Building_Ireland-14350334
created soup for /movie/Building_Ireland-14350334
https://subslikescript.com/movie/The_Girl_on_a_Motorcycle-63013
created soup for /movie/The_Girl_on_a_Motorcycle-63013
Parsed /movie/The_Girl_on_a_Motorcycle-63013
https://subslikescript.com/movie/Taz_Quest_for_Burger-27469256
created soup for /movie/Taz_Quest_for_Burger-27469256
Parsed /movie/Taz_Quest_for_Burger-27469256
https://subslikescript.com/movie/Trust_Us-26009938
created soup for /movie/Trust_Us-26009938
Parsed /movie/Trust_Us-26009938
https://subslikescript.com/movie/Swooner_Crooner-37339
created soup for /movie/Swooner_Crooner-37339
Parsed /movie/Swooner_Crooner-37339
https://subslikescript.com/movie/Plane_Daffy-37180
created soup for /movie/Plane_Daffy-37180
Parsed /movie/Plane_Daffy-37180
https://subslikescript.com/movie/A_Gruesome_Twosome-37753
created soup for /movie/A_Gruesome_Twosome-37753
Parsed /movie/A_Gruesome_Twosome-37753
https://subslikescript.com/movie/I_Am_T-Rex-28117438
created soup for /movie/I_Am_T-Rex-28117438
Parsed /movie/I_Am_T-Rex-28117438
https://subslikescript.com/movie/Come_Into_My_World_How_to_Interact_with_a_Person_Who_Has_Dementia-11396186
created soup for /movie/Come_Into_My_World_How_to_Interact_with_a_Person_Who_Has_Dementia-11396186
https://subslikescript.com/movie/Shadow_Warriors-6975420
created soup for /movie/Shadow_Warriors-6975420
Parsed /movie/Shadow_Warriors-6975420
https://subslikescript.com/movie/The_Young_Dragons-70801
created soup for /movie/The_Young_Dragons-70801
Parsed /movie/The_Young_Dragons-70801
https://subslikescript.com/movie/Tove-11007444
created soup for /movie/Tove-11007444
Parsed /movie/Tove-11007444
https://subslikescript.com/movie/A_Not_So_Royal_Christmas-29593677
created soup for /movie/A_Not_So_Royal_Christmas-29593677
Parsed /movie/A_Not_So_Royal_Christmas-29593677
https://subslikescript.com/movie/Land_of_Fear-233234
created soup for /movie/Land_of_Fear-233234
Parsed /movie/Land_of_Fear-233234
https://subslikescript.com/movie/Daddy_Daughter_Trip-15367558
created soup for /movie/Daddy_Daughter_Trip-15367558
Parsed /movie/Daddy_Daughter_Trip-15367558
https://subslikescript.com/movie/The_Projected_Man-62159
created soup for /movie/The_Projected_Man-62159
Parsed /movie/The_Projected_Man-62159
https://subslikescript.com/movie/Bunker_Hill_Bunny-42290
created soup for /movie/Bunker_Hill_Bunny-42290
Parsed /movie/Bunker_Hill_Bunny-42290
https://subslikescript.com/movie/The_Night_Heaven_Fell-50193
created soup for /movie/The_Night_Heaven_Fell-50193
Parsed /movie/The_Night_Heaven_Fell-50193
https://subslikescript.com/movie/Violette_nei_capelli-34362
created soup for /movie/Violette_nei_capelli-34362
Parsed /movie/Violette_nei_capelli-34362
https://subslikescript.com/movie/Body_on_the_Beach-21155252
created soup for /movie/Body_on_the_Beach-21155252
https://subslikescript.com/movie/Earth-7541728
created soup for /movie/Earth-7541728
https://subslikescript.com/movie/The_Morning_After-17541886
created soup for /movie/The_Morning_After-17541886
Parsed /movie/The_Morning_After-17541886
https://subslikescript.com/movie/Hyde_Park-15727400
created soup for /movie/Hyde_Park-15727400
Parsed /movie/Hyde_Park-15727400
https://subslikescript.com/movie/Anthropophagus_II-13757762
created soup for /movie/Anthropophagus_II-13757762
Parsed /movie/Anthropophagus_II-13757762
https://subslikescript.com/movie/Je_taime_moi_non_plus-73196
created soup for /movie/Je_taime_moi_non_plus-73196
Parsed /movie/Je_taime_moi_non_plus-73196
https://subslikescript.com/movie/How_to_Fall_in_Love_by_Christmas-29144851
created soup for /movie/How_to_Fall_in_Love_by_Christmas-29144851
Parsed /movie/How_to_Fall_in_Love_by_Christmas-29144851

Process finished with exit code 0
```