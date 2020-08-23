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
    savingPlan_list_name=[]
    savingPlan_list_type = []
    soup = BeautifulSoup(page_contents, "html5lib")
    soup.prettify()
    name = soup.select("span.provider-name")
    saving_type = soup.find('h1')

    for i in range(0, len(name)):
        savingPlan_list_name.append(name[i].text)
        savingPlan_list_type.append(saving_type)
        dbHandler.insert_saving_plans(name=name[i].text, type=saving_type.text)

    dict_savingPlan = dict({1: savingPlan_list_name, 2: savingPlan_list_type})

    return dict_savingPlan
