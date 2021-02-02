from flask import Flask, render_template
import sqlite3
import os


app = Flask(__name__)


os.environ.get("FLASK_APP")


def get_db_connection():
    conn = sqlite3.connect('database.db') 
    conn.row_factory = sqlite3.Row
    return conn


def get_ip_info(ip_addr):
    ip_json = requests.get('http://ip-api.com/json/' + ip_addr).json()  # get json object from api
    return ip_json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locate')
def locate():
    ip_addr = request.remote_addr # ip address of the incoming connection
    return get_ip_info(ip_addr)




# #@app.route('/')
# def search():
#     pass
# #app.route('/')
# def login():
#     pass

if __name__ == "__main__":
    application.run(debug=False)