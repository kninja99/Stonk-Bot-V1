from os import closerange
import eel
from bs4 import BeautifulSoup
import requests

'''
this will be the class the all the scrapers will inherit
has your base variables  that each scraper should have
and also has getters for all variables
'''

# a new scraper will be created for each ticker symbol


class Scraper:
    stock_ticker = None
    header_arr = []         # headers of arrays
    articles_info = []  # articles infor will be an array of arrays
    link_to_article = []  # this array will contain the links to each article

    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker.upper()
        self.yahooScraper()
        self.marketWatchScraper()
        self.benZingaScraper()

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

    # ---- function getters ----

    def getTicker(self):
        return self.stock_ticker

    def getHeader(self):
        return self.header_arr

    def getArticleInfo(self):
        return self.articles_info

    def getArticleLink(self):
        return self.link_to_article
