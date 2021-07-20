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


'''
this function will return the headers of the articles to an array
# param HTMLarr = articles list in html
# return an array of type string, articleHeaderArr
'''


def articlesHeaderToString(HTMLarr):
    articleHeaderArr = []
    for i in HTMLarr:
        header = i.find('h3')
        articleHeaderArr.append(header.get_text())
    return articleHeaderArr


'''
this function will return the preview of the articles to an array
# param HTMLarr = articles list in html
# return articlePreArr = the preview of the article
'''


def articlesPreviewToString(HTMLarr):
    articlePreArr = []
    for i in HTMLarr:
        preview = i.find('p')
        articlePreArr.append(preview.get_text())
    return articlePreArr


'''
this function will build news articles on startup and also used for live updates
# param stockTicker = ticker that you want to scrape info on
'''


def buildNews(stockTicker):
    ticker = stockTicker.upper()
    # builds link based off of the inputed ticker, currently just yahoo
    yahoo_search = "https://finance.yahoo.com/quote/{tick}?p={tick}&.tsrc=fin-srch".format(
        tick=ticker)
    # gets html info and sends to a scraper called soup
    html_info = requests.get(yahoo_search).text
    soup = BeautifulSoup(html_info, "lxml")
    # builds a news articles array
    news_articles = soup.find('li', class_='js-stream-content Pos(r)')
    # checks for a valid stock ticker, if not valid will spit out an error message
    if news_articles == None:
        eel.searchError()
    else:
        # sends info to frontend
        eel.addStock(ticker, articlesHeaderToString(
            news_articles), articlesPreviewToString(news_articles))


# points eel to the directors where html file is
eel.init('web')

# yahoo link info
#                                 ticker?=ticker.tsrc=fin-srch
# https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch  ---- searched link
# https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch
# https://finance.yahoo.com --- Normal link for yahoo


# marketwatch, trying to figure out how to scrap market watch
# https://www.marketwatch.com/investing/stock/aapl?mod=quote_search
# https://www.marketwatch.com/investing/stock/poww?mod=quote_search

# benZinga scraper testing
# base site https://www.benzinga.com/
# aapl https://www.benzinga.com/quote/AAPL
# poww https://www.benzinga.com/quote/POWW
# stock search link https://www.benzinga.com/quote/{ticker}

# benzinga_search = 'https://www.benzinga.com/quote/{tick}'.format(tick='AAPL')
# html_info = requests.get(benzinga_search).text
# soup = BeautifulSoup(html_info, 'lxml')
# news_articles = soup.find('div', class_='py-2')
# # finds the header and sets it to a string
# header = news_articles.get_text()
# # now getting to the article
# article_link = news_articles.find('a', href=True)
# article_link = article_link['href']  # grabs the link to article
# # opens the article
# html_info = requests.get(article_link).text
# soup = BeautifulSoup(html_info, 'lxml')
# article_preview = soup.find('div', class_='article-content')
# # gets the article preview in text
# article_preview = article_preview.find('p').get_text()
# print(header)
# print(article_preview)


news_scraper = scraper.Scraper('dis')
# testing to see if new_scraper built right and is displaying data in order
print('---- Headers ----')
print(news_scraper.header_arr)
print('---- article previews ----')
# probably should look into a way of condensing market watch to only one element, so finding a way to grab the importent preview element of every ticker that is searched
for arr in news_scraper.articles_info:
    print(arr)
print('---- links ----')
print(news_scraper.link_to_article)


# starts the eel program
eel.start('index.html', size=(1280, 720), position=(100, 40), block=False)


# application loop
while True:
    if(len(user_input_que) > 0):
        # Takes in user input and will build the news for it
        buildNews(user_input_que.pop(0))
    else:
        eel.sleep(1)

# grab links to news areticals next
