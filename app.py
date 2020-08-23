import os
import codecs
import argparse
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from flask import request, flash, url_for, session
from wtforms import Form, TextField
import web_scraping_utilities
from enum import IntEnum
import database_utilities as dbHandler
from classDefs import Financial_Data as fData
from urllib.request import urlopen

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

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        resp = dbHandler.login(userName=email, Password=password)
        if resp == LOGIN_STATE.USER_DOESNT_EXIST:
            print("user doesn't exist. Would you like to sign up?")  ## Add an error text, but don't redirect
            dbHandler.insert_User(userName=email, Password=password)
            return "No Match!"
        elif resp == LOGIN_STATE.USER_EXISTS:
            print("login successfully")
            return redirect('/dashboard')

    else:
        print("scraping web")
        dbHandler.create_table_saving_plans()
        file = codecs.open("HISA.html", 'r', 'utf-8')
        web_scraping_utilities.scrape_page(file)
        file = codecs.open("RRSP.html", 'r', 'utf-8')
        web_scraping_utilities.scrape_page(file)
        file = codecs.open("TFSA.html", 'r', 'utf-8')
        web_scraping_utilities.scrape_page(file)
        file = codecs.open("YOUTH.html", 'r', 'utf-8')
        web_scraping_utilities.scrape_page(file)
        return render_template('signlog.html')


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('index.html')


@app.route('/inputForm', methods=["GET", "POST"])
def input_form():
    if request.method == "POST":
        req = request.form
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("inputForm.html", feedback=feedback)
        else:
            # currData = fData()
            # currData.income = request.form.get("income")
            # currData.food = request.form.get("food")
            # currData.housing = request.form.get("housing")
            # currData.misc = request.form.get("misc")
            # session['currData'] = currData

            income = request.form.get("income")
            food = request.form.get("food")
            # housing=request.form.get("housing")
            session['housing'] = request.form.get("housing")
            session['misc'] = request.form.get("misc")

            return redirect(url_for('results', income=income, food=food))
        return redirect(request.url)
    return render_template("inputForm.html")


@app.route('/results')
def results():
    # currData = fData()

    income = request.args.get('income', None)
    food = request.args.get('food', None)
    housing = session.get('housing', None)
    misc = session.get('misc', None)

    print(food, housing, misc)
    income = int(income)
    food = int(food)
    housing = int(housing)
    misc = int(misc)
    currData = fData(food, housing, misc, income)
    totalExpenses = food + housing + misc
    # currData = session.get('currData', None)
    # income = currData.income
    return render_template("results.html", currData=currData)


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")

    dbHandler.create_table()
    dbHandler.create_table_saving_plans()
    app.run()
