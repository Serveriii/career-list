import pandas as pd
import json

file_path = 'industry_content.xlsx'

try:
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower()

except Exception as e:
    exit(1)

industry_contents = []

for index, row in df.iterrows():
    try:
        content = {
           'course': row['course name'],
           'partner': row['partner'],
           'asset_type': row['asset type'],
           'difficulty': row['difficulty'],
           'estimated_hours': row['estimated hours'] if not pd.isnull(row['estimated hours']) else None,
           'url': row['url'],
           'description': row['description'] if not pd.isnull(row['description']) else None,
           'specialization': row['specialization'] if not pd.isnull(row['specialization']) else None,
           'specialization_url': row['specialization url'] if not pd.isnull(row['specialization url']) else None,
           'career': row['career'] if not pd.isnull(row['career']) else None,
           'domain': row['domain'] if not pd.isnull(row['domain']) else None,
           'has_certificate': row['certificate boolean'],
        }
        
        industry_contents.append(content)
    except KeyError as e:
        # print(f"Missing expected column in the Excel file: {e}")
        continue

try:
    with open('industry_content.json', 'w') as f:
        json.dump(industry_contents, f, indent=4)
except Exception as e:
    print(f"Error writing the JSON file: {e}")