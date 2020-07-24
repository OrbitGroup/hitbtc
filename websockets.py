import time
import queue
import json
import requests
from hitbtc import HitBTC

# testing websocket logic using ETHBTC as an example

# c = HitBTC()
# c.start()
# time.sleep(5)  # Give the socket some time to connect
# c.subscribe_ticker(symbol='ETHBTC') # Subscribe to ticker data for the pair ETHBTC
#
# while True:
#     try:
#         data = c.recv()
#         print(data)
#     except queue.Empty:
#         continue

def websockets(uniqueMarkets):
    c = HitBTC()
    c.start()
    time.sleep(2) # you need to give it 2 seconds to connect before requesting orderbooks
    for markets in uniqueMarkets:
        symbol = str(markets)
        c.subscribe_book(symbol=str(symbol))
    while True:
        try:
            data = c.recv()
        except queue.Empty:
            continue
        print(data)