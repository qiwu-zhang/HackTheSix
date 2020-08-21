from flask import Flask, render_template
from flask import request
import database_utilities as dbHandler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        return render_template('signlog.html')
    else:
        return render_template('signlog.html')


if __name__ == '__main__':
    app.run()
