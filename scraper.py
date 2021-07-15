

'''
this will be the class the all the scrapers will inherit
has your base variables  that each scraper should have
and also has getters for all variables
'''

# a new scraper will be created for each ticker symbol


class Scraper:
    stock_ticker = None
    header = []         # headers of arrays
    articles_info = []  # articles infor will be an array of arrays
    link_to_article = []  # this array will contain the links to each article

    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker

    # ---- Scraper Function Logic ----

    def yahooScraper(self, stock_ticker):
        pass

    def marketWatchScraper(self, stock_ticker):
        pass

    # ---- function getters ----

    def getTicker(self):
        return self.stock_ticker

    def getHeader(self):
        return self.header

    def getArticleInfo(self):
        return self.articles_info

    def getArticleLink(self):
        return self.link_to_article

# inherites the scrapper base class

# maybe we could just have one class.... and then use the class functions to momdify it, so idk about this part


'''class YahooScraper(Scraper):
    # this constructor should build up all the variables... aka should do the scrapping then store in properlocation
    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker '''
