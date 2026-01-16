import streamlit as st
import sqlite3
import pandas as pd

st.title("Automated Skill Gap Analyzer")

conn = sqlite3.connect('skills.db')
student_ids = pd.read_sql_query("SELECT DISTINCT StudentID FROM StudentSkills", conn)['StudentID'].tolist()
job_roles = pd.read_sql_query("SELECT DISTINCT JobRole FROM JobSkills", conn)['JobRole'].tolist()
conn.close()

if not student_ids or not job_roles:
    st.error("No data in JobSkills or StudentSkills. Run load_job_skills.py and load_student_skills.py.")
else:
    student_id = st.selectbox("Select Student ID", student_ids)
    job_role = st.selectbox("Select Job Role", job_roles)

    if st.button("Analyze Gaps"):
        conn = sqlite3.connect('skills.db')
        job_skills = pd.read_sql_query("SELECT DISTINCT RequiredSkill FROM JobSkills WHERE JobRole = ?", conn, params=(job_role,))['RequiredSkill'].tolist()
        student_skills = pd.read_sql_query("SELECT DISTINCT Skill FROM StudentSkills WHERE StudentID = ?", conn, params=(student_id,))['Skill'].tolist()
        conn.close()

        missing_skills = [skill for skill in job_skills if skill not in student_skills]
        total_job_skills = len(job_skills) if job_skills else 1
        matched_skills = len([skill for skill in student_skills if skill in job_skills])
        coverage = (matched_skills * 100.0 / total_job_skills) if total_job_skills > 0 else 0

        st.write(f"**Student ID**: {student_id}")
        st.write(f"**Job Role**: {job_role}")
        st.write(f"**Skill Coverage**: {coverage:.2f}%")
        st.write(f"**Missing Skills**: {', '.join(missing_skills)}")
        st.write(f"**Recommendations**: {', '.join([f'Take course in {s}' for s in missing_skills[:3]])}")

        df_chart = pd.DataFrame({'StudentID': [student_id], 'Coverage_%': [coverage]})
        st.bar_chart(df_chart.set_index('StudentID'))