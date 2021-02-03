import requests
import json

cases_endpt = 'https://api.gdc.cancer.gov/cases'

# The 'fields' parameter is passed as a comma-separated string of single names.
fields = [
    "submitter_id",
    "case_id",
    "primary_site",
    "disease_type",
    "diagnoses.vital_status"
    ]

fields = ','.join(fields)

params = {
    "fields": fields,
    "size": "100"
    }

response = requests.get(cases_endpt, params = params)

print(json.dumps(response.json(), indent=3))