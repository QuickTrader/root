'''
Created on Aug 16, 2015

@author: pdono_000
'''
from mysql.local import db_connect

# connects to quicktrader database
def connect_to_sp_500_db():
    connection = db_connect.connect_to_db('s&p_500', 'root', '')
    return connection
