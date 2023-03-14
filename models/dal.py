"""
dal.py
-------

Implements the model for our website by simulating database.

Note - although this is nice as an simple example, in real-world project
we do not use global object for application data.
"""

import json

def load_db():
    with open("/Users/prashant/PICT/VELOCITY 5Nov/miniflask_v2/models/flaskcard_db.json") as foo:
        return json.load(foo)


db = load_db()
