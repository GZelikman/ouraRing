import requests
import matplotlib.pyplot as plt

def get_data(URL):
    Header = {'Authorization': "Bearer " + APIToken}
    r = requests.get(url = URL, headers = Header)
    return r.json()

file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()

# Prints DailyReadiness, Sleep and Activity scores
ReadinessScore = get_data("https://api.ouraring.com/v2/usercollection/daily_readiness")
ActivityScore = get_data("https://api.ouraring.com/v2/usercollection/daily_activity")
SleepScore = get_data("https://api.ouraring.com/v2/usercollection/daily_sleep")
print("Readiness: ", ReadinessScore["data"][0]["score"] , " Sleep: " , SleepScore["data"][0]["score"], " Activity: " , ActivityScore["data"][0]["score"])

# Plots Heart Rate from sleep
Sleep = get_data("https://api.ouraring.com/v2/usercollection/sleep")
heartrate = Sleep["data"][1]["heart_rate"]["items"]
time = []
for i in range(len(heartrate)):
    time.append(i*5)
plt.plot(time, heartrate,  'o:r')
plt.title('Heart Rate while sleeping')
plt.xlabel('Time')
plt.ylabel('Heart Rate')
plt.ylim(min(filter(None, heartrate)) - 10, max(filter(None, heartrate)) + 10)
plt.show()
