"""Constants for Chilicon Cloud integration"""

DOMAIN = "chiliconcloud"

CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_INSTALLATION_HASH = "installation_hash"

ROOT_URL = 'https://cloud.chiliconpower.com'
LOGIN_URL = ROOT_URL + '/login'
INSTALLATION_URL = ROOT_URL + '/installation/' #and then hash
UPDATE_URL = ROOT_URL + '/ajax/fetchOwnerUpdate' #and then ?today=2020-01-23
