'''
Created on Sep 8, 2015

@author: pdono_000
'''

def escape_sql(string):
    escaped_string = ''
    for character in string:
        if character != '\'':   #check for quotation mark
            escaped_string += character
        else:
            escaped_string += '\\\''
    return escaped_string