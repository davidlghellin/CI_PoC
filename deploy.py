import json
import sys
import time
import requests
from bs4 import BeautifulSoup


def login_in_dcos(master, user, pwd):
    """
    Function that simulates the login in DCOS flow with SSO to obtain a valid
    cookie that will be used to make requests to Marathon
    """
    # Needed parameters
    url = "https://"+master+"/login?firstUser=false"
    username = user
    password = pwd

    # First request to mesos master to be redirected to gosec sso login
    # page and be given a session cookie
    first_response = requests.get(url, verify=False)
    callback_url = first_response.url
    session_id_cookie = first_response.history[-1].cookies

    # Parse response body for hidden tags needed in the data of our login post request
    body = first_response.text
    parser = BeautifulSoup(body, "lxml")
    hidden_tags = [tag.attrs for tag in parser.find_all("input", type="hidden")]
    data = {tag['name']: tag['value'] for tag in hidden_tags
            if tag['name'] == 'lt' or tag['name'] == 'execution'}

    # Add the rest of needed fields and login credentials in the data of
    # our login post request and send it
    data.update(
        {'_eventId': 'submit',
         'submit': 'LOGIN',
         'username': username,
         'password': password
        }
    )
    login_response = requests.post(callback_url, data=data, cookies=session_id_cookie, verify=False)

    # Obtain dcos cookie from response
    return login_response.history[-1].cookies


if len(sys.argv)<4:
    sys.exit("ERROR! You need to provide three parameters: master-node hostname, user and password")

master = sys.argv[1]
user = sys.argv[2]
pswd = sys.argv[3]

##Obtain cookie
authCookie = login_in_dcos(master, user, pswd)
##Read marathon.json from project
json_data=open("marathon.json").read()
mjson = json.loads(json_data)
##Change ID in order to mark app as test
newId = "/hello-world-host-test"
mjson["id"] = newId
heads = {'Content-type': 'application/json'}

print("\nSending marathon deploy request for "+ newId)
response = requests.post("https://"+master+"/service/marathon/v2/apps", json=mjson, cookies=authCookie, headers=heads ,verify=False)
print("Response: " + str(response.status_code))

print("\nWaiting for marathon... he is a good guy")
time.sleep(2)
print("\nLooking for deployed test-app in marathon")
response = requests.get("https://"+master+"/service/marathon/v2/apps/"+newId, json=mjson, cookies=authCookie, headers=heads ,verify=False)
appstatusjson = json.loads(response.text)

host = appstatusjson['app']['tasks'][0]['host']
port = appstatusjson['app']['tasks'][0]['ports'][0]

url = "http://"+host+":"+str(port)

time.sleep(2)
try:
    response = requests.get(url)
except:
    sys.exit("Cant reach app")