from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    "id": "1",
    "title": "Android Developer",
    "description":
    "Android Developer is responsible for developing and maintaining Android applications. They work with a team of developers, designers, and product managers to create high-quality applications that meet the needs of users.",
    "location": "Bengaluru",
    "salary": "Rs. 10,00,000"
}, {
    "id": "2",
    "title": "Data Scientist",
    "description":
    "Data Scientist is responsible for collecting, analyzing, and interpreting large data sets to help an organization understand and optimize its business processes.",
    "location": "Delhi",
    "salary": "Rs. 15,00,000"
}, {
    "id": "3",
    "title": "Frontend Engineer",
    "description":
    "Frontend Engineer is responsible for developing and maintaining the user interface of a website or web application. They work with a team of developers, designers, and product managers to create a seamless and engaging user experience.",
    "location": "Remote",
    "salary": "Rs. 12,00,000"
}, {
    "id": "4",
    "title": "Backend Engineer",
    "description":
    "Backend Engineer is responsible for developing and maintaining the server-side logic of a website or web application. They work with a team of developers, designers, and product managers to create a robust and scalable backend infrastructure.",
    "location": "San Francisco",
    "salary": "$120,000"
}]


@app.route('/')
def home():
  return render_template("home.html", jobs=jobs)

@app.route("/job")
def  getjobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
