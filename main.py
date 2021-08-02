import requests
from datetime import datetime

USERNAME = "nadun"
TOKEN = "thisisvalidationtoken"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# only uncomment this section if you need to create a new account in pixela
# request = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(request.text)

# create a graph inside pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My Coding Tracker",
    "unit": "hr",
    "type": "int",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# Use this line to create a graph
# request = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(request.text)

# menu
print(
    "Coding Habit Tracker V1\n----------------------------\n* input (1) to Add Today's Hours spent on coding.\n* input (2) to delete recorde.\n* input (3) to update")
menu = int(input("Enter option:- "))
if menu == 1:
    # post value to the graph
    graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

    # input number of hours learned code
    hours = str(input("Enter number of hours spend on coding today: "))

    # today in yyyy-mm-dd format
    today = datetime.now()
    today_formatted = str(datetime.strftime(today, '%Y%m%d'))

    graph_post_params = {
        "date": today_formatted,
        "quantity": hours
    }

    request = requests.post(url=graph_post_endpoint, headers=header, json=graph_post_params)
    print(request.text)
elif menu == 2:
    date = input("Enter date you want to delete data (eg: 20200615): ")
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"
    request = requests.delete(url=delete_pixel_endpoint, headers=header)
    print(request.text)
elif menu == 3:
    date = input("Enter date you want to update data (eg: 20200615): ")
    quantity = input("Enter how many hours need to update (0-9): ")
    update_params = {
        "quantity": quantity
    }
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"
    request = requests.put(url=update_pixel_endpoint, headers=header, json=update_params)
    print(request.text)
else:
    print("Invalid Input")
