import os

from flask import Flask, render_template
from flask import request
import database_utilities as dbHandler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        os.chdir(os.path.dirname(__file__))
        path = os.path.join(os.getcwd(),"LoginInfo.db")
        dbHandler.create_database(database_path=path)
        dbHandler.insert_User(database_path=path, userName=email, Password=password)
        return render_template('signlog.html')

    else:
       return render_template('signlog.html')



if __name__ == '__main__':
    app.run()
