'''
This creates a database with a table for each S&P 500 company containing it's ticker, name, and sector

PREREQUISITES:
create a mysql database through phpmyadmin called "s&p_500"

Created on Aug 21, 2015

@author: pdono_000
'''

from mysql.local.quicktrader import create_historical_rumors_table
from mysql.sp_500 import create
from csv_internal import csv_to_array
from mysql.sp_500 import db_connect

#get 2D array of company information (sybmol, name, ticker)
csv_array = csv_to_array.csvConvert('sp_500_companies.csv')
array_of_companies = csv_array[1:]
    
connection = db_connect.connect_to_sp_500_db()
cursor = connection.cursor()
for company in array_of_companies:
    print(company)
    create.create_table(cursor, company[0], company[1], company[2])
connection.close()

print('SUCCESS: S&P 500 Database creation is complete.')


''' GRAVEYARD'''
'''
for index in range(0,18):
    print (array_of_tickers[index])
    create.create_table(cursor, array_of_tickers[index])
#have to stop at 19 because ticker is named "ALL"
for index in range(20,499):
    print (array_of_tickers[index])
    create.create_table(cursor, array_of_tickers[index])
connection.close()
'''






