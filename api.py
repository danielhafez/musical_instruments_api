import flask
import json
from data import users, instruments_data

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def homepage():
    return "<h1>Musical Instruments API</h1><p>This is a prototype API for managing musical instruments in venues.</p>"


@app.route('/instruments')
def get_all_instruments():
    response = app.response_class(
        response=json.dumps(instruments_data),
        status=200,
        mimetype='application/json')
    return response


@app.route('/instruments/<user_name>')
def get_instruments_by_user(user_name):
    instruments= []
    for i in instruments_data:
        users = instruments_data[i]['user']
        for num in users:
            if num['first_name'] == user_name:
                instruments.append(instruments_data[i])

    response = app.response_class(
        response=json.dumps(instruments),
        status=200,
        mimetype='application/json')
    return response

app.run()




