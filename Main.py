from hitbtcapi.client import Client
from sortData import *
from calculateOpportunities import *

#hitbtc does not require any private keys for market data API requests
client = Client('public key', 'secret key')

#Pull all market data from hitbtc API
tickers = client.get_tickers()

#takes market data and sorts it into the format needed
sortedData = sortData(tickers)

#takes sorted market data and calculates every possible triangular arbitrage opportunity
opportunities = calculateOpportunities(sortedData)