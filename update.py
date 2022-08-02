import os
import requests
from dotenv import load_dotenv
load_dotenv()

scriptPath = os.path.join(os.getcwd(), 'bin', 'compile')
latestFFVer = requests.get("https://product-details.mozilla.org/1.0/firefox_versions.json").json()['LATEST_FIREFOX_VERSION']
latestgeckoVer = requests.get("https://api.github.com/repos/mozilla/geckodriver/releases").json()[0]['name']
supportedHeroku = list(filter(lambda x: x.startswith("heroku"), list(map(lambda x: x['stack']['name'].lower(), requests.get(os.environ.get("GH_URL")).json()['data']))))


with open(scriptPath) as f:
    data = f.readlines()
data[38] = f"VERSION_FIREFOX={latestFFVer}\n"
data[39] = f"VERSION_GECKODRIVER={latestgeckoVer}\n"
data[53] = '  "' + '" | "'.join(supportedHeroku) + '")\n'
with open(scriptPath, 'w') as f:
    f.writelines(data)
