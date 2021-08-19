from os import closerange
import eel
from bs4 import BeautifulSoup
import requests
from requests.api import request
import scraper
import json
# constent
JSON_FILE = 'web/stocks.json'

# user input que
user_input_que = []

'''
this function is used to send front end button input to the backend
# param input = user input from front end
'''


@eel.expose
def grabInput(input):
    user_input_que.append(input)


'''
writes data to json file
# param data = data you wish to write
# param file_name = json file name
'''


def write_json(data, file_name=JSON_FILE):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)


def search_json(ticker, file_name=JSON_FILE):
    # opens and reads json stock info list
    with open(file_name) as f:
        data = json.load(f)
        stock_information = data['stock_info']
    # searches for the stock ticker that you want to remove
    for stock in stock_information:
        stock_ticker = stock['stock_ticker']
        if(stock_ticker == ticker.upper()):
            return True
    return False


'''
this will seach for a stock ticker to remove from the json
stock info list
'''


@eel.expose
def remove_stock(ticker, file_name=JSON_FILE):
    # opens and reads json stock info list
    with open(file_name) as f:
        data = json.load(f)
        stock_information = data['stock_info']
    # searches for the stock ticker that you want to remove
    for stock in stock_information:
        stock_ticker = stock['stock_ticker']
        if(stock_ticker == ticker):
            # removes the stock from original stock list
            stock_information.remove(stock)
            # process of overwriting old data
            data['stock_info'] = stock_information
            write_json(data)


'''
this function will take in a scraper object of a stock and send th information to the json file to be store
@param stock = scraper object with data scraped stored in it
@param file_name = is where the data from the scraper object will be written
'''


def add_stock(stock, file_name=JSON_FILE):
    with open(file_name) as json_file:
        data = json.load(json_file)
        temp = data['stock_info']
        info = {'stock_ticker': stock.stock_ticker, 'price': stock.current_price, 'percent_change': stock.percent_change,
                'headers': stock.header_arr, 'articles': stock.articles_info, 'links': stock.link_to_article}
        temp.append(info)
        write_json(data)


# points eel to the directors where html file is
eel.init('web')

# starts the eel program
eel.start('index.html', size=(1280, 720), position=(100, 40), block=False)


# application loop
while True:
    if(len(user_input_que) > 0):
        # check to see if data already exist for this stock
        if(search_json(user_input_que.pop(0))):
            eel.duplicateDataError()
        # if data doesn't exist this is where it will be built
    else:
        eel.sleep(1)
