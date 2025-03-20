import requests

file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()

URLread = "https://api.ouraring.com/v2/usercollection/daily_readiness"
URLsleep = "https://api.ouraring.com/v2/usercollection/daily_sleep"
URLactivity = "https://api.ouraring.com/v2/usercollection/daily_activity"
Header = {'Authorization': "Bearer " + APIToken}

r_read = requests.get(url = URLread, headers = Header)
r_activity = requests.get(url = URLactivity, headers = Header)
r_sleep = requests.get(url = URLsleep, headers = Header)

Readiness = r_read.json()
Activity = r_activity.json()
Sleep = r_sleep.json()

print("Readiness: ", Readiness["data"][0]["score"] , " Sleep: " , Sleep["data"][0]["score"], " Activity: " , Activity["data"][0]["score"])