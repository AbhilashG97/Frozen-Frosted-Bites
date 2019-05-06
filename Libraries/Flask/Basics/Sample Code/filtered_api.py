import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

fruits = [
    {   
        'id' : 0,
        'name' : 'watermelon',
        'price' : 12
    },
    {
        'id' : 1,
        'name' : 'banana',
        'price' : 20
    },
    {
        'id' : 2,
        'name' : 'orange',
        'price' : 100
    }
]

@app.route("/", methods=['GET'])
def home():
    return ''' 
    <h1>Welcome to the fruit API</h1>
    <p>You pick a fruit from here.</p>
    '''

@app.route('/api/v1/resources/fruits', methods=['GET'])
def get_fruit():
    selected_fruits = []
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return '''
        <p>Ah oh, no id provided :(</p>
        '''
    
    for fruit in fruits:
        if(fruit['id'] == id):
            selected_fruits.append(fruit)
    
    return jsonify(selected_fruits)

@app.route('/api/v1/resources/fruits/all')
def get_all_fruits():
    return jsonify(fruits)

app.run()