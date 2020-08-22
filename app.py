import os
import argparse
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from flask import request
import web_scraping_utilities
import database_utilities as dbHandler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def first_step():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        os.chdir(os.path.dirname(__file__))
        path = os.path.join(os.getcwd(), "LoginInfo.db")
        if dbHandler.login(database_path=path, userName=email, Password=password) == 0:
            print("user doesn't exist")
            dbHandler.insert_User(database_path=path, userName=email, Password=password)
        if dbHandler.login(database_path=path, userName=email, Password=password) == 1:
            print("login successfully")
            return redirect('/dashboard')
        else:
            return redirect('/dashboard')

    else:
        return render_template('signlog.html')


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('index.html')


def main(database: str, url_list_file: str):
    saving_plan_list = []
    print("we are going to work with " + database)
    print("we are going to scan " + url_list_file)
    urls = web_scraping_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("reading " + url)
        page_content = web_scraping_utilities.load_page(url=url)
        saving_plans = web_scraping_utilities.scrape_page(page_content)
        saving_plan_list.extend(saving_plans)


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    dbHandler.create_database(database_path=path)
    app.run()
