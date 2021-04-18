from binance.client import Client
import json

api_key=""
sec_key=""


# list tickers
# note list elements returnned as dictiionary with unicode pairings
#u'symbol' and u'price'

def list_tickers(tickers_list):    
    l = [x for x in tickers_list]
    for e in l:
        print(e[u'symbol'] +"\t"+ e[u'price'])

#
#
#
client = Client(api_key, sec_key)
tickers = client.get_all_tickers()
# print(type(tickers))
#tickers returns dictionary with unicoe pairings

list_tickers(tickers)