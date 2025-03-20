import requests

file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()

URL = "https://api.ouraring.com/v2/usercollection/sleep"
Header = {'Authorization': "Bearer " + APIToken}
r = requests.get(url = URL, headers = Header)
data = r.json()
print(data)