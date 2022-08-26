from func_get_roundings import get_price_rounding
from func_get_roundings import get_qty_rounding
from config_REST_api_connect import session_auth
from config_REST_api_connect import session_unauth
from config_execution_api import signal_positive_ticker
from config_execution_api import signal_negative_ticker

# orderbook = session_unauth.orderbook(symbol="ADAUSDT")['result']
# print(orderbook[0]["symbol"])
#
# price_rounding = get_price_rounding(orderbook[0]["symbol"])
# quantity_rounding = get_qty_rounding(orderbook[0]["symbol"])
#
# print(price_rounding)
# print(quantity_rounding)
#
# api = session_unauth.orderbook(
#         symbol="ICPUSDT",
#         limit=100
#     )
# print(api)

session_auth.cancel_all_active_orders(symbol="BTCUSDT")