import requests
from bs4 import BeautifulSoup

city = "hyderabad"
url = "https://www.google.com/search?q=weather"
response = requests.get(url).content
#html_info=print(response)
soup_obj = BeautifulSoup(response, 'html.parser')

# Extract the required weather data
temperature = soup_obj.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
time_and_sky = soup_obj.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
#humidity = soup_obj.find('span', attrs={'id':'wob_km'}).text.strip()
other_data = soup_obj.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})[5].text

data = time_and_sky.split('\n')
time = data[0]
sky = data[1]


print(f"temperature: {temperature}")
print(f"It's {sky}")
# print(f"humidity is {humidity}")
# print(f"more info: {other_data}")