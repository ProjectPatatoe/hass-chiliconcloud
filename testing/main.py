"""
    Python Example of API Call to the Chilicon Power Cloud
"""
import json
import requests

# Get credentials from file
with open('config.json', 'r') as configfile:
    config=json.loads(configfile.read())

print('username: ', config['username'])
print('password: ', config['password'])
print('installation_hash: ', config['installation_hash'])


# Credentials for authentication - TODO: Change for each user
USERNAME = config['username']  # put correct usename here
PASSWORD = config['password']  # put correct password here

# URL paths
URL_root = 'https://cloud.chiliconpower.com'  # cloud main URL
login_URL = URL_root + '/login'
INSTALLATION_HASH = config['installation_hash']  # can be found in the URL when
# accessing that site in a browser
INSTALLATION_URL = URL_root + '/installation/' + INSTALLATION_HASH
fetchOwnerUpdate_URL = URL_root + '/ajax/fetchOwnerUpdate?today=%s'

session = requests.session()  # create a session object to persist the login session across all our requests

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

form_data = {
    'username': USERNAME,
    'password': PASSWORD,
    'Login': 'Login'
}

# Authenticate
print("\n____________LOGIN_POST_______")
r = session.post(login_URL, data=form_data, headers=req_headers, allow_redirects=False)
print("Request Headers: %s" % r.headers)
print("Request Status Code: %s" % r.status_code)
print("Request Text: %s" % r.text)

# Read data
url = fetchOwnerUpdate_URL % '2021-03-03'
r2_headers = {
    'Host': 'cloud.chiliconpower.com',
    'Referer': INSTALLATION_URL
}
r2 = session.get(url, headers=r2_headers)
print("\n____________DATA_____________")
print(r2.headers)
print(r2.status_code)
print(r2.text)

print("\n____________PARSED RESULTS___")
[today, lifetimeEnergy, currentProduction] = json.loads(r2.text)
print("Lifetime Energy = ", lifetimeEnergy)
print("Current Production = ", currentProduction)
