from flask import Flask, render_template, jsonify

from database import get_jobs_from_db

app = Flask(__name__)


@app.route('/')
def home():
    jobs = get_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/job")
def getjobs():
    jobs = get_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
