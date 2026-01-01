# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    return create_engine(
        DATABASE_URL,
        pool_recycle=300,
        pool_pre_ping=True
    )


engine = get_connection()

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        # Convert rows to dictionaries for easier access
        return [dict(row._mapping) for row in rows]
        
##get jobs from db
def get_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        # Convert to list of dictionaries
        return [dict(row._mapping) for row in result_all]

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, phone, linkedin, github, cover_letter) VALUES (:job_id, :full_name, :email, :phone, :linkedin, :github, :cover_letter)")
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "phone": data['phone'],
            "linkedin": data.get('linkedin'),
            "github": data.get('github'),
            "cover_letter": data['cover_letter']
        })
        conn.commit()

def get_applications_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT a.*, j.title as job_title FROM applications a JOIN jobs j ON a.job_id = j.id"))
        apps = [dict(row._mapping) for row in result]
    return apps

def update_application_status(app_id, status):
    with engine.connect() as conn:
        # Update status
        conn.execute(text("UPDATE applications SET status = :s WHERE id = :id"), {"s": status, "id": app_id})
        conn.commit()
        
        # Get application and job details for the email
        result = conn.execute(text("SELECT a.*, j.title as job_title FROM applications a JOIN jobs j ON a.job_id = j.id WHERE a.id = :id"), {"id": app_id})
        row = result.first()
        if row:
            return dict(row._mapping)
    return None
