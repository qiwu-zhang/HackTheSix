import os

from flask import Flask, render_template, flash
from flask import request, redirect
from wtforms import Form, TextField 
import database_utilities as dbHandler

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


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
    dbHandler.create_database(database_path=path)
    app.run()


