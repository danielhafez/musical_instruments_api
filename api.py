import flask
from data import users, instruments_data

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def homepage():
    return "<h1>Musical Instruments API</h1><p>This is a prototype API for managing musical instruments in venues.</p>"

app.run()




