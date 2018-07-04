from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Letterify is service to extract letters from images."


@app.route("/api/")
def upload():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
