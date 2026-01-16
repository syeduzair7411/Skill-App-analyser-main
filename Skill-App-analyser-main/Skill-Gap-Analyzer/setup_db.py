import sqlite3

conn = sqlite3.connect('skills.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS JobSkills (
    JobRole TEXT,
    RequiredSkill TEXT,
    PRIMARY KEY (JobRole, RequiredSkill)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS StudentSkills (
    StudentID TEXT,
    Skill TEXT,
    PRIMARY KEY (StudentID, Skill)
)
''')

conn.commit()
conn.close()