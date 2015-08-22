'''
Created on Aug 16, 2015

@author: pdono_000
'''
from mysql.local import db_connect

# connects to quicktrader database
def connect_to_quicktrader_db():
    connection = db_connect.connect_to_db('quicktrader_historical_rumors', 'root', '')
    return connection
