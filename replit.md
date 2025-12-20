# Student Careers Website

## Overview
A Flask-based website designed to help students explore various career paths and make informed decisions about their future.

## Project Structure
```
/
├── main.py           # Flask application entry point
├── templates/        # Jinja2 HTML templates
│   ├── base.html     # Base template with common layout
│   ├── index.html    # Homepage with career listings
│   ├── career.html   # Individual career detail page
│   ├── about.html    # About page
│   ├── resources.html# Career resources page
│   └── 404.html      # Error page
├── static/
│   └── css/
│       └── style.css # Main stylesheet
├── pyproject.toml    # Python dependencies
└── README.md         # Project description
```

## Running the Application
- The Flask server runs on `0.0.0.0:5000`
- Run command: `python main.py`

## Features
- Browse career options with descriptions, salary ranges, and skill requirements
- Individual career detail pages
- About and Resources sections
- Responsive design for mobile and desktop

## Technologies
- Python 3.11
- Flask 3.x
- Jinja2 templating
- CSS3 with modern layout (Grid, Flexbox)
