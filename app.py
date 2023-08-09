from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, It's working!", 200


@app.route('/submit')
def submit():
    # Extract the query parameters from the URL
    company_name = request.args.get('CompanyName')
    client_name = request.args.get('ClientName')
    phone = request.args.get('Phone')

    # Create the body for the POST request
    body = {
        "Company Name": company_name,
        "Client Name": client_name,
        "Phone": phone
    }

    # Send the POST request to the specified URL
    url = "https://prod-164.westeurope.logic.azure.com:443/workflows/d56a85dbe1d64cd3bf77c41c2b0b8b65/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=QY7r_fRgGdOZeJSVn836RE4hT2eKJmqUDCua_XThC3c"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=body, headers=headers)

    # Return a response to the client
    if response.status_code == 202:
        return "Request was successful!", 202
    else:
        return f"Request failed with status code {response.status_code}: {response.text}", 400

def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == '__main__':
    app.run()

