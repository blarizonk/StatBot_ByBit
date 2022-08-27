from config_execution_api import signal_positive_ticker
from config_execution_api import signal_negative_ticker
from config_REST_api_connect import get_position_data
from config_REST_api_connect import session_auth

#Get position information
def get_position_info(ticker):

    # Declare output variables
    side = 0
    size = ""

    # Extract position info
    position = get_position_data(ticker)
    if "ret_msg" in position.keys():
        if position["ret_msg"] == "OK":
            if len(position["result"]) == 2:
                if position["result"][0]["size"] > 0:
                    size = position["result"][0]["size"]
                    side = "Buy"
                else:
                    size = position["result"][1]["size"]
                    side = "Sell"

    #Return output
    return side, size


#  Place market close order
def place_market_close_order(ticker, side, size):

    #place market close orders              << There might need to be some fail safe or notification that this was successful or not successful.
    session_auth.place_active_order(
        symbol=ticker,
        side=side,
        order_type="Market",
        qty=size,
        time_in_force="GoodTillCancel",
        reduce_only=True,
        close_on_trigger=False
    )

    #Return
    print(f"{ticker}:{size} closing Market-order placed")
    return


#close all positions for both tickers
def close_all_positions(kill_switch):

    print(signal_positive_ticker, signal_negative_ticker)

    #cancel all active orders:
    session_auth.cancel_all_active_orders(symbol=signal_positive_ticker)
    session_auth.cancel_all_active_orders(symbol=signal_negative_ticker)

    #Get position information:
    side_1, size_1 = get_position_info(signal_positive_ticker)
    side_2, size_2 = get_position_info(signal_negative_ticker)

    if size_1 > 0:
        place_market_close_order(signal_positive_ticker,side_2,size_1)

    if size_2 > 0:
        place_market_close_order(signal_negative_ticker, side_1, size_2)

    #output results: once all positions have been closed, killswitch becomes 0 and new trades are looked for.
    kill_switch = 0
    return kill_switch
