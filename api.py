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


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    if post_id not in posts_storage:
        abort(404)

    post = posts_storage[post_id].format_to_json()
    response = app.response_class(
        response=json.dumps(post),
        status=200,
        mimetype='application/json')
    return response



app.run()




