import re
import string
import requests
from urllib.request import urlopen

from bs4 import BeautifulSoup


def load_urls_from_file(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readlines()
            return content
    except FileNotFoundError:
        print("the file " + file_path + " could not be found")
        exit(2)



def scrape_page(url: str):
    response = request.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.find_all('span', class_= "provider-name ng-binding")
    type = soup.find_all('h1', class_='ng-scope')
    rate = soup.find_all('span', class_= 'ng-binding')
    for i in range(0,len(name)):
        print(type)
        print(name[i].text)
        print(rate[i].text)

