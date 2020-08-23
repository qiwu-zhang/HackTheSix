import re
import string
import requests
from urllib.request import urlopen
import database_utilities as dbHandler

from bs4 import BeautifulSoup


def load_urls_from_file(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readlines()
            return content
    except FileNotFoundError:
        print("the file " + file_path + " could not be found")
        exit(2)


def scrape_page(page_contents: str):
    soup = BeautifulSoup(page_contents, "html5lib")
    soup.prettify()
    name = soup.select("span.provider-name")
    saving_type = soup.find('h1')
    dbHandler.insert_saving_plans(name,saving_type)
    for i in range(0, len(name)):
        print(saving_type.text)
        print(name[i].text)
