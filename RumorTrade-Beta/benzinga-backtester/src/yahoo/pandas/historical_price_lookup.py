'''
Created on Feb 29, 2016

@author: pdono_000
'''
import datetime
import pandas.io.data as pandas

def get_earnings(stock_symbol, year, month, start_day):
    dates = AdjustedDate(stock_symbol, start_day, month, year)      #just call this method several times to check over a number of days. Save the first start day and the last end day
    first_day_close = pandas.DataReader(stock_symbol, 'yahoo', dates.start_date, dates.start_date)["Close"][0] #get numbers for that day, parse data frame to get close price in "Close" column at index=0
    last_day_close = pandas.DataReader(stock_symbol, 'yahoo', dates.end_date, dates.end_date)["Close"][0]
    return (last_day_close - first_day_close)/first_day_close


class AdjustedDate:

    def __init__(self, stock_symbol, start_day, month, year):
        self.stock_symbol = stock_symbol
        self.start_day = start_day
        self.start_month = month
        self.start_year = year
        self.set_start_date()
        self.find_true_start_date()
        self.initialize_end_date()
        self.set_end_date()
        self.find_true_end_date()
        
    def set_start_date(self):
        self.start_date = datetime.datetime(self.start_year, self.start_month, self.start_day)

    def set_end_date(self):
        self.end_date = datetime.datetime(self.end_year, self.end_month, self.end_day)
    
    def find_true_start_date(self):
        try:
            pandas.DataReader(self.stock_symbol, 'yahoo', self.start_date, self.start_date)
        except:
            if self.start_day < 31:    #check to make sure its not the last day of the month
                self.start_day += 1
            elif self.start_month == 12:      #check to make sure its not the last day of the year
                self.start_year += 1
                self.start_month = 1
                self.start_day = 1
            else:
                self.start_month += 1
                self.start_day = 1
            self.set_start_date()       #set new start date
            self.find_true_start_date()

    def initialize_end_date(self):
            if self.start_day < 31:                        #check to make sure its not the last day of the month
                self.end_day = self.start_day + 1          #need to update end day too
                self.end_month = self.start_month
                self.end_year = self.start_year
            elif self.start_month == 12:                         #check to make sure its not the last day of the year
                self.end_day = 1
                self.end_month = 1 
                self.end_year = self.start_year + 1
            else:
                self.end_day = 1    
                self.end_month = self.start_month + 1
                self.end_year = self.start_year
            
    def find_true_end_date(self):
        try:
            pandas.DataReader(self.stock_symbol, 'yahoo', self.end_date, self.end_date)
        except:
            if self.end_day < 31:    #check to make sure its not the last day of the month
                self.end_day += 1         #need to update end day too
            elif self.end_month == 12:      #check to make sure its not the last day of the year
                self.end_day = 1
                self.end_month = 1
                self.end_year += 1
            else:
                self.end_day = 1
                self.end_month += 1
            try:
                self.set_end_date()         #set new end date too
            except:
                print("WARNING: Datetime package error; date may be out of range")
            self.find_true_end_date()
            
