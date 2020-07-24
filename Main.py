from hitbtcapi.client import Client
from sortData import *
from calculateOpportunities import *
from websockets import *

# hitbtc does not require any private keys for market data API requests
client = Client('public key', 'secret key')

# Pull all market data from hitbtc API
tickers = client.get_tickers()

# takes market data and sorts it into the format needed
sortedData = sortData(tickers)

# takes sorted market data and calculates every possible triangular arbitrage opportunity
# 'uniqueMarkets' is every unique symbol which is involved with a possible triarb trade
uniqueMarkets, opportunities = calculateOpportunities(sortedData)
#print(len(uniqueMarkets))

# passing one triangular set through the function as a test
#uniqueMarkets = ["EDGBTC", "EDGETH", "ETHBTC"]
# send unique markets to websocket module, to then subscribe to those order books
websockets(uniqueMarkets)
