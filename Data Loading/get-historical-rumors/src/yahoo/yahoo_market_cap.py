'''
Created on Aug 16, 2015

@author: pdono_000
'''

import json
import urllib

def get_market_cap(ticker):
    base_url = 'https://query.yahooapis.com/v1/public/yql?'
    query = {
        'q': 'select MarketCapitalization from yahoo.finance.quote where symbol in ("YHOO","'+ticker+'")',
        'format': 'json',
        'env': 'store://datatables.org/alltableswithkeys'
    }
    
    url = base_url + urllib.parse.urlencode(query)
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    json_dict = json.loads(data)
    market_cap = json_dict['query']['results']['quote'][1]['MarketCapitalization'] #get final value -- the object from yahoo finance is complex
    return mkt_cap_str_to_float(market_cap)

def mkt_cap_str_to_float (mkt_cap_str):
    if mkt_cap_str[len(mkt_cap_str)-1] == 'T':
        return (float(mkt_cap_str[:len(mkt_cap_str)-2]))*(10**12)
    elif mkt_cap_str[len(mkt_cap_str)-1] == 'B':
        return (float(mkt_cap_str[:len(mkt_cap_str)-2]))*(10**9)
    elif mkt_cap_str[len(mkt_cap_str)-1] == 'M':
        return (float(mkt_cap_str[:len(mkt_cap_str)-2]))*(10**6)
    elif mkt_cap_str[len(mkt_cap_str)-1] == 'K':
        return (float(mkt_cap_str[:len(mkt_cap_str)-2]))*(10**3)
    else:
        print('WARNING: Market capitalization may be too small for program to read')
        return mkt_cap_str
