#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states')
def states():
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)


@app.route('/states/<id>')
def states_by_id(id):
    state = None
    states = storage.all("State").values()
    for s in states:
        if s.id == id:
            state = s
    return render_template("9-states.html", state=state)

@app.teardown_appcontext
def end_session(e):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
