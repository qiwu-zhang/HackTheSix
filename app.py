import os
import argparse
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from flask import request
<<<<<<< HEAD
import web_scraping_utilities
=======
from enum import IntEnum
>>>>>>> e65fce831ee299f170f2b2ccf5659b105f4d1377
import database_utilities as dbHandler

app = Flask(__name__)

class LOGIN_STATE(IntEnum):
    USER_DOESNT_EXIST = 0
    USER_EXISTS = 1

@app.before_request
def before_request():
    dbHandler.make_connection()


@app.route('/', methods=['POST', 'GET'])
def first_step():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        resp = dbHandler.login(userName=email, Password=password)
        if resp == LOGIN_STATE.USER_DOESNT_EXIST:
            print("user doesn't exist. Would you like to sign up?") ## Add an error text, but don't redirect
            dbHandler.insert_User(userName=email, Password=password)
            return "No Match!"
        elif resp == LOGIN_STATE.USER_EXISTS:
            print("login successfully")
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
    dbHandler.create_table(database_path=path)
    app.run()
