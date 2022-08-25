from config_REST_api_connect import session_unauth
from config_execution_api import ticker_1
from config_execution_api import ticker_2

#Get the price values to establish how much precisions there is
def get_price_rounding(ticker):
    API = session_unauth.public_trading_records(
        symbol=ticker,
        limit=100
    )["result"]

    decimal_list = []
    #sift through each price found in past limit of data
    for live_price in API:
        string = str(live_price["price"])
        count = 0
        #look for a . in the string.
        if "." in string:
            #if . found in string, find location of it
            for char in string:
                if char == ".":
                    decimal_list.append(len(string) - count)
                else:
                    count += 1
            decimal_list.sort(reverse=True)

    #if there is a decimal, return the decimal. if not, return 0.
    if decimal_list:
        return (decimal_list[0] - 1)
    else:
        return 0

def get_qty_rounding(ticker):
    API = session_unauth.public_trading_records(
        symbol=ticker,
        limit=100
    )["result"]
    decimal_list = []
    #sift through each price found in past limit of data
    for live_qty in API:
        string = str(live_qty["qty"])
        count = 0
        #look for a . in the string.
        if "." in string:
            #if . found in string, find location of it
            for char in string:
                if char == ".":
                    decimal_list.append(len(string) - count)
                else:
                    count += 1
            decimal_list.sort(reverse=True)

    #if there is a decimal, return the decimal. if not, return 0.
    if decimal_list:
        return (decimal_list[0] - 1)
    else:
        return 0

rounding_ticker_1 = get_price_rounding(ticker_1)
rounding_ticker_2 = get_price_rounding(ticker_2)
quantity_rounding_ticker_1 = get_qty_rounding(ticker_1)
quantity_rounding_ticker_2 = get_qty_rounding(ticker_2)