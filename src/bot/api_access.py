import os

import requests

API_KEY = os.environ.get("API_KEY","")
clanTag = os.environ.get("CLAN_TAG", "%2328C9UPJU2")
API_URL = os.environ.get("API_URL", "https://api.clashofclans.com/v1")

def get_current_war():
    war_data = requests.get(API_URL + "/clans/" + clanTag + "/currentwar",
                            headers={"Authorization": "Bearer " + API_KEY}).json()
    return war_data
