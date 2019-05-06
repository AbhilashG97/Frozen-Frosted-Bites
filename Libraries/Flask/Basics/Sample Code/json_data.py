import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

fruits = [
    {
        'name' : 'watermelon',
        'price' : 12
    },
    {
        'name' : 'banana',
        'price' : 20
    },
    {
        'name' : 'orange',
        'price' : 100
    }
]

@app.route("/", methods=['GET'])
def home():
    return "<h1>Watermelon Heart</h1><p>Do you like watermelons?</p>"

@app.route("/watermelon", methods=['GET'])
def hello_watermelon():
    return "<h1>Hello Watermelon</h1>"

@app.route("/api/v1/resources/fruits/all", methods=['GET'])
def display_fruits():
    return jsonify(fruits)

app.run()