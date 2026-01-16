import sqlite3
import pandas as pd

def analyze_gaps(student_id, job_role='Chief Executives'):
    conn = sqlite3.connect('skills.db')

    # Debug: Check data
    job_roles = pd.read_sql_query("SELECT DISTINCT JobRole FROM JobSkills", conn)['JobRole'].tolist()
    student_ids = pd.read_sql_query("SELECT DISTINCT StudentID FROM StudentSkills", conn)['StudentID'].tolist()
    print(f"Available Job Roles: {job_roles}")
    print(f"Available Student IDs: {student_ids}")

    # Get all job skills
    query_job_skills = "SELECT DISTINCT RequiredSkill FROM JobSkills WHERE JobRole = ?"
    job_skills = pd.read_sql_query(query_job_skills, conn, params=(job_role,))['RequiredSkill'].tolist()

    # Get student skills
    query_student_skills = "SELECT DISTINCT Skill FROM StudentSkills WHERE StudentID = ?"
    student_skills = pd.read_sql_query(query_student_skills, conn, params=(student_id,))['Skill'].tolist()

    # Find missing skills
    missing_skills = [skill for skill in job_skills if skill not in student_skills]

    # Calculate coverage
    total_job_skills = len(job_skills) if job_skills else 1  # Avoid division by zero
    matched_skills = len([skill for skill in student_skills if skill in job_skills])
    coverage = (matched_skills * 100.0 / total_job_skills) if total_job_skills > 0 else 0

    conn.close()

    return {
        'student_id': student_id,
        'job_role': job_role,
        'coverage_%': coverage,
        'missing_skills': missing_skills,
        'recommendations': [f"Take course in {skill}" for skill in missing_skills[:3]]
    }

# Test
result = analyze_gaps('Student_001')
print(result)