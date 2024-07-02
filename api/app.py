from flask import Flask, abort, jsonify, request

from api.util import list_endpoints
from scraper.model.live_matches import NS247LiveMatches
from scraper.ns247_scraper import Ns247Scraper

app = Flask(__name__)
ns_scraper = Ns247Scraper()


@app.route("/")
def root():
    available_endpoints = list_endpoints(app)
    message = {
        "greetings": "Welcome to my football streaming api",
        "endpoints": available_endpoints[1:]
    }
    response = jsonify(message)

    return response


@app.route("/get_matches/<int:source>")
def get_matches(source: int):
    live_matches: NS247LiveMatches = None
    message = {"error": "Invalid source selected"}

    try:
        match source:
            case 1:
                live_matches = ns_scraper.get_matches()

                return jsonify(live_matches.to_dict())
            case _:
                return jsonify(message)
    except Exception as e:
        message["error"] = str(e)
        return jsonify(message)
    

@app.route("/get_stream/<channel>")
def get_stream(channel: str):
    stream_url = ns_scraper.get_match_stream_link(channel)
    
    if stream_url is None:
        abort(404)
    else:
        message = {"stream_url": stream_url}
        return jsonify(message)


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found " + request.url}
    response = jsonify(message)

    response.status_code = 404

    return response
