from bs4 import BeautifulSoup
import requests


def searchError(ticker):
    '''
    this function will determine if you can search for an entered ticker
    :param ticker: this is the ticker that it will search for
    :return: Will return True if it can't find the stock and false if it can
    '''
    # creates the link to yahoo
    yahoo_search = "https://finance.yahoo.com/quote/{tick}?p={tick}&.tsrc=fin-srch".format( tick=ticker.upper())
    html_info = requests.get(yahoo_search).text
    soup = BeautifulSoup(html_info, 'lxml')
    news_articles = soup.find('li', class_='js-stream-content Pos(r)')
    if(news_articles == None):
        return True
    return False

# a new scraper will be created for each ticker symbol


class Scraper:
    stock_ticker = None
    # variables that keep track of stock prices and change
    current_price = None
    percent_change = None

    def __init__(self, stock_ticker):
        self.header_arr = []
        self.articles_info = []
        self.link_to_article = []
        self.stock_ticker = stock_ticker.upper()
        self.yahooScraper()
        self.marketWatchScraper()
        self.benZingaScraper()
        self.fetchPriceInfo()

    # ---- Scraper Function Logic ----

    def yahooScraper(self):
        # creates the link to yahoo
        yahoo_search = "https://finance.yahoo.com/quote/{tick}?p={tick}&.tsrc=fin-srch".format(
            tick=self.stock_ticker)
        html_info = requests.get(yahoo_search).text
        soup = BeautifulSoup(html_info, 'lxml')
        # builds a news articles array
        news_articles = soup.find('li', class_='js-stream-content Pos(r)')
        # now that we have all the news articles we must build the header
        head = news_articles.find('a', href=True)
        self.header_arr.append(head.get_text())
        # this first steps sets article preview to an array that contains the articles preview info
        article_preview = news_articles.find('p').get_text()
        self.articles_info.append(article_preview)
        # grabs article link and appends in proper index
        article_link = 'https://finance.yahoo.com' + head['href']
        self.link_to_article.append(article_link)

    def marketWatchScraper(self):
        # market watch search link
        market_search = "https://www.marketwatch.com/investing/stock/{tick}?mod=quote_search".format(
            tick=self.stock_ticker)
        html_info = requests.get(market_search).text
        soup = BeautifulSoup(html_info, 'lxml')
        # looks for html info to get header
        news_articles = soup.find('div', class_='article__content')
        # gets the header string
        header = news_articles.find('h3').get_text().strip()
        # append to header_arr
        self.header_arr.append(header)
        # article preview
        article_link = news_articles.find('a', href=True)
        # if there is no valid link to article
        if(article_link == None):
            # appends an empty list so index count doesnt get mixed up
            self.articles_info.append('')
            # appends a Null pointer in article links
            self.link_to_article.append(article_link)
        # this gets executed if there is a valid link to the article
        else:
            # opens the article link
            html_info = requests.get(article_link['href']).text
            soup = BeautifulSoup(html_info, 'lxml')
            news_summary = soup.find('div', {'id': 'js-article__body'})
            # pretty much grabs the whole news article in html
            news_summary = news_summary.findAll('p')
            # sets first p tag to the article preview
            article_preview = news_summary[0].get_text()
            # checks word count to see if there is an author set as a p tag, if there is it will grab the next p tag
            if(article_preview.count(' ') <= 3):
                article_preview = news_summary[1].get_text()
            # appends to article
            self.articles_info.append(article_preview)
            # appends article link
            self.link_to_article.append(article_link['href'])

    def benZingaScraper(self):
        benzinga_search = 'https://www.benzinga.com/quote/{tick}'.format(
            tick=self.stock_ticker)
        html_info = requests.get(benzinga_search).text
        soup = BeautifulSoup(html_info, 'lxml')
        news_articles = soup.find('div', class_='py-2')
        # finds the header and sets it to a string
        header = news_articles.get_text()
        # adds header to header arr
        self.header_arr.append(header)
        # now getting to the article
        article_link = news_articles.find('a', href=True)
        article_link = article_link['href']  # grabs the link to article
        self.link_to_article.append(article_link)
        # opens the article
        html_info = requests.get(article_link).text
        soup = BeautifulSoup(html_info, 'lxml')
        article_preview = soup.find('div', class_='article-content')
        # gets the article preview in text
        article_preview = article_preview.find('p').get_text()
        article_arr = article_preview
        self.articles_info.append(article_arr)

    '''
    this will fetch all the price info that is needed
    such as the current price, and the price change in the day
    '''

    def fetchPriceInfo(self):
        # creates the link to yahoo
        yahoo_search = "https://finance.yahoo.com/quote/{tick}?p={tick}&.tsrc=fin-srch".format(
            tick=self.stock_ticker)
        html_info = requests.get(yahoo_search).text
        soup = BeautifulSoup(html_info, 'lxml')
        # builds a price info arr
        price_info_arr = soup.find('div', class_='D(ib) Mend(20px)')
        price_info_arr = price_info_arr.find_all('span')
        # sends the price info and percent change to the object data
        self.current_price = price_info_arr[0].get_text()
        self.percent_change = price_info_arr[1].get_text()

    # ---- function getters ----

    def getTicker(self):
        return self.stock_ticker

    def getHeader(self):
        return self.header_arr

    def getArticleInfo(self):
        return self.articles_info

    def getArticleLink(self):
        return self.link_to_article
