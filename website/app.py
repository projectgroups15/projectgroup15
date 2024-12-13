from flask import Flask, render_template
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'student_lifestyle_dataset.db') 

def get_data_sample():
    """Fetch a sample of data from the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    query = "SELECT * FROM Students_lifestyle LIMIT 30;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def generate_navbar():
    """Generate a consistent navigation bar for all pages with styling."""
    navbar = (
        "<style>"
        "body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; color: #333; }"
        "nav { background-color: #333; padding: 20px; text-align: center; }"
        "nav a { margin: 0 15px; text-decoration: none; color: white; font-weight: bold; }"
        "nav a:hover { color: #FFD700; }"
        "hr { border: 0; height: 1px; background: #ccc; margin: 20px 0; }"
        "h1, h2 { color: #007BFF; text-align:center;}"
        "p{text-align:center;}"
        "ul { padding-left: 20px; list-style-type: none; padding-left: 30rem}"
        "ul li { margin-bottom: 10px;  }"
        "table { border-collapse: collapse; width: 100%; padding: 0 30px, margin: 20px 0; }"
        "table th, table td { border: 1px solid #ccc; padding: 10px; text-align: left; }"
        "table th { background-color: #007BFF; color: white; }"
        "table tr:nth-child(even) { background-color: #f2f2f2; }"
        "footer { background-color: #333; color: white; text-align: center; padding: 10px 0; position: fixed; width: 100%; bottom: 0; }"
        "</style>"
        "<nav>"
        "<a href='/'>Home</a>"
        "<a href='/about'>About</a>"
        "<a href='/data'>Data</a>"
        "</nav><hr>"
    )
    return navbar

@app.route('/')
def home():
    navbar = generate_navbar()
    return navbar + (
        "<h1>Welcome to the Student Lifestyle Data App</h1>"
        "<p>Explore the dataset via the About and Data pages.</p>"
        "<p>Discover insights about student habits and academic performance.</p>"
    )

@app.route('/about')
def about():
    navbar = generate_navbar()
    about_text = (
        "<h1>About the Data</h1>"
        "<p>This dataset captures various lifestyle metrics of students, including study hours, extracurricular activities, sleep, and more.</p>"
        "<h2>Data Columns:</h2>"
        "<ul>"
        "<li><b>Student_ID</b>: Unique identifier for each student</li>"
        "<li><b>Study_Hours_Per_Day</b>: Daily hours spent studying</li>"
        "<li><b>Extracurricular_Hours_Per_Day</b>: Daily hours spent on extracurricular activities</li>"
        "<li><b>Sleep_Hours_Per_Day</b>: Daily hours of sleep</li>"
        "<li><b>Social_Hours_Per_Day</b>: Daily hours spent in social activities</li>"
        "<li><b>Physical_Activity_Hours_Per_Day</b>: Daily hours spent on physical activity</li>"
        "<li><b>GPA</b>: Grade Point Average</li>"
        "<li><b>Stress_Level</b>: Stress level categorized as Low, Moderate, or High</li>"
        "</ul>"
    )
    return navbar + about_text

@app.route('/data')
def data():
    navbar = generate_navbar()
    df = get_data_sample()
    return navbar + (
        "<h1>Data Sample</h1>"
        "<p>Below is a sample of the data from the dataset:</p>"
        + df.to_html(index=False, border=0, classes='data-table')
    )

if __name__ == '__main__':
    app.run(debug=True)
