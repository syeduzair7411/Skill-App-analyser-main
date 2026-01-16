# Skill Gap Analyzer

## Overview
The Skill Gap Analyzer is a project designed to help users identify skill gaps between student skills and job requirements. It utilizes a SQLite database to store and retrieve data related to job roles and student skills, providing insights into areas for improvement.

## Project Structure
```
Skill-Gap-Analyzer
├── app.py
├── analyse_gaps.py
├── bugs.py
├── load_job_skills.py
├── load_student_skills.py
├── setup_db.py
├── data
│   ├── Skills.csv
│   └── Occupation Data.csv
├── README.md
```

## Files Description

- **app.py**: Contains the Streamlit application that allows users to analyze skill gaps based on student skills and job requirements. It connects to a SQLite database to retrieve and display relevant data.

- **analyse_gaps.py**: Defines the `analyze_gaps` function that takes a student ID and job role as parameters. It connects to the SQLite database, retrieves job skills and student skills, calculates skill coverage, and identifies missing skills.

- **bugs.py**: Loads the `Skills.csv` data, checks for unique job codes, and retrieves skills specific to the Data Scientist job role (15-2051.00) from the dataset.

- **load_job_skills.py**: Loads job skills from the `Skills.csv` and `Occupation Data.csv` files into the SQLite database. It filters skills based on job codes and inserts them into the `JobSkills` table.

- **load_student_skills.py**: Loads student skills from a CSV file (`coursea_data.csv`), maps course titles to skills, and inserts the skills into the `StudentSkills` table in the SQLite database.

- **setup_db.py**: Sets up the SQLite database by creating two tables: `JobSkills` and `StudentSkills`, which store job roles and required skills, and student IDs and skills, respectively.

- **data/Skills.csv**: Contains skills associated with various job roles, including their O*NET-SOC codes and importance ratings.

- **data/Occupation Data.csv**: Contains job titles and their corresponding O*NET-SOC codes.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd Skill-Gap-Analyzer
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python setup_db.py
   ```

5. Load job skills and student skills:
   ```
   python load_job_skills.py
   python load_student_skills.py
   ```

6. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

## Usage
- Open the Streamlit application in your web browser.
- Select a student ID and job role from the dropdown menus.
- Click on "Analyze Gaps" to view skill coverage and missing skills.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.