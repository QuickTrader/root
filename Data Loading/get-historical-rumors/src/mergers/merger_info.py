'''
Created on Aug 16, 2015

@author: pdono_000
'''

class MergerArticleInfo(object):
    '''
    classdocs
    '''

    acquirer = ''
    acquiree = ''
    merger_verified = False     #set to true if one company's market cap is more than 150% of the other's

    def __init__(self,timestamp,header,text,tickers):
        '''
        Constructor
        '''
        self.article_timestamp = timestamp
        self.article_header = header
        self.article_text = text
        self.article_tickers = tickers
        if self.article_header.find('M&A Chatter') == -1:
            self.m_and_a_chatter = False
        else:
            self.m_and_a_chatter = True
    def add_to_db(self):
        return

    def print_merger_info(self):
        print ('Timestamp: '+str(self.article_timestamp))
        print ('Tickers: '+str(self.article_tickers))
        print ('Header: '+self.article_header)
        print ('Text: '+self.article_text)
        print ('Merger spec\'s: '+str(self.merger_verified)+'    '+self.acquirer+' acquires '+self.acquiree)
        print ('M&A Chatter: '+str(self.m_and_a_chatter))
        print ('')
        
