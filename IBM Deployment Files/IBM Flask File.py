from flask import Flask, render_template, request

import requests
import pickle

scalar = pickle.load(open("scalar_movies.pkl","rb"))

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "A4M0hSoy-nfCNTQ7VtiP7MLHcTRJHKlDCMbVjkX3Ygqz"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("Demo2.html")

@app.route('/resultnew', methods = ['POST'])
def User():
    b = request.form["bg"]
    c = request.form["ge"]
    d = request.form["pr"]
    e = request.form["rt"]
    f = request.form["va"]
    g = request.form["vc"]
    h = request.form["dc"]
    i = request.form["rm"]
    j = request.form["rd"]
    t = [[float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j)]]
    y = scalar.transform(t)
    k = y[0][0]
    l = y[0][1]
    m = y[0][2]
    n = y[0][3]
    o = y[0][4]
    p = y[0][5]
    q = y[0][6]
    r = y[0][7]
    s = y[0][8]
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields":[["f0","f1","f2","f3","f4","f5","f6","f7","f8"]], "values": [[float(k),float(l),float(m),float(n),float(o),float(p),float(q),float(r),float(s)]] }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/41f82949-cdb6-4c3f-b453-97afce0fcdd9/predictions?version=2022-06-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    pred = response_scoring.json()
    output = pred['predictions'][0]['values'][0][0][0]
    print(output)

    return render_template("resultnew.html",out="The revenue is $"+str(output)+" million")

if __name__ == '__main__':
    app.run(debug = False)