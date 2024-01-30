from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(): return 'PYTHON SNAKE'


@app.route('/score', methods=['POST'])
def add_score():
    return 0

@app.route('/scoreboard', methods=['GET'])
def scoreboard():