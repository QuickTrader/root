'''
Created on Aug 16, 2015

@author: pdono_000
'''

import pymysql

def connect_to_db(db_name, username, password):
    '''
    connects to local database
    '''
    try:
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user=username,
                                     password=password,
                                     db=db_name,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    except:
        print ("Cannot connect to database")
    else:
        print ("Successfully connected to database")
        return connection