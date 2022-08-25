#API URL: https://bybit-exchange.github.io/docs/linear/#t-websocketorderbook25
from pybit import usdt_perpetual
from config_execution_api import ticker_1
from config_execution_api import ticker_2

list = [
    ticker_1,
    ticker_2
]

ws_linear = usdt_perpetual.WebSocket(
    test=True,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)
def handle_message(msg):
    print(msg["data"])
# To subscribe to multiple symbols,
# pass a list: ["BTCUSDT", "ETHUSDT"]
all_data = ws_linear.orderbook_25_stream(
    handle_message, list
)


#_______________________________________________________________

# from config_execution_api import ws_public_url
# from config_execution_api import ticker_1
# from config_execution_api import ticker_2
#
# from pybit import WebSocket
#
# # Public ws subscriptions
# subs_public = [
#     f"orderBookL2_25.{ticker_1}",
#     f"orderBookL2_25.{ticker_2}"
# ]
#
# # Public ws connection
# ws_public = WebSocket(
#     ws_public_url,
#     subscriptions=subs_public,
#)


