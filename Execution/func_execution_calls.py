from config_execution_api import limit_order_basis
from config_REST_api_connect import session_auth, get_single_orderbook, session_unauth
from func_calculations import get_single_trade_details


#Set leverage
def set_leverage(ticker):

    # Setting the leverage
    try:
        leverage_set = session_auth.cross_isolated_margin_switch(
            symbol=ticker,
            is_isolated=True,
            buy_leverage=1,
            sell_leverage=1
        )
    except Exception as e:
        pass
    print(f"\t{ticker} is isolated and set to 1x Leverage.")
    # Return
    return

def place_order(ticker, price, quantity, direction, stop_loss):

    #Set Variables
    if direction == "Long":
        side = "Buy"
    else:
        side = "Sell"

    #Place limit order
    if limit_order_basis:
        order = session_auth.place_active_order(
            symbol=ticker,
            side=side,
            order_type="Limit",
            qty=quantity,
            price=price,
            time_in_force="PostOnly",
            reduce_only=False,
            close_on_trigger=False,
            stop_loss=stop_loss
        )
    else:
        order = session_auth.place_active_order(
            symbol=ticker,
            side=side,
            order_type="Market",
            qty=quantity,
            time_in_force="GoodTillCancel",
            reduce_only=False,
            close_on_trigger=False,
            stop_loss=stop_loss,
        )
    return order

#initialise Order Execution:
def initialise_order_execution(ticker, direction, capital):
    orderbook = session_unauth.orderbook(symbol=ticker)["result"]
    if orderbook:
        mid_price, stop_loss, quantity = get_single_trade_details(orderbook, direction, capital)
        if quantity > 0:
            order = place_order(ticker, mid_price, quantity, direction, stop_loss)
            if "result" in order.keys():
                if "order_id" in order["result"]:
                    return order["result"]["order_id"]
    return 0
