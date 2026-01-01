from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_mail import Mail, Message
import os
from database import get_jobs_from_db, load_job_from_db, add_application_to_db, get_applications_from_db, update_application_status

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev_key_123')

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Static admin credentials for testing
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

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
    add_application_to_db(job_id, data)
    
    # Attempt to send confirmation email
    if app.config.get('MAIL_USERNAME') and app.config.get('MAIL_PASSWORD'):
        try:
            msg = Message(
                'Application Submitted Successfully',
                sender=app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            msg.body = f"Hello {data['full_name']},\n\nYour application for the position has been successfully submitted. We will reach out to you later after reviewing your profile.\n\nBest regards,\nStudent Careers Team"
            mail.send(msg)
        except Exception as e:
            # Log the error but don't fail the request
            print(f"DEBUG: Email sending failed: {e}")
    else:
        print("DEBUG: Email credentials not configured. Skipping email.")
        
    return render_template("application_submitted.html", application=data)


@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        return render_template("admin_login.html", error="Invalid credentials")
    return render_template("admin_login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    apps = get_applications_from_db()
    return render_template("admin_dashboard.html", applications=apps)

@app.route("/admin/application/<int:app_id>/status", methods=['POST'])
def update_status(app_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    new_status = request.form.get('status')
    app_data = update_application_status(app_id, new_status)
    
    if app_data:
        # Send status update email
        if app.config.get('MAIL_USERNAME') and app.config.get('MAIL_PASSWORD'):
            try:
                subject = f"Update on your application for {app_data['job_title']}"
                msg = Message(
                    subject,
                    sender=app.config['MAIL_USERNAME'],
                    recipients=[app_data['email']]
                )
                if new_status == 'accepted':
                    body = f"Hello {app_data['full_name']},\n\nWe are pleased to inform you that your application for the {app_data['job_title']} position has been accepted. We will contact you soon with the next steps."
                else:
                    body = f"Hello {app_data['full_name']},\n\nThank you for your interest in the {app_data['job_title']} position. Unfortunately, we have decided not to proceed with your application at this time."
                
                msg.body = body + "\n\nBest regards,\nStudent Careers Team"
                mail.send(msg)
            except Exception as e:
                print(f"DEBUG: Status email failed: {e}")
            
    return redirect(url_for('admin_dashboard'))

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
