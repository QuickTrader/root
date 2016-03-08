'''
Created on Aug 22, 2015

@author: pdono_000
'''

#create database
def create_database(cursor):
    try:
        cursor.execute('CREATE DATABASE `s&p_500`')
    except:
        print('ERROR: Failed to create database')
        exit(1)
    else:
        print('SUCCESS: Database created')
        
#create table
def create_table(cursor, symbol, name, sector):
    sql_statement= 'CREATE TABLE `'+symbol+'` (Symbol varchar(255), Name varchar(255), Sector varchar(255) )'
    try:
        cursor.execute(sql_statement)
    except:
        print ('ERROR: Cannot create table')
        exit(1)
    else:
        print ('Successfully added table named '+symbol)
        insert_company_info(cursor, symbol, name, sector)
  
#fill first three columns with ticker, full company name, and sector      
def insert_company_info(cursor, symbol, name, sector):
    sql_statement= 'INSERT INTO `'+symbol+'` (Symbol, Name, Sector) VALUES ( "'+symbol+'", "'+name+'", "'+sector+'" )'
    print (sql_statement)
    try:
        cursor.execute(sql_statement)
    except:
        print ("ERROR: Cannot add company information")
        exit(1)
    else:
        print ("Successfully added table named "+symbol)
