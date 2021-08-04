from os import closerange
import eel
from bs4 import BeautifulSoup
import requests
from requests.api import request
import scraper

# user input que
user_input_que = []

'''
this function is used to send front end button input to the backend
# param input = user input from front end
'''


@eel.expose
def grabInput(input):
    user_input_que.append(input)


# points eel to the directors where html file is
eel.init('web')

# this is for testing
#news_scraper = scraper.Scraper('dis')
# testing to see if new_scraper built right and is displaying data in order
# print('---- Headers ----')
# print(news_scraper.header_arr)d
# print('---- article previews ----')
# # probably should look into a way of condensing market watch to only one element, so finding a way to grab the importent preview element of every ticker that is searched
# for arr in news_scraper.articles_info:
#     print('--news article--')
#     print(arr)
# print('---- links ----')
# print(news_scraper.link_to_article)


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
