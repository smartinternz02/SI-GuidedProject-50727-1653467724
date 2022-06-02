import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "A4M0hSoy-nfCNTQ7VtiP7MLHcTRJHKlDCMbVjkX3Ygqz"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields":[["f0","f1","f2","f3","f4","f5","f6","f7","f8"]], "values": [[0.51337409,-1.10962,0.29948929,0.67721181,0.72843001,0.41661337,-1.58160954,-1.1640214,-0.11265796]] }]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/41f82949-cdb6-4c3f-b453-97afce0fcdd9/predictions?version=2022-06-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
pred = response_scoring.json()
output = pred['predictions'][0]['values'][0][0][0]
print(output)