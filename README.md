# Student Careers Website

A professional Flask-based job portal designed to help students explore various career paths and apply for opportunities. This project features dynamic job listings and a secure application system integrated with a database.




## Features
- **Dynamic Job Listings**: View up-to-date career opportunities fetched from a database.
- **Detailed Job Pages**: Each job has a dedicated page showing responsibilities, requirements, and salary.
- **Application System**: Integrated form for students to submit applications (Name, Email, Phone, Links, Cover Letter).
- **Database Integration**: Secure storage for both job listings and applicant data.
- **Responsive Design**: Built with Bootstrap 5 to ensure a great experience on mobile and desktop.
- **Connection Stability**: Includes SQLAlchemy connection pooling and pre-pinging to ensure reliable database access.

## Tech Stack
- **Backend**: Python with Flask
- **Database**: SQL (MySQL/PostgreSQL compatible)
- **ORM**: SQLAlchemy
- **Frontend**: HTML5, Jinja2, Bootstrap 5, CSS3

## Project Structure
```
/
├── app.py              # Main Flask application and routing
├── database.py         # Database connection and CRUD operations
├── static/             # Static assets (CSS, Images, SVGs)
│   ├── css/style.css
│   ├── banner.jpg
│   └── job.svg
├── templates/          # HTML Templates (Jinja2)
│   ├── home.html       # Homepage with job listings
│   ├── jobfrom.html    # Application form
│   ├── navbar.html     # Navigation partial
│   ├── footer.html     # Footer partial
│   └── application_submitted.html # Success page
└── replit.md           # Project configuration for Replit
```

## Setup and Running
1. **Install Dependencies**:
   ```bash
   pip install flask sqlalchemy pymysql psycopg2-binary
   ```
2. **Environment Variables**:
   Ensure `DATABASE_URL` is set in your environment.
3. **Run Application**:
   ```bash
   python app.py
   ```
   The server will start on `0.0.0.0:5000`.

## Database Schema
The project uses two main tables:
- `jobs`: Stores job titles, locations, descriptions, and salaries.
- `applications`: Stores applicant details and links them to job IDs.
