import time
import queue
from hitbtc import HitBTC

c = HitBTC()
c.start()
time.sleep(30)  # Give the socket some time to connect
c.subscribe_ticker(symbol='ETHBTC') # Subscribe to ticker data for the pair ETHBTC

while True:
    try:
        data = c.recv()
        print(data)
    except queue.Empty:
        continue

def websockets(uniqueMarkets):
    c = HitBTC()
    c.start()
    for markets in uniqueMarkets:
        symbol = markets
        c.subscribe_book(symbol)
    while True:
        try:
            data = c.recv()
        except queue.Empty:
            continue
        print(data)