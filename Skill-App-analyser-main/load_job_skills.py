import sqlite3
import pandas as pd

conn = sqlite3.connect('skills.db')
cursor = conn.cursor()

df_skills = pd.read_csv('data/Skills.csv')
df_occupations = pd.read_csv('data/Occupation Data.csv')
soc_column = [col for col in df_occupations.columns if 'SOC' in col.upper()][0]

# List of job codes to load (add more from your Skills.csv)
job_codes = ['11-1011.00', '13-1111.00', '11-1021.00']  # Chief Executives, Management Analysts, General Managers
print(f"Loading skills for job codes: {job_codes}")

inserted = 0
for job_code in job_codes:
    # Get job title
    job_title = df_occupations[df_occupations[soc_column] == job_code]['Title'].iloc[0] if not df_occupations[df_occupations[soc_column] == job_code].empty else f"Unknown Job {job_code}"

    # Filter skills
    job_skills_all = df_skills[df_skills['O*NET-SOC Code'] == job_code]
    if job_skills_all.empty:
        print(f"No skills found for {job_code} ({job_title})")
        continue
    job_skills = job_skills_all[df_skills['Scale ID'] == 'IM']
    high_importance_skills = job_skills[job_skills['Data Value'] > 2.5]['Element Name'].drop_duplicates().tolist()
    print(f"Skills for {job_title}: {len(high_importance_skills)}")

    # Insert
    for skill in high_importance_skills:
        cursor.execute("INSERT OR IGNORE INTO JobSkills (JobRole, RequiredSkill) VALUES (?, ?)", (job_title, skill))
        inserted += 1

conn.commit()
conn.close()
print(f"Loaded {inserted} job skills for {len(job_codes)} roles. Sample for {job_title}: {high_importance_skills[:5]}")