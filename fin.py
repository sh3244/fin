# Samuel Huang 2016
# finance v0.01

import numpy
import scipy
import matplotlib
import pandas
import urllib2 # https://docs.python.org/2/howto/urllib2.html
import json #https://docs.python.org/2.7/library/json.html

from twilio.rest import TwilioRestClient
ACCOUNT_SID = "AC2735c2d441c154487ab9b7be094b099a"
AUTH_TOKEN = "c2cbe614f5cc3189546294cdbdd84311"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

import ans

# http://www.quantshare.com/sa-426-6-ways-to-download-free-intraday-and-tick-data-for-the-us-stock-market

def stockInfoRobinhood(symbol):
    # https: // api.robinhood.com / quotes / MSFT /
    link = "https://api.robinhood.com/quotes/" + symbol + "/"
    stockInfo(symbol, link)
def initialize():
    print "\nfinance v0.01"
    ans.pTime()

def stockInfo(symbol, link):
    # link = "http://finance.google.com/finance/info?&q="
    # url = link + "%s" % (symbol)
    # url = "https://www.google.com/finance?q=aapl"
    print symbol
    # print "\tURL:", url
    print link

    u = urllib2.urlopen(link)
    # print u
    content = u.read()
    decode = []

    # print content
    decode = json.loads(content)
    # print decode

    full = []

    count = 0
    for d in decode:
        temp = decode[d]
        full.append([d, temp])
        print full[len(full)-1]
        count += 1
    print count
    # loaded = False
    # index = 0
    # while loaded == False:
    #     try:
    #         decode = json.loads(content[index:])[0]
    #         loaded = True
    #         # print "decoded json from index:", index
    #     except:
    #         index += 1
    #         if index > 99:
    #             break
    # print decode

    # aPrice = float(decode["el"])
    # aChange = float(decode["ec"])
    # aTime = decode["elt"]
    # change = float(decode["c"])
    # price = float(decode["l"])
    # time = decode["lt"]
    #
    # print "\tPrice:", price
    # print "\t\t", change
    # print "\t", time
    # print ""
    # print "\tAfter Hours:", aPrice
    # print "\t\t", aChange
    # print "\t", aTime
    # print "\n"



class RobinhoodStock:
    def __init__(self):
        initialize()




stocks = ["AAPL", "GOOG", "AMZN"]
for stock in stocks:
    stockInfoRobinhood(stock)
# client.messages.create(
#     to='6098488487',
#     from_='6098425050',
#     body='why',
# )