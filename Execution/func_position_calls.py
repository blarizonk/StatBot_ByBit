from config_REST_api_connect import session_auth

#Check for open positions
def open_position_confirmation(ticker):
    try:
        position = session_auth.my_position(symbol=ticker)
        if position["ret_msg"] == "OK":
            for item in position["result"]:
                if item["size"] > 0:
                    return True
    except:
        return True
    return False

#Check for active positions
def active_position_confirmation(ticker):
    try:
        active_order = session_auth.get_active_order(
            symbol=ticker,
            order_status="Created,New,PartiallyFilled,Active",
        )
        if active_order["ret_msg"] == "OK":
            if active_order["result"]["data"] != None:
                return True
    except:
        return True
    return False

#get open position price and quantity
def get_open_positions(ticker, direction="Long"):
    #get position
    position = session_auth.my_position(
        symbol=ticker
    )
    #select index to avoid looping through response:
    index = 0 if direction == "Long" else 1

    #construct a message:
    if "ret_msg" in position.keys():
        if position["ret_msg"] == "OK":
            if "symbol" in position["result"][index].keys():
                order_price = position["result"][index]["entry_price"]
                order_quantity = position["result"][index]["size"]
                return order_price, order_quantity
            return(0,0)
    return(0,0)

#get active position price and quantity
def get_active_positions(ticker):
    #get position
    active_order = session_auth.get_active_order(
        symbol=ticker,
        order_status="Created,New,PartiallyFilled,Active"
    )
    #construct a message:
    if "ret_msg" in active_order.keys():
        if active_order["ret_msg"] == "OK":
            if active_order["result"]["data"] != None:
                order_price = active_order["result"]["data"][0]["price"]
                order_quantity= active_order["result"]["data"][0]["quantity"]
                return order_price, order_quantity
            return(0,0)
    return(0,0)

#Query existsing orders:
def query_existing_order(ticker, order_id, direction):

    #query order
    order = session_auth.query_active_order(
        symbol=ticker,
        order_id=order_id
    )
    #construct a response:
    if "ret_msg" in order.keys():
        if order["ret_msg"] == "OK":
            order_price = order["result"]["price"]
            order_quantity = order["result"]["qty"]
            order_status = order["result"]["order_status"]

            return order_price, order_quantity, order_status
    return (0,0,0)

