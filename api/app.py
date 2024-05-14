from flask import Flask, jsonify, request
from scraper.model.live_matches import LiveMatches
from scraper.ns247_scraper import Ns247Scraper

app = Flask(__name__)
ns_scraper = Ns247Scraper()


@app.route("/")
def root():
    message = {"greetings": "Welcome to my football streaming api"}
    response = jsonify(message)

    return response


@app.route("/live_matches/<int:source>")
def get_matches(source: int):
    live_matches: LiveMatches = None
    message = {"error": "Invalid source selected"}

    match source:
        case 1:
            live_matches = ns_scraper.get_matches()

            return jsonify(live_matches.to_dict())
        case _:
            return jsonify(message)


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found " + request.url}
    response = jsonify(message)

    response.status_code = 404

    return response
