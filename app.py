import os
import requests
from bs4 import BeautifulSoup

import base64
import datetime
import plaid
import json
import time
import argparse
import requests
from flask import Flask, render_template, flash
from flask import request, redirect, request, jsonify, \
url_for, session
from wtforms import Form, TextField
import web_scraping_utilities
from enum import IntEnum
import database_utilities as dbHandler
from classDefs import Financial_Data as fData

app = Flask(__name__, template_folder="./src/templates", static_folder="./src/static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

############################################################## LOGIN ###############################################################3
class LOGIN_STATE(IntEnum):
    USER_DOESNT_EXIST = 0
    USER_EXISTS = 1

@app.before_request
def before_request():
    dbHandler.make_connection()


@app.route('scraping', methods=['GET'])
def scrapeWeb():
    print("scraping web")
    urls = web_scraping_utilities.load_urls_from_file("bankWebsite.txt")
    for url in urls:
    web_scraping_utilities.scrape_page(url=url)

@app.route('/login', methods=['POST'])
def first_step():
    email = request.form['email']
    password = request.form['password']
    resp = dbHandler.login(userName=email, Password=password)
    if resp == LOGIN_STATE.USER_DOESNT_EXIST:
        print("user doesn't exist. Would you like to sign up?") ## Add an error text, but don't redirect
        dbHandler.insert_User(userName=email, Password=password)
        return "Login Unsuccessful"
    elif resp == LOGIN_STATE.USER_EXISTS:
        return "Login Successful"


########################################################### PLAID #########################################################

# Fill in your Plaid API keys - https://dashboard.plaid.com/account/keys
PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
# PLAID_PRODUCTS is a comma-separated list of products to use when initializing
# Link. Note that this list must contain 'assets' in order for the app to be
# able to create and retrieve asset reports.
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions').split(',')

# PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
# will be able to select institutions from.
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')


def empty_to_none(field):
  value = os.getenv(field)
  if value is None or len(value) == 0:
    return None
  return value


# Parameters used for the OAuth redirect Link flow.
#
# Set PLAID_REDIRECT_URI to 'http://localhost:8000/oauth-response.html'
# The OAuth redirect flow requires an endpoint on the developer's website
# that the bank website should redirect to. You will need to configure
# this redirect URI for your client ID through the Plaid developer dashboard
# at https://dashboard.plaid.com/team/api.
PLAID_REDIRECT_URI = empty_to_none('PLAID_REDIRECT_URI')

client = plaid.Client(client_id=PLAID_CLIENT_ID,
                      secret=PLAID_SECRET,
                      environment=PLAID_ENV,
                      api_version='2019-05-29')
@app.route('/api/create_link_token', methods=['POST'])
def create_link_token():
  try:
    # form = request.get_json()
    response = client.LinkToken.create(
      {
        'user': {
          # This should correspond to a unique id for the current user.
          'client_user_id': PLAID_CLIENT_ID,
        },
        "secret": PLAID_SECRET,
        'client_name': "Plaid Quickstart",
        'products': PLAID_PRODUCTS,
        'country_codes': PLAID_COUNTRY_CODES,
        'language': "en",
        'redirect_uri': PLAID_REDIRECT_URI,
      }
    )
    pretty_print_response(response)
    return jsonify(response)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))
    
# Exchange token flow - exchange a Link public_token for
# an API access_token
# https://plaid.com/docs/#exchange-token-flow
@app.route('/api/set_access_token', methods=['POST'])
def get_access_token():
  global access_token
  global item_id
  public_token = request.form['public_token']
  try:
    exchange_response = client.Item.public_token.exchange(public_token)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))

  pretty_print_response(exchange_response)
  access_token = exchange_response['access_token']
  item_id = exchange_response['item_id']
  return jsonify(exchange_response)

def pretty_print_response(response):
  print(json.dumps(response, indent=2, sort_keys=True))

<<<<<<< HEAD
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
        missing = list()
        
        for k,v in req.items():
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

            
            income =  request.form.get("income")
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

    income=request.args.get('income', None)
    food=request.args.get('food', None)
    housing = session.get('housing', None)
    misc = session.get('misc', None)

    print(food,housing, misc)
    income=int(income)
    food=int(food)
    housing=int(housing)
    misc=int(misc)
    currData = fData(food, housing, misc, income)
    totalExpenses=food+housing+misc
    # currData = session.get('currData', None)
    # income = currData.income
    return render_template("results.html", currData=currData)







=======
def format_error(e):
  return {'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type, 'error_message': e.message } }


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    dbHandler.create_table(database_path=path)
    dbHandler.create_table_saving_plans("bankWebsite.txt")
>>>>>>> HarrisReact
    app.run()


