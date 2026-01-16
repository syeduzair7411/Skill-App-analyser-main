import pandas as pd

# Load Skills.csv
df_skills = pd.read_csv('data/Skills.csv')

# Check unique job codes
job_codes = df_skills['O*NET-SOC Code'].unique()
print("Unique job codes in Skills.csv:", job_codes.tolist())

# Check for Data Scientist (15-2051.00)
data_scientist_skills = df_skills[df_skills['O*NET-SOC Code'] == '15-2051.00']
if not data_scientist_skills.empty:
    print(f"Found {len(data_scientist_skills)} rows for Data Scientist (15-2051.00):")
    print(data_scientist_skills[['O*NET-SOC Code', 'Element Name', 'Scale ID', 'Data Value']].head())
else:
    print("No rows found for Data Scientist (15-2051.00) in Skills.csv.")