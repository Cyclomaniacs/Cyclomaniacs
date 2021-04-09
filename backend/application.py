from flask import Flask
import os
from dotenv import load_dotenv
from controllers.routing_controller import bp
from cyclescrapers.runcycles import run_scrapers

app = Flask(__name__)

load_dotenv()

appname = os.getenv("FLASK_APP")
port = os.getenv("FLASK_RUN_PORT")
host = os.getenv("FLASK_RUN_HOST")

app.register_blueprint(bp, url_prefix='/api')

# def get_ip_info(ip_addr):
#     ip_json = requests.get('http://ip-api.com/json/' + ip_addr).json()  # get json object from api
#     return ip_json
#
#
# @app.route('/locate')
# def locate():
#    ip_addr = request.remote_addr # ip address of the incoming connection
#    return get_ip_info(ip_addr)
#
#
# @app.route('/scrapetest')
# def scrapetest():
#    run_scrapers('fox ranger gloves')
#    return
#
#
# @app.route('/')
# def search():
#    pass
#
#
# app.route('/')
# def login():
#    pass


if __name__ == "__main__":
    app.run(host=host, port=port, debug=False)