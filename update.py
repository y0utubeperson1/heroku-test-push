import os
import requests
from dotenv import load_dotenv
load_dotenv()

scriptPath = os.path.join(os.getcwd(), 'getlatestff')
latestFFVer = requests.get("https://product-details.mozilla.org/1.0/firefox_versions.json").json()['LATEST_FIREFOX_VERSION']
latestgeckoVer = requests.get("https://api.github.com/repos/mozilla/geckodriver/releases").json()[0]['name']
supportedHeroku = list(filter(lambda x: x.startswith("heroku"), list(map(lambda x: x['stack']['name'].lower(), requests.get(os.getenv("GH_URL")).json()['data']))))


with open("getlatestff") as f:
    data = f.readlines()
data[38] = f"VERSION_FIREFOX={latestFFVer}\n"
data[39] = f"VERSION_GECKODRIVER={latestgeckoVer}\n"
data[53] = '  "' + '" | "'.join(supportedHeroku) + '")\n'
with open("FFTestOut", 'w') as f:
    f.writelines(data)
