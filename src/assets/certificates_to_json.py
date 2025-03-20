import pandas as pd
import json

file_path = 'professional_certificates.xlsx'

try:
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower()

except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit(1)

certificates = []

for index, row in df.iterrows():
    try:
        certificate = {
             'provider': row['provider'],
            'name': row['name'],
            'slug': row['slug'],
            'industry': row['industry'],
            'domain': row['domain'],
            'level': row['level'],
        }
        certificates.append(certificate)
    except KeyError as e:
        print(f"Missing expected column in the Excel file: {e}")
        continue

try:
    with open('certificates.json', 'w') as f:
        json.dump(certificates, f, indent=4)
except Exception as e:
    print(f"Error writing the JSON file: {e}")