from flask import Flask, render_template
import sqlite3
import os


app = Flask(__name__)


# def load_config():
os.environ.get("FLASK_APP")



@app.route('/')
def index():
    return render_template('index.html')

def get_db_connection():
    conn = sqlite3.connect('database.db') 
    conn.row_factory = sqlite3.Row
    return conn


#@app.route('/')
def search():
    pass
#app.route('/')
def login():
    pass

