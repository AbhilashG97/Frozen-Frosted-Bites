import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome HimmelDreng</h1><p>I love watermelons. Do you like watermelons too?</p>"

app.run()