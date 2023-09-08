import os
from datetime import datetime

import requests

API_KEY = os.environ.get("API_KEY","")
clanTag = os.environ.get("CLAN_TAG", "%2328C9UPJU2")
API_URL = os.environ.get("API_URL", "https://api.clashofclans.com/v1")

war_data = requests.get(API_URL + "/clans/" + clanTag + "/currentwar", headers={"Authorization": "Bearer " + API_KEY}).json()

start_time = war_data["startTime"]
date_time_format = "%Y%m%dT%H%M%S.%fZ"
start_time = datetime.strptime(start_time, date_time_format)
print(start_time)
print(war_data)

if datetime.utcnow() < start_time:
    print("War has not started yet.", (start_time - datetime.utcnow()), "until war starts.")
    exit(0)
