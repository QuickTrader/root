'''
Created on Feb 29, 2016

@author: pdono_000
'''

from csv_internal.csv_to_array import *
from yahoo.pandas.historical_price_lookup import *

def getDate(timestamp):
    i = 0
    day_str = ""
    month_str = ""
    year_str = ""
    while timestamp[i] != '/':
        day_str += timestamp[i]
        i += 1
    i += 1
    while timestamp[i] != '/':
        month_str += timestamp[i]
        i += 1
    i += 1
    j = 0
    while j < 4:
        year_str += timestamp[i]
        j += 1
        i += 1
    return {
            "day": int(day_str),
            "month": int(month_str),
            "year": int(year_str)
            }
            
        
rumor_classification = csvConvert("rumor-classifier.csv")        #remove first row
rumor_classification.pop(0)
results = 0
for row in rumor_classification:
    date = getDate(row[3])
    if row[6] != 'N/A':     #row 6 is first target
        try:    
            results += get_earnings(row[6], date["year"], date["month"], date["day"])
        except:
            print("WARNING: Pandas cannot find the numbers for this trade.")
    if row[7] != 'N/A':     #row 7 is second target
        try:    
            results += get_earnings(row[7], 2015, 3, 10)
        except:
            print("WARNING: Pandas cannot find the numbers for this trade.")
    print (results)


#test = get_earnings("BE", 2014, 12, 31)        --keep this here so we have the formate

    
