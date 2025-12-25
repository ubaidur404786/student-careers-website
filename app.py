from flask import Flask, render_template, jsonify, request
from flask_mail import Mail, Message
import os
from database import get_jobs_from_db, load_job_from_db, add_application_to_db, get_applications_from_db

app = Flask(__name__)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    jobs = get_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    # job is a list of rows from database.plect *
    # let's make sure we pass the first row object
    return render_template("jobfrom.html", job=job[0])


@app.route("/applyjob", methods=['POST'])
def apply_to_job():
    data = request.form
    job_id = data.get('job_id')
    # We could also get job_title from form if needed, but job_id is enough for DB
    add_application_to_db(job_id, data)
    
    # Send confirmation email
    try:
        msg = Message(
            'Application Submitted Successfully',
            sender=app.config['MAIL_USERNAME'],
            recipients=[data['email']]
        )
        msg.body = f"Hello {data['full_name']},\n\nYour application for the position has been successfully submitted. We will reach out to you later after reviewing your profile.\n\nBest regards,\nStudent Careers Team"
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
        
    return render_template("application_submitted.html", application=data)


@app.route("/api/jobs/<id>")
def show_job_api(id):
    job = load_job_from_db(id)
    return jsonify(job)


@app.route("/job_list")
def getjobs():
    jobs = get_jobs_from_db()
    return jsonify(jobs)


@app.route("/applications")
def applications():
    apps = get_applications_from_db()
    return render_template("applications.html", apps=apps)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
