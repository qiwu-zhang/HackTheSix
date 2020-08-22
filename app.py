import os
import argparse
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from flask import request, flash
from wtforms import Form, TextField
import web_scraping_utilities
from enum import IntEnum
import database_utilities as dbHandler

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class LOGIN_STATE(IntEnum):
    USER_DOESNT_EXIST = 0
    USER_EXISTS = 1

@app.before_request
def before_request():
    dbHandler.make_connection()


@app.route('/', methods=['POST', 'GET'])
def first_step():
    print("scraping web")
    urls = web_scraping_utilities.load_urls_from_file("bankWebsite.txt")
    for url in urls:
        web_scraping_utilities.scrape_page(url=url)

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

def main(url_list_file:str):
    print("scraping web")
    urls = web_scraping_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        page_content = web_scraping_utilities.load_page(url=url)
        web_scraping_utilities.scrape_page(page_content)


@app.route('/inputForm', methods = ["GET", "POST"])
def input_form():
    if request.method == "POST":
        req = request.form
        food = request.form.get("food")
        housing = request.form.get("housing")
        misc = request.form.get("misc")
        print(req)
        return redirect(request.url)
    return render_template("inputForm.html")

@app.route('/done')
def place_holder():
    return render_template("tables.html")





if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    dbHandler.create_table(database_path=path)
    dbHandler.create_table_saving_plans("bankWebsite.txt")

    app.run()


