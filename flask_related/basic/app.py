import flask
import utils

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def start():
    if flask.request.method == "POST":
        gpa = utils.calculate_gpa(flask.request.form.values())
        return flask.render_template("results.html", gpa=gpa)

    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
