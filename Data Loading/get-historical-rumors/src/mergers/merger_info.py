'''
Created on Aug 16, 2015

@author: pdono_000
'''

from mysql import formatting

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
        self.article_header = formatting.escape_sql(str(header))
        self.article_text =  formatting.escape_sql(str(text))
        self.article_tickers = tickers
        if self.article_header.find('M&A Chatter') == -1:
            self.m_and_a_chatter = False
        else:
            self.m_and_a_chatter = True
    def add_to_db(self):
        return
    
    def print_article_text(self):
        try:
            print ('Text: '+self.article_text)
        except:
            print ('ERROR: could not print article text ')
            
    def add_to_database(self, cursor):
        #add_item = ("INSERT INTO "+table+" (Ticker,NetIncome) VALUES (%(Ticker)s, %(NetIncome)s)")
        #item_data = {'Ticker': tick, 'NetIncome': netInc}
        if self.m_and_a_chatter == True:
            add_item = "INSERT INTO `m&a_rumors` (article_timestamp, article_header, article_text) VALUES ('"+str(self.article_timestamp)+"','"+str(self.article_header)+"','"+str(self.article_text)+"')"
            try:
                cursor.execute(add_item)  
            except:
                print ("Error--cannot add item")
                exit(1)
            else:
                print ("Successfully added item")
        else:
            add_item = "INSERT INTO `non_m&a_rumors` (article_timestamp, article_header, article_text) VALUES ('"+str(self.article_timestamp)+"','"+str(self.article_header)+"','"+str(self.article_text)+"')"              
            try:
                cursor.execute(add_item)  
            except:
                print ("Error--cannot add item")
                exit(1)
            else:
                print ("Successfully added item")

    def print_merger_info(self):
        print ('Timestamp: '+str(self.article_timestamp))
        print ('Tickers: '+str(self.article_tickers))
        print ('Header: '+self.article_header)
        self.print_article_text()
        print ('Merger spec\'s: '+str(self.merger_verified)+'    '+self.acquirer+' acquires '+self.acquiree)
        print ('M&A Chatter: '+str(self.m_and_a_chatter))
        print ('')
        
        
