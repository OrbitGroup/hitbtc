def sortData(tickers):
    sortedData = []
    for markets in tickers:
        # identify and define what the base markets are for each market. All of the base markets have symbols with three letters other than
        # USDT and TUSD
        # this is what the raw data looks like from hitbtc
        #   {
        #     "ask": "0.050043",
        #     "bid": "0.050042",
        #     "last": "0.050042",
        #     "open": "0.047800",
        #     "low": "0.047052",
        #     "high": "0.051679",
        #     "volume": "36456.720",
        #     "volumeQuote": "1782.625000",
        #     "timestamp": "2017-05-12T14:57:19.999Z",
        #     "symbol": "ETHBTC"
        #  }
        #
        if markets['symbol'][-4:] == "USDT" or markets['symbol'][-4:] == "TUSD":
            baseMarket = markets['symbol'][-4:]
            altMarket = markets['symbol'][:len(markets['symbol']) - 4]
        else:
            baseMarket = markets['symbol'][-3:]
            altMarket = markets['symbol'][:len(markets['symbol']) - 3]
        # append each market to the table. This takes only the most basic information, the bid/ask prices, and the market names
        marketLog = {
            "symbol": markets['symbol'],
            "base": baseMarket,
            "alt": altMarket,
            "bid": float(markets['bid']),
            "ask": float(markets['ask'])
        }
        sortedData.append(marketLog)
    return(sortedData)