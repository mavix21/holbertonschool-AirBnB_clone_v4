#!/usr/bin/python3
""" This module starts a Flask Web application that listens on 0.0.0.0
    (all network interfaces) and port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
import uuid

app = Flask(__name__)


@app.route("/2-hbnb", strict_slashes=False)
def filters():
    """Renders all states, cities, and amenities stored in the database"""
    context = {
            'states': storage.all(State).values(),
            'amenities': storage.all(Amenity).values(),
            'places': storage.all(Place).values(),
            'users': storage.all(User),
            'cache_id': uuid.uuid4()
            }
    return render_template("2-hbnb.html", **context)


@app.teardown_appcontext
def close_session(self):
    """Removes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
