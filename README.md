# HackTheSix project 
##  Name Pending  ##

##   Description  ##
This is a personalized web app that will give the user several tailored saving plans. The user will input current savings, expenses, and earnings and then be provided with suggested plans.
The plans will have a variety of risks, lengths of time, and certain restrictions(like age), and will suggest a combination of cutting specific expense and investment opportunities so the user can choose whatever plan suits them best.

This project used HTML, CSS, Javascript, Flask, React, Python, SQLite and BeautifulSoup4 library.

## SETUP ##
To run the front_end, use
> cd front_end
> npm install

To install the python dependencies, run
> pip install -r requirements.txt

To start the backend server, run
> PLAID_CLIENT_ID=5f3f5c7bd4530d001106214d \
> PLAID_SECRET=8a93ca80daf1eef77524335027fe7e \
> PLAID_PRODUCTS=transactions \
> PLAID_COUNTRY_CODES=US \
> PLAID_ENV=sandbox \
> flask run
