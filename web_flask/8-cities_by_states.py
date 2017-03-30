#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def show_states():
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def show_cities():
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_session(e):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
