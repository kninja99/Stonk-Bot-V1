import eel
import scraper
import JsonManager

# user input que
user_input_que = []


@eel.expose
def grabInput(input):
    '''
this function is used to send front end button input to the backend
:param input: user input from front end
'''
    user_input_que.append(input)


def loadData():
    '''
    this function will load most recent data for the saved stocks
    '''
    old_stock_info = JsonManager.getStocks()
    old_stock_tickers = []
    # saves old stock tickers and then removes old data
    for stock in old_stock_info:
        old_stock_tickers.append(stock['stock_ticker'])
        JsonManager.remove_stock(stock['stock_ticker'])
    # builds up new data
    for ticker in old_stock_tickers:
        # builds the scraper to gather news info
        news_build = scraper.Scraper(ticker)
        # adds the stock to the json file
        JsonManager.add_stock(news_build)


# pre loads data before launch
eel.spawn(loadData())
# points eel to the directors where html file is
eel.init('web')

# starts the eel program
eel.start('index.html', size=(1280, 720), position=(100, 40), block=False)


# application loop
while True:
    if(len(user_input_que) > 0):
        user_input = user_input_que.pop(0)
        # check to see if data already exist for this stock
        if(JsonManager.search_json(user_input)):
            eel.duplicateDataError()
        # checks to see if the stock ticker is searchable
        elif(scraper.searchError(user_input)):
            eel.searchError(user_input.upper())
        else:
            # builds the scraper to gather news info
            news_build = scraper.Scraper(user_input)
            # adds the stock to the json file
            JsonManager.add_stock(news_build)
            # adds the stock to the front end
            eel.add_new_stock()
    else:
        eel.sleep(1)
