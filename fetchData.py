"""
Henry Rossiter - henry.rossiter@utexas.edu
A Simple UI to simplify data extraction and saving from Strava API
Obtain a Strava Development token here: https://www.strava.com/settings/api
"""

import pip
try:
    import subprocess
except ImportError:
    pip.main(['install',subprocess])
    import subprocess
try:
    import httpie
except ImportError:
    pip.main(['install',httpie])
    import httpie

USER_TOKEN = ""
if len(USER_TOKEN) == 0:
    USER_TOKEN = input("Enter your Strava developer token: ")

url = ""
if len(url)==0:
    print('API Documentation can be found at http://developers.strava.com/docs/reference/#api-Activities')
    print('requests typically start with \'http GET\'\n\n')
    url = input('enter a Strav\a HTTPie GET request: ')

if 'PUT' in url or 'POST' in url:
    print("Sorry, this script cannot handle PUT or POST requests.")
    System.exit(0)

if url[0] == '\"':
    url = 'http GET '+url

url.replace('[[token]]',USER_TOKEN)
subprocess.run(url)


save = input('Would you like to save this data as json locally? (y/n)')
if save.lower()=='y':
    subprocess.run(url.replace('GET','--download'))
