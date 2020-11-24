import requests

continent = input("Enter the name of the continent : ")
city = input("Enter the name of the country : ")

response = requests.get(f"http://worldtimeapi.org/api/timezone/{continent}/{city}")

data = response.json();

print(data['datetime'][11:19])
print("DONE!!")
