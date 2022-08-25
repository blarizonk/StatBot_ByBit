from config_execution_api import stop_loss_fail_safe
from func_get_roundings import rounding_ticker_1
from func_get_roundings import rounding_ticker_2
from func_get_roundings import quantity_rounding_ticker_1
from func_get_roundings import quantity_rounding_ticker_2

import math


# Puts all close prices in a list
def extract_close_prices(prices):
    close_prices = []
    for price_values in prices:
        if math.isnan(price_values["close"]):
            return []
        close_prices.append(price_values["close"])
    return close_prices


def get_single_trade_details(orderbook, direction="Long", capital=0):
    # Set calculation and output variables
    price_rounding_1 = 20
    quantity_rounding_1 = 20
    mid_price_1 = 0
    quantity_1 = 0
    stop_loss_1 = 0
    bid_items_list_1 = []
    ask_items_list_1 = []

    # Get prices, stop loss and quantity for ticker_1
    if orderbook:

        # Set price rounding
        price_rounding_1 = rounding_ticker_1
        quantity_rounding_1 = quantity_rounding_ticker_1

        # Organise prices
        for level in orderbook:
            if level["side"] == "Buy":
                bid_items_list_1.append(float(level["price"]))
            else:
                ask_items_list_1.append(float(level["price"]))

            # Calculate price, size, stop loss and average liquidity
            if len(ask_items_list_1) > 0 and len(bid_items_list_1) > 0:

                # Sort lists
                ask_items_list_1.sort()
                bid_items_list_1.sort()
                bid_items_list_1.reverse()

                # Get nearest ask, nearest bid and orderbook spread
                nearest_ask_1 = ask_items_list_1[0]
                nearest_bid_1 = bid_items_list_1[0]

                # Calculate hard stop loss
                if direction == "Long":
                    mid_price_1 = nearest_bid_1  # placing at Bid has high probability of not being cancelled, but may not fill
                    stop_loss_1 = round(mid_price_1 * (1 - stop_loss_fail_safe), price_rounding_1) #<< stop_loss_1 = round(mid_price_1 * (1 - stop_loss_fail_safe), price_rounding_1)
                else:
                    mid_price_1 = nearest_ask_1  # placing at Ask has high probability of not being cancelled, but may not fill
                    stop_loss_1 = round(mid_price_1 * (1 + stop_loss_fail_safe), price_rounding_1)

                # Calculate quantity
                quantity_1 = round(capital / mid_price_1, quantity_rounding_1)

        return mid_price_1, stop_loss_1, quantity_1


#Get trade details and latest prices
# def get_trade_details(orderbook_ticker, direction="Long", capital=0):
#     # Set calculation and output variables
#     price_rounding = 20
#     quantity_rounding = 20
#     mid_price = 0
#     quantity = 0
#     stop_loss = 0
#     bid_items_list = []
#     ask_items_list = []
#
#     # Get prices, stop loss and quantity for ticker_1
#     if orderbook_ticker:
#
#         # Set price rounding
#         price_rounding = rounding_ticker_1
#         quantity_rounding = quantity_rounding_ticker_1
#
#         # Organise prices
#         for level in orderbook_ticker:
#             if level["side"] == "Buy":
#                 bid_items_list.append(float(level["price"]))
#             else:
#                 ask_items_list.append(float(level["price"]))
#
#             # Calculate price, size, stop loss and average liquidity
#             if len(ask_items_list) > 0 and len(bid_items_list) > 0:
#
#                 # Sort lists
#                 ask_items_list.sort()
#                 bid_items_list.sort()
#                 bid_items_list.reverse()
#
#                 # Get nearest ask, nearest bid and orderbook spread
#                 nearest_ask = ask_items_list[0]
#                 nearest_bid = bid_items_list[0]
#
#                 # Calculate hard stop loss
#                 if direction == "Long":
#                     mid_price = nearest_bid # placing at Bid has high probability of not being cancelled, but may not fill
#                     stop_loss = round(mid_price * (1 - stop_loss_fail_safe), price_rounding)
#                 else:
#                     mid_price = nearest_ask  # placing at Ask has high probability of not being cancelled, but may not fill
#                     stop_loss = round(mid_price * (1 + stop_loss_fail_safe), price_rounding)
#
#                 # Calculate quantity
#                 quantity = round(capital / mid_price, quantity_rounding)
#
#         #Output results
#
#     return mid_price, stop_loss, quantity

