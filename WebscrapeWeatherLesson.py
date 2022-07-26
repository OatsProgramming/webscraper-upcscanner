import os
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

# Refer to this https://www.youtube.com/watch?v=cta1yCb3vA8
# Fk BeautifulSoup and the other guy

os.system('clear')

location = input("Enter a location: ")

url = f'https://www.google.com/search?q=weather+{location}'

#HTMLSession (This works better)
s = HTMLSession()
r = s.get(url)
temp = (r.html.find('span#wob_tm', first=True).text)
# print(temp)
unit = (r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text)
# print(unit)
condition = (r.html.find('span#wob_dc', first=True).text).lower()
# print(condition)

print(f'It is currently {temp}{unit} in {location}. It is also {condition} right now.')

# Note to SELF: There is a HUGE difference btwn copying an Xpath and a FULL Xpath. Try to copy the xpath first; if not possible then full xpath





#BeautifulSoup
#result = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser")                                For some reason, HTML Session works much better than BeautifulSoup. Whenever I print this, I get None, 
#print(doc.find('span#wob_tm.wob_t q8U8x'))                                     even tho I CLEARLY SEE THAT ITS THERE AND ITS THE EXACT NAME AND EVERYTHING
