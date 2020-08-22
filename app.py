import os

from flask import Flask, render_template, redirect
from flask import request
from enum import IntEnum
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



if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    dbHandler.create_table(database_path=path)
    app.run()
