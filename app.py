import os

from flask import Flask, render_template, redirect
from flask import request
import database_utilities as dbHandler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def second_step():
    print("first step")
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



if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    dbHandler.create_database(database_path=path)
    app.run()
