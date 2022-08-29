# from func_get_roundings import get_price_rounding
# from func_get_roundings import get_qty_rounding
# from config_REST_api_connect import session_auth
# from config_REST_api_connect import session_unauth
# from config_execution_api import signal_positive_ticker
# from config_execution_api import signal_negative_ticker
# import json
# from func_cointegration import extract_close_prices
#
# with open("1_price_list.json") as json_file:
#     price_data = json.load(json_file)
#
# prices_1 = extract_close_prices(price_data[sym_1])
# prices_2 = extract_close_prices(price_data[sym_2])
#
# def hedge_ratio(series_1, series_2):
#     print(series_1)
#     print(series_2)
#
# hedge_ratio(prices_1, prices_2)

start = -3
current = -1

if current > start:
    print(True)
else:
    print(False)