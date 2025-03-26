import requests
import matplotlib.pyplot as plt

def get_data(URL):
    Header = {'Authorization': "Bearer " + APIToken}
    r = requests.get(url = URL, headers = Header)
    return r.json()

def get_heart_rate():
    # Plots Heart Rate from sleep
    Sleep = get_data("https://api.ouraring.com/v2/usercollection/sleep")
    heartrate = Sleep["data"][0]["heart_rate"]["items"]
    time = []
    for i in range(len(heartrate)):
        time.append(i*5)
    plt.plot(time, heartrate,  'o:r')
    plt.title('Heart Rate while sleeping')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.ylim(min(filter(None, heartrate)) - 10, max(filter(None, heartrate)) + 10)
    return plt

def get_daily():
    # Prints Daily Readiness, Sleep and Activity scores
    ReadinessScore = get_data("https://api.ouraring.com/v2/usercollection/daily_readiness")
    ActivityScore = get_data("https://api.ouraring.com/v2/usercollection/daily_activity")
    SleepScore = get_data("https://api.ouraring.com/v2/usercollection/daily_sleep")
    return "Readiness: " + str(ReadinessScore["data"][0]["score"]) + " Sleep: " + str(SleepScore["data"][0]["score"]) + " Activity: " + str(ActivityScore["data"][0]["score"])

file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()
con = "y"

while con == "y":
    print("Welcome to Oura Data Analysis")
    print("Choose desired option:")
    print("1. Print Daily Readiness, Sleep and Activity scores")
    option = int(input("2. Plot Heart Rate while sleeping "))

    if option == 1:
        print(get_daily())
    elif option == 2:
        plt = get_heart_rate()
        plt.show()
    else:
        print("Invalid option")
    con = input("continue? [y/n] ")
