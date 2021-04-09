from flask import Blueprint, render_template, request, jsonify, abort
from controllers.db_controller import Search

bp = Blueprint('example', __name__)

@bp.route('/')
def index():
    print('the backend is working')
    return render_template('index.html')

@bp.route('/search', methods=['GET'])
def query():
    s = Search()
    term = request.args.get('term')
    if term is not None:
        s.start(term)
        return s.get_results()
    else:
        abort(404)