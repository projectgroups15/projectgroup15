### Student Lifestyle Data App
This project provides a web application built with Flask that allows users to explore and understand data related to student lifestyles and their academic performance.

### Features
Home Page: Welcomes users to the app with an overview of its purpose.
About Page: Describes the dataset, including its structure and key columns.
Data Page: Displays a sample of the dataset in a tabular format.

### Dataset Overview
The application uses a SQLite database named student_lifestyle_dataset.db. The database contains data about students, including the following columns:

* Student_ID: Unique identifier for each student.
* Study_Hours_Per_Day: Daily hours spent studying.
* Extracurricular_Hours_Per_Day: Hours dedicated to extracurricular activities each day.
* Sleep_Hours_Per_Day: Daily hours of sleep.
* Social_Hours_Per_Day: Time spent on social activities daily.
* Physical_Activity_Hours_Per_Day: Daily hours spent on physical activity.
* GPA: Grade Point Average.
* Stress_Level: Stress level categorized as Low, Moderate, or High.

#### Installation
Clone the repository and navigate to the project directory.
Ensure Python is installed (Python 3.7 or later recommended).

#### Install dependencies using pip:
pip install flask pandas sqlite3

#### Run the Flask app:
python app.py

#### File Structure
* app.py: The main application file containing routes and core functionality.
* student_lifestyle_dataset.db: SQLite database containing the dataset.
* templates/: Folder for HTML templates (if applicable in future updates).
* static/: Folder for static files such as CSS and JavaScript (if applicable).
