import requests

def get_data(URL):
    Header = {'Authorization': "Bearer " + APIToken}
    r = requests.get(url = URL, headers = Header)
    return r.json()

file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()

Readiness = get_data("https://api.ouraring.com/v2/usercollection/daily_readiness")
Activity = get_data("https://api.ouraring.com/v2/usercollection/daily_activity")
Sleep = get_data("https://api.ouraring.com/v2/usercollection/daily_sleep")
print("Readiness: ", Readiness["data"][0]["score"] , " Sleep: " , Sleep["data"][0]["score"], " Activity: " , Activity["data"][0]["score"])