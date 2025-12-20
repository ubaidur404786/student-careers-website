from flask import Flask, render_template

app = Flask(__name__)

careers = [
    {
        "id": 1,
        "title": "Software Engineer",
        "description": "Design, develop, and maintain software applications and systems.",
        "skills": ["Programming", "Problem Solving", "Mathematics", "Communication"],
        "education": "Bachelor's degree in Computer Science or related field",
        "salary_range": "$70,000 - $150,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "description": "Analyze and interpret complex data to help organizations make decisions.",
        "skills": ["Statistics", "Machine Learning", "Python/R", "Data Visualization"],
        "education": "Master's degree in Data Science, Statistics, or related field",
        "salary_range": "$80,000 - $160,000"
    },
    {
        "id": 3,
        "title": "Healthcare Professional",
        "description": "Provide medical care and support to patients in various healthcare settings.",
        "skills": ["Patient Care", "Medical Knowledge", "Empathy", "Attention to Detail"],
        "education": "Medical degree or nursing qualification",
        "salary_range": "$50,000 - $200,000+"
    },
    {
        "id": 4,
        "title": "Financial Analyst",
        "description": "Evaluate financial data and provide investment recommendations.",
        "skills": ["Financial Modeling", "Excel", "Analytical Thinking", "Reporting"],
        "education": "Bachelor's degree in Finance, Economics, or Accounting",
        "salary_range": "$60,000 - $120,000"
    },
    {
        "id": 5,
        "title": "Marketing Manager",
        "description": "Develop and execute marketing strategies to promote products or services.",
        "skills": ["Digital Marketing", "Analytics", "Creativity", "Leadership"],
        "education": "Bachelor's degree in Marketing or Business",
        "salary_range": "$55,000 - $130,000"
    },
    {
        "id": 6,
        "title": "Teacher/Educator",
        "description": "Educate and inspire students across various subjects and age groups.",
        "skills": ["Communication", "Patience", "Subject Expertise", "Classroom Management"],
        "education": "Bachelor's degree in Education plus teaching certification",
        "salary_range": "$40,000 - $80,000"
    }
]

@app.route('/')
def home():
    return render_template('index.html', careers=careers)

@app.route('/career/<int:career_id>')
def career_detail(career_id):
    career = next((c for c in careers if c['id'] == career_id), None)
    if career:
        return render_template('career.html', career=career)
    return render_template('404.html'), 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
