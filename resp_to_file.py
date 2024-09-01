import requests

url = "https://www.google.com/search?q=weather"

response = requests.get(url)

with open("weather.txt", 'w') as file:
    file.write(response.text)