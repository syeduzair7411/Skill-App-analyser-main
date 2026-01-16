import sqlite3
import pandas as pd

conn = sqlite3.connect('skills.db')
cursor = conn.cursor()

def map_course_to_skills(course_title):
    skill_map = {
        'python': ['python', 'programming', 'critical thinking', 'complex problem solving'],
        'data science': ['machine learning', 'data analysis', 'sql', 'statistics', 'critical thinking'],
        'machine learning': ['machine learning', 'ai', 'neural networks', 'complex problem solving'],
        'sql': ['sql', 'database management', 'active learning'],
        'excel': ['excel', 'data visualization', 'critical thinking'],
        'project management': ['project management', 'agile', 'scrum', 'management'],
        'business': ['business strategy', 'management', 'critical thinking', 'active listening'],
        'crash course in data science': ['data science', 'data analysis', 'critical thinking'],
        'ai for everyone': ['ai', 'machine learning', 'complex problem solving'],
        'aws': ['cloud computing', 'aws', 'systems evaluation'],
        'cybersecurity': ['cybersecurity', 'systems security', 'systems analysis'],
        'data analysis': ['data analysis', 'statistics', 'critical thinking'],
        'deep learning': ['deep learning', 'neural networks', 'complex problem solving'],
        'tableau': ['data visualization', 'tableau', 'critical thinking'],
        'r programming': ['r', 'data analysis', 'active learning'],
    }
    course_lower = course_title.lower()
    for key in skill_map:
        if key in course_lower:
            return skill_map[key]
    return []

df_students = pd.read_csv('data/coursea_data.csv')
print(f"First 5 course titles: {df_students['course_title'].head().tolist()}")
df_students['student_skills'] = df_students['course_title'].apply(map_course_to_skills)

unmatched = df_students[df_students['student_skills'].apply(len) == 0]['course_title'].tolist()
print(f"Unmatched course titles (first 5): {unmatched[:5]}")

df_students['StudentID'] = [f"Student_{i+1:03d}" for i in range(len(df_students))]

inserted = 0
for _, row in df_students.iterrows():
    student_id = row['StudentID']
    for skill in row['student_skills']:
        cursor.execute("INSERT OR IGNORE INTO StudentSkills (StudentID, Skill) VALUES (?, ?)", (student_id, skill))
        inserted += 1

cursor.execute("SELECT DISTINCT Skill FROM StudentSkills")
loaded_skills = [row[0] for row in cursor.fetchall()]
print(f"Loaded skills: {loaded_skills}")

conn.commit()
conn.close()
print(f"Loaded {inserted} student skills into StudentSkills table.")
print(f"Sample: First student skills: {df_students['student_skills'].iloc[0]}")