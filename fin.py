# Samuel Huang 2016
# finance v0.01

import numpy
import scipy
import matplotlib
import pandas
import urllib2 # https://docs.python.org/2/howto/urllib2.html
import json #https://docs.python.org/2.7/library/json.html

import ans

# http://www.quantshare.com/sa-426-6-ways-to-download-free-intraday-and-tick-data-for-the-us-stock-market

def initialize():
    print "\nfin v0.1"
    ans.pTime()

# fetches info using robinhood api
def stockInfoRobinhood(symbol):
    link = 'https://api.robinhood.com/quotes/' + symbol + '/'
    print "\n...fetching stockInfo:", symbol
    print "\t", link

    u = urllib2.urlopen(link)
    content = u.read()
    decode = json.loads(content)
    fields = []

    fieldCount = 0
    for fieldName in decode:
        fieldValue = decode[fieldName]
        fields.append([fieldName, fieldValue])
        fieldCount += 1
    # print "\tfields:", fieldCount, "\n"
    return fields

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.info = stockInfoRobinhood(symbol)

initialize()
while(1):
    quote = raw_input("\nenter a quote:").upper()
    theQuote = Stock(quote)
    print theQuote.info