from config_strategy_api import session_unauth

#function to get tradeable symbols

"""THIS STAGE HAS EXCHANGE DEPENDENT NUANCES:
This part of the script is using the API documentation to effectivly deliver a list of every coin that is available on the exchange, that is tradable against "USDT". If we want to spread this across other exchanges, we need to carefully evaluate how to collect all the coin data from each other excahnge. Binance might be a good option here."""

def get_tradeable_symbols():

    #Get available symbols on the exchange. Using the API, run a query for all symbols. This returns a dict, which you can use the key "name" to pull out all the symbols.
    sym_list = []
    symbols = session_unauth.query_symbol()# << this is different to the tutorial because Blair used Rest API instead of Websocket as websocket was upgraded after tutorial was posted. tutorial was out of date and thsi was apparently a suitable workaround.
    if "ret_msg" in symbols.keys():
        if symbols["ret_msg"] == "OK":
            symbols = symbols["result"]
            for symbol in symbols:
                if symbol["quote_currency"] == "USDT" and symbol["status"] == "Trading":
                    sym_list.append(symbol)

    # Return output
    return sym_list