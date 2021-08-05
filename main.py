from os import closerange
import eel
from bs4 import BeautifulSoup
import requests
from requests.api import request
import scraper
import json

# user input que
user_input_que = []

'''
this function is used to send front end button input to the backend
# param input = user input from front end
'''


@eel.expose
def grabInput(input):
    user_input_que.append(input)


def write_json(data, file_name='web/stocks.json'):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)


# points eel to the directors where html file is
eel.init('web')

# testing writing to jason
with open('web/stocks.json') as json_file:
    data = json.load(json_file)
    temp = data['stock_info']
    y = {'stock_ticker': 'poww', 'price': '22.50', 'percent_change': '+22%'}
    temp.append(y)


write_json(data)
# starts the eel program
eel.start('index.html', size=(1280, 720), position=(100, 40), block=False)


# application loop
while True:
    if(len(user_input_que) > 0):
        # Takes in user input and will build the news for it
        print(user_input_que.pop(0))
    else:
        eel.sleep(1)

# grab links to news areticals next
