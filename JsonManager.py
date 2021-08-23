import json
import eel
JSON_FILE = 'web/stocks.json'


def write_json(data, file_name=JSON_FILE):
    '''
writes data to json file
:param data: data you wish to write
:param file_name: json file name
'''
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)


def search_json(ticker, file_name=JSON_FILE):
    '''
    This will seach the json file for the ticker
    :param ticker: is the stock ticker you want to search for in the json file
    '''
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


@eel.expose
def remove_stock(ticker, file_name=JSON_FILE):
    '''
this will seach for a stock ticker to remove from the json
stock info list
'''
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


def add_stock(stock, file_name=JSON_FILE):
    '''
this function will take in a scraper object of a stock and send th information to the json file to be store
:param stock: scraper object with data scraped stored in it
:param file_name: is where the data from the scraper object will be written
'''
    with open(file_name) as json_file:
        data = json.load(json_file)
        temp = data['stock_info']
        info = {'stock_ticker': stock.stock_ticker, 'price': stock.current_price, 'percent_change': stock.percent_change,
                'headers': stock.header_arr, 'articles': stock.articles_info, 'links': stock.link_to_article}
        temp.append(info)
        write_json(data)


def getStocks(file_name=JSON_FILE):
    with open(file_name) as f:
        data = json.load(f)
        stock_information = data['stock_info']
        return stock_information
