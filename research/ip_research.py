# Importing modules
import re
import requests
import json
import urllib3
# Disable requests and urllib3 certificate warnings https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_ip(research):
    '''
    Search in the given line something that correspond to the regex of an ip.
    '''
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip = re.findall(re_ip,research)
    print("IP present in the line (",ip[0], "), API localisation :" )
    locate(ip)

def locate(ip):
    '''
    Function that get the ip informations from an API and return it.
    '''
    rep = requests.get('https://geolocation-db.com/json/' + ip[0], verify = False)
    response = rep.text
    data = json.loads(response)
    print(data)

# https://github.com/SoikRs/PythInt