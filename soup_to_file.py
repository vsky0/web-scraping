# tried to save soup object to text file but didn't work..
import requests
from bs4 import BeautifulSoup
import pickle
url = "https://www.google.com/search?q=weather"

response = requests.get(url)

soup = BeautifulSoup(response, 'html.parser')

with open("soup_weather.pickle", 'wb') as file:
    pickle.dump(soup, file)