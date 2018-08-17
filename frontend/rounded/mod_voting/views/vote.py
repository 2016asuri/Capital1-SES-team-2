import flask
import firebase_admin
from rounded.core import firebase
from rounded.mod_voting import controller
from rounded.mod_voting.lib import db as voting_db
import json

@controller.route("/vote", methods=["GET"])
def vote():

    db_client = firebase.getDB()

    try:
        raw_charities = voting_db.get_charities(db_client)
    except Exception as e:
        return "Error retrieving charities: " + str(e)

    # processs dictionary
    charities = [
        {
            'name': key,
            'votes': int(raw_charities[key]),
            'description': "I don't feell like writing this",
        } for key in raw_charities
    ]
    charities.sort(key=lambda x: x["votes"], reverse=True)

    _charities = json.dumps(charities)
    return flask.render_template(
        "voting.html",
        charities=charities,
        _charities=_charities,
    )

@controller.route("/vote", methods=["POST"])
def _vote():
    form = flask.request.form

    votedFor = form.get("selectedCharity") 
    db_client = firebase.getDB()

    if votedFor != None:
        voting_db.increment_charity(db_client, votedFor)

    return flask.redirect(flask.url_for("mod_voting.vote"))
