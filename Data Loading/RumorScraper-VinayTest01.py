__author__ = 'Vinay Sridharan'
# #Imports/Global variable definitions
import pandas as pd
import requests as req
import bs4 as bs

max_pages = 72  # est. via manual checking on website

# #Define Scraper function
def rumorScraper(soup):
    assert type(soup) == bs.BeautifulSoup, 'Type Error: Use BeautifulSoup object as input'
    headers = soup.find_all('h3')
    if headers[0].getText() == 'What are you waiting for? Sign up now!':  # Remove irrelevant tag
        headers.pop(0)
    headers_text = [head.getText() for head in headers]
    headers_urls = ['http://www.benzinga.com' + head.findAll('a', href=True)[0]['href'] for head in headers]
    return (headers_text, headers_urls)

# #Start checking pages

url0 = 'http://www.benzinga.com/news/rumors'
soup0 = bs.BeautifulSoup(req.get(url0).text)
rumor0 = rumorScraper(soup0)
assert len(rumor0[0]) == 15, 'Rumor length seems off; should be 15 per page'
rumor_dict = {}
rumor_dict[0] = rumor0
for page_number in range(1, max_pages + 1):
    url = 'http://www.benzinga.com/news/rumors?page=' + str(page_number)
    rumor = rumorScraper(bs.BeautifulSoup(req.get(url).text))
    if page_number != max_pages:
        assert len(rumor[0]) == 15, 'Rumor length seems off; should be 15 per page'
    rumor_dict[page_number] = rumor

###Now we work with rumor dict which has all our rumors headings and urls for further investigation.
##I think the headings will be a sql column.
