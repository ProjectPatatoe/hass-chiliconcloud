"""
    Python Example of API Call to the Chilicon Power Cloud
    with aiohttp instead
"""
import json
import aiohttp
import asyncio

# Get credentials from file
with open('testing/config.json', 'r') as configfile:
    config=json.loads(configfile.read())

#print('username: ', config['username'])
#print('password: ', config['password'])
#print('installation_hash: ', config['installation_hash'])


# Credentials for authentication
USERNAME = config['username']  # put correct usename here
PASSWORD = config['password']  # put correct password here

# URL paths
URL_root = 'https://cloud.chiliconpower.com'  # cloud main URL
login_URL = URL_root + '/login'
INSTALLATION_HASH = config['installation_hash']  # can be found in the URL when
# accessing that site in a browser
INSTALLATION_URL = URL_root + '/installation/' + INSTALLATION_HASH
#fetchOwnerUpdate_URL = URL_root + '/ajax/fetchOwnerUpdate?today=%s'
fetchOwnerUpdate_URL = URL_root + '/ajax/fetchOwnerUpdate'



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
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(login_URL,data=form_data,headers=req_headers) as resp:
            print("Request Headers: %s" % resp.headers)
            print("Request Status Code: %s" % resp.status)
            print("Request Text: %s" % await resp.text())

# Read data
        req2_headers = {
            'Host': 'cloud.chiliconpower.com',
            'Referer': INSTALLATION_URL
        }
        async with session.get(fetchOwnerUpdate_URL, params={'today':'2021-03-03'}, headers=req2_headers) as resp2:
            print("\n____________DATA_____________")
            print(resp2.headers)
            print(resp2.status)
            print(await resp2.text())

            print("\n____________PARSED RESULTS___")
            [today, lifetimeEnergy, currentProduction] = json.loads(await resp2.text())
            print("Today = ", today)
            print("Lifetime Energy = ", lifetimeEnergy)
            print("Current Production = ", currentProduction)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())