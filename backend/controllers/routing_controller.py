from flask import Blueprint, render_template, request, jsonify
from controllers.db_controller import Search
import psycopg2

bp = Blueprint('example', __name__)

@bp.route('/')
def index():
    print('the backend is working')
    return render_template('index.html')

@bp.route('/search')
def query():
    s = Search()
    s.start()
    return s.get_results()