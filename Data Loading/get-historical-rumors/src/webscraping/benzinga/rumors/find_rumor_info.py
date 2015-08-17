'''
Created on Aug 16, 2015

@author: pdono_000
'''

from yahoo import yahoo_market_cap



def record_acquirer_and_acquiree(merger, ticker1, ticker2):
    if yahoo_market_cap.get_market_cap(ticker1) > (1.5*yahoo_market_cap.get_market_cap(ticker2)):
        merger.acquirer = ticker1
        merger.acquiree = ticker2
        merger.merger_verified= True
    elif yahoo_market_cap.get_market_cap(ticker2) > (1.5*yahoo_market_cap.get_market_cap(ticker1)):
        merger.acquirer = ticker2
        merger.acquiree = ticker1
        merger.merger_verified = True
    return
    
    

