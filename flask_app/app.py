from flask import Flask
from flask import request

server = Flask(__name__)


def run_request():
    index = int(request.json['index'])
    colours = ['red', 'green', 'blue', 'yellow', 'black']
    return colours[index]


@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()
