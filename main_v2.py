from flask import Flask, render_template, abort, jsonify
from models.dal import db


app = Flask(__name__)


@app.route("/")
def welcome():
    """
    This is welcome API endpoint
    :return:
    """

    return render_template(
        "welcome.html",
        message="Here's message from the view",
    )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]

        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)


@app.route("/api/card/")
def api_card_list():
    """
    NOTE -
    you can use `jsonify` method to explicitly set output to application/json
    :return:
    """
    return jsonify(db)
