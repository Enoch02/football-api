from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def root():
    message = {"greetings": "Welcome to my football streaming api"}
    response = jsonify(message)

    return response


@app.route("/live_matches")
def get_matches(): ...


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found " + request.url}
    response = jsonify(message)

    response.status_code = 404

    return response


if __name__ == "__main__":
    app.run(debug=True)
