import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Musical Instruments API</h1><p>This is a prototype API for managing musical instruments in venues.</p>"

app.run()

