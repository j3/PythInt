# Importing modules
from http.client import FOUND
import sys
import linecache
import requests
import json
import urllib3
# Disable requests and urllib3 certificate warnings https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def research(mail, isitarealemailapi, leakcheckapi):
    '''
    Ask if the user want to search the email locally only or using api services too.
    '''
    reponse = input("Activate API services ? o[yes]/n[no] (default no)")
    reponse = reponse.strip().lower()
    if reponse.startswith('o'):
        api_search(mail, leakcheckapi)
        api_validate(mail, isitarealemailapi)
        local_search(mail)
    else:
        local_search(mail)

def api_search(mail, leakcheckapi):
    '''
    If the user say 'o' in the research function then this fuction will research the email on the api of leakcheck.net.
    '''
    headers_dict = {'Accept':'application/json'}
    rep = requests.get('https://leakcheck.net/api?key=' + leakcheckapi + '&check=' + mail + '&type=email', verify = False)
    response = rep.text
    data = json.loads(response)
    if data["success"] == False:
        if data["error"] == "Not found":
            print(mail+" not found by leakcheck.net.")
        elif data["error"] == "IP linking is required":
            print("You need to link your ip on the leakcheck.net api page.")
        else:
             print("Unknown leakcheck.net error.")
    else:
        found = data["found"]
        for i in data["result"]:
            line = (i["line"])
            sources = (i["sources"])
            last_breach = (i["last_breach"])
            print(sources,"|",last_breach,":",line)

def api_validate(mail, isitarealemailapi):
    '''
    Function to see if a given email exist (with isitarealemail API).
    '''
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': mail},headers = {'Authorization': "Bearer " + isitarealemailapi}, verify = False)
    data = response.json()
    status = data['status']
    if status == "valid":
        return "The email seems invalid"
    elif status == "invalid":
        return None
    else:
        return None

def local_search(mail):
    '''
    Function that search the email in an "optimized" way by searching on the files that have already been sorted.
    '''
    folder1 = mail[0]
    folder2 = mail[1]
    
    fichiertxt = open("sorteddbs/"+folder1+"/"+folder2+"/"+folder1+folder2+".txt", "r", encoding="utf8")
    flag = 0
    i = 0
    for line in fichiertxt:
        i = i + 1
        if mail in line:
            flag = 1
            line = i
            ligne = linecache.getline("sorteddbs/"+folder1+"/"+folder2+"/"+folder1+folder2+".txt", line)
            print(ligne)
            break
    if flag == 0:
       print('Email ('+mail+') not found in local databases.')

# https://github.com/SoikRs/PythInt