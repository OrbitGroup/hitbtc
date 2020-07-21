def sortData(tickers):
    sortedData = []
    for markets in tickers:
        # identify and define what the base markets are for each market. All of the base markets have symbols with three letters other than
        # USDT and TUSD
        if markets['symbol'][-4:] == "USDT" or markets['symbol'][-4:] == "TUSD":
            baseMarket = markets['symbol'][-4:]
            altMarket = markets['symbol'][:len(markets['symbol']) - 4]
        else:
            baseMarket = markets['symbol'][-3:]
            altMarket = markets['symbol'][:len(markets['symbol']) - 3]
        # append each market to the table. This takes only the most basic information, the bid/ask prices, and the market names
        marketLog = {
            "base": baseMarket,
            "alt": altMarket,
            "bid": float(markets['bid']),
            "ask": float(markets['ask'])
        }
        sortedData.append(marketLog)
    return(sortedData)