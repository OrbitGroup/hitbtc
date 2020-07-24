import logging
def calculateOpportunities(sortedData):
    # the trading methodology is to always start and end holding BTC.
    # therefore the first trade is to purchase an altcoin with BTC, then use that altcoin to purchase something else,
    # which is then sold for BTC

    opportunities = []
    uniqueMarkets = []
    for firstPair in sortedData:
        for secondPair in sortedData:
            for thirdPair in sortedData:
                # this 'if' statement matches up the markets to their corresponding possible markets to form a chain of three compatible markets (a 'triangle')
                # the first market must have a base currency of BTC, the second market must have the same altcoin but a different base than BTC, and the third market should
                # have a base of BTC but an 'alt' equal to the base of the second market.
                if firstPair['base'] == 'BTC' \
                        and secondPair['alt'] == firstPair['alt'] \
                        and secondPair['base'] != 'BTC' \
                        and thirdPair['base'] == 'BTC' \
                        and thirdPair['alt'] == secondPair['base']:

                    uniqueMarkets.append(firstPair['symbol'])
                    uniqueMarkets.append(secondPair['symbol'])
                    uniqueMarkets.append(thirdPair['symbol'])
                    # on the first trade you are buying an altcoin using BTC, so you use the ask price
                    firstTrade = 1 / firstPair['ask']
                    # on the second trade you are selling the altcoin for a base coin other than BTC, so you use the bid price
                    secondTrade = firstTrade * secondPair['bid']
                    # on the third trade you are selling whatever is held for BTC, using the bid price again
                    thirdTrade = secondTrade * thirdPair['bid']
                    tradingFlow = str("BTC -> " + firstPair['alt']+" -> "+secondPair['base']+" -> BTC")
                    entry = {
                        "tradingFlow": tradingFlow,
                        "ending balance": thirdTrade
                    }

                    #some basic logging: writes all calculated opportunities to a log file
                    # logging.basicConfig(filename="hitbtc opportunities",
                    #                     format="%(message)s",
                    #                     filemode='w')
                    # loggerArb = logging.getLogger("hitbtc opportunities")
                    # loggerArb.setLevel(logging.INFO)
                    # loggerArb.info(entry)
                    opportunities.append(entry)

    uniqueMarkets = list(dict.fromkeys(uniqueMarkets))
    return(uniqueMarkets, opportunities)