#____________________________________________________________________________________________________________ TICKER_1 and TICKER_2
#Get trade details and latest prices








def get_trade_details(orderbook_ticker_1, orderbook_ticker_2, direction="Long", capital=0):
    # Set calculation and output variables
    price_rounding_1 = 20
    price_rounding_2 = 20
    quantity_rounding_1 = 20
    quantity_rounding_2 = 20
    mid_price_1 = 0
    mid_price_2 = 0
    quantity_1 = 0
    quantity_2 = 0
    stop_loss_1 = 0
    stop_loss_2 = 0
    bid_items_list_1 = []
    ask_items_list_1 = []
    bid_items_list_2 = []
    ask_items_list_2 = []

    # Get prices, stop loss and quantity for ticker_1
    if orderbook_ticker_1:

        # Set price rounding
        price_rounding_1 = rounding_ticker_1
        quantity_rounding_1 = quantity_rounding_ticker_1

        # Organise prices
        for level in orderbook_ticker_1:
            if level["side"] == "Buy":
                bid_items_list_1.append(float(level["price"]))
            else:
                ask_items_list_1.append(float(level["price"]))

            # Calculate price, size, stop loss and average liquidity
            if len(ask_items_list_1) > 0 and len(bid_items_list_1) > 0:

                # Sort lists
                ask_items_list_1.sort()
                bid_items_list_1.sort()
                bid_items_list_1.reverse()

                # Get nearest ask, nearest bid and orderbook spread
                nearest_ask_1 = ask_items_list_1[0]
                nearest_bid_1 = bid_items_list_1[0]

                # Calculate hard stop loss
                if direction == "Long":
                    mid_price_1 = nearest_bid_1 # placing at Bid has high probability of not being cancelled, but may not fill
                    stop_loss_1 = round(mid_price_1 * (1 - stop_loss_fail_safe), price_rounding_1)
                else:
                    mid_price_1 = nearest_ask_1  # placing at Ask has high probability of not being cancelled, but may not fill
                    stop_loss_1 = round(mid_price_1 * (1 + stop_loss_fail_safe), price_rounding_1)

                # Calculate quantity
                quantity_1 = round(capital / mid_price_1, quantity_rounding_1)

    # Get prices, stop loss and quantity for ticker_1
    elif orderbook_ticker_2:

        # Set price rounding
        price_rounding_2 = rounding_ticker_2
        quantity_rounding_2 = quantity_rounding_ticker_2

        # Organise prices
        for level in orderbook_ticker_2:
            if level["side"] == "Buy":
                bid_items_list_2.append(float(level["price"]))
            else:
                ask_items_list_2.append(float(level["price"]))

            # Calculate price, size, stop loss and average liquidity
            if len(ask_items_list_2) > 0 and len(bid_items_list_2) > 0:

                # Sort list2
                ask_items_list_2.sort()
                bid_items_list_2.sort()
                bid_items_list_2.reverse()

                # Get nearest ask, nearest bid and orderbook spread
                nearest_ask_2 = ask_items_list_2[0]
                nearest_bid_2 = bid_items_list_2[0]

                # Calculate hard stop loss
                if direction == "Long":
                    mid_price_2 = nearest_bid_2  # placing at Bid has high probability of not being cancelled, but may not fill
                    stop_loss_2 = round(mid_price_2 * (1 - stop_loss_fail_safe), price_rounding_2)
                else:
                    mid_price_2 = nearest_ask_2  # placing at Ask has high probability of not being cancelled, but may not fill
                    stop_loss_2 = round(mid_price_2 * (1 + stop_loss_fail_safe), price_rounding_2)

                # Calculate quantity
                quantity_2 = round(capital / mid_price_2, quantity_rounding_2)
        #Output results

        return mid_price_1, stop_loss_1, quantity_1, mid_price_2, stop_loss_2, quantity_2

# from config_REST_api_connect import get_orderbook_api
# from time import sleep
#
# while True:
#     sleep(1)
#     orderbook_ticker_1, orderbook_ticker_2 = get_orderbook_api()
#     mid_price_1, stop_loss_1, quantity_1, mid_price_2, stop_loss_2, quantity_2 = get_trade_details(orderbook_ticker_1,orderbook_ticker_2, direction="Long", capital=10000)
#
#     print("mid_price_1:", mid_price_1)
#     print("stop_loss_1:", stop_loss_1)
#     print("quantity_1:", quantity_1)



