__author__ = 'Vinay Sridharan'
# #Imports/Global variable definitions
import pandas as pd
import requests as req
import bs4 as bs
import string
import pdb
from mysql.local.quicktrader import create_historical_rumors_table
from yahoo import yahoo_market_cap
from mergers import merger_info
from webscraping.benzinga.rumors import find_rumor_info
from mysql.local import *

'''
merger_article = merger_info.MergerArticleInfo()
find_rumor_info.record_acquirer_and_acquiree(merger_article, 'GOOG', 'AAPL')
print (merger.acquirer, merger.acquiree, merger.merger_verified)
'''

max_pages = 72  # est. via manual checking on website

def pageRumorData(soup):
    assert type(soup) == bs.BeautifulSoup, 'Type Error: Use BeautifulSoup object as input'
    rumorHeaders = _rumorScraper(soup)
    #print('N rumors per page:', len(rumorHeaders[1]))
    df_dict = {'title': [], 'date': [], 'tickers': [], 'text': []}
    for i, url in enumerate(rumorHeaders[1]):
        url_soup = bs.BeautifulSoup(req.get(url).text)
        tickers = tuple(_tickerExtractor(url_soup))
        publish_date = url_soup.find('span', {'date'}).getText().strip()
        publish_date = pd.datetools.to_datetime(publish_date)
        article_text = url_soup.find('div', {'article-content-body'}).getText()
        article_header = rumorHeaders[0][i]
        df_dict['title'].append(article_header)
        df_dict['date'].append(publish_date)
        df_dict['tickers'].append(tickers)
        df_dict['text'].append(article_text)
        merger_article = merger_info.MergerArticleInfo(publish_date,article_header,article_text,tickers)
        merger_article.print_merger_info()
        
        connection = db_connect.connect_to_db('quicktrader_historical_rumors', 'root', '')
        cursor = connection.cursor()
        merger_article.add_to_database(cursor)
        
        connection.commit()
        connection.close()
        
        '''
        find_rumor_info.record_acquirer_and_acquiree(merger_article, 'GOOG', 'AAPL')
        print (merger.acquirer, merger.acquiree, merger.merger_verified)        
        '''
    return df_dict
#Write this as a list of dictionaries - then you can use csvrwiter to output as csv

def _rumorScraper(soup):
    #Operates on pages with multiple rumors
    assert type(soup) == bs.BeautifulSoup, 'Type Error: Use BeautifulSoup object as input'
    headers = soup.find_all('h3')
    if headers[0].getText() == 'What are you waiting for? Sign up now!':  # Remove irrelevant tag
        headers.pop(0)
    headers_text = [head.getText() for head in headers]
    headers_urls = []
    for head in headers:
        headerurl = head.findAll('a', href=True)
        if len(headerurl) == 1:
            headers_urls.append('http://www.benzinga.com' + headerurl[0]['href'])
        elif len(headerurl) ==2:
            assert headerurl[0]['href'] == '/best-of-benzinga', 'One rumor title returning 2 urls'
            headers_urls.append('http://www.benzinga.com' + headerurl[1]['href'])
        else:
            print('One rumor title returning multiple urls')
            pdb.set_trace()
    return (headers_text, headers_urls)

def _tickerExtractor(soup):
    #Operates on single rumor description
    assert type(soup) == bs.BeautifulSoup, 'Type Error: Use BeautifulSoup object as input'
    article = soup.find('div', {'article-content-body'}).getText().split()
    exchanges = ['NYSE:', 'NASDAQ:', 'LSE:']
    exch_dict = {}
    tickers = []
    for exch in exchanges:
        tickers_id= pd.Series([exch in word for word in article])
        tickers_index = list(tickers_id[tickers_id == True].index)
        tickers.extend(article[i+1].strip().strip(string.punctuation) for i in tickers_index)
    return tickers


# #Start checking pages
rumor_dict = {}

for page_number in range(max_pages + 1):
    if page_number == 0:
        url0 = 'http://www.benzinga.com/news/rumors'
        soup0 = bs.BeautifulSoup(req.get(url0).text)
        rumor0 = pageRumorData(soup0)
        rumor_dict[0] = rumor0
    else:
        url = 'http://www.benzinga.com/news/rumors?page=' + str(page_number)
        rumor = pageRumorData(bs.BeautifulSoup(req.get(url).text))
        if page_number != max_pages:
            assert len(rumor['title']) == 15, 'Number of rumor articles seems off; should be 15 per page'
        rumor_dict[page_number] = rumor
# #This has all the data we need to analyze what's going on (i.e. date, title, text, and tickers listed.)

#   #Builds a DataFrame
df = pd.DataFrame(rumor_dict[0])
for i in range(1, len(list(rumor_dict.keys()))):
    df = df.append(pd.DataFrame(rumor_dict[i]))
df.index = pd.DatetimeIndex(df['date'])
df['text'] = [x.encode('utf-8') for x in df['text']]
df['title'] = [x.encode('utf-8') for x in df['title']]
#Can now export to csv (df.to_csv)
#Will now need a seperate categorizer

