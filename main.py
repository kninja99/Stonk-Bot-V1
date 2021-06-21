import eel
from os import closerange
from bs4 import BeautifulSoup
import requests
import time

# gui start command
eel.init('web')
eel.start('index.html')


# user inputs
ticker_apple = 'aapl'
yahoo_base = "https://finance.yahoo.com/quote/"
# sends tickers to uppers
ticker_apple.upper()

# program will search said website for ticker
#                                 ticker?=ticker.tsrc=fin-srch
# https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch  ---- searched link
# https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch
# https://finance.yahoo.com --- Normal link for yahoo

# TEMP COMMENT
html_text = requests.get(
    "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch").text

# html_text = requests.get(
#    "https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch").text

# send to soup
soup1 = BeautifulSoup(html_text, "lxml")

# grab first three news articles (don't know why it skips the ad and only gets the first 3) buuttttt it works sooooo
# possible infinte scrolling glitch
news_article = soup1.findAll(
    'li', class_='js-stream-content Pos(r)')

# list containing back end of links aka HREFS
yahoo_links = []
# hrefs added to this link to get ful url
yahoo_base_link = "https://finance.yahoo.com"

# for loop that finds the href and builds full links for yahoo
for articles in news_article:
    temp_link = articles.find('a', href=True)
    yahoo_links.append(yahoo_base_link + temp_link['href'])


# for testing
for text in yahoo_links:
    print(text)
    print("\n\n")


# grab links to news areticals next
