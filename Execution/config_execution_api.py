
#API link
#https://bybit-exchange.github.io/docs/linear/#t-introduction

#API imports


# Config Variables:

mode = "test"
ticker_1 = "SUSHIUSDT"
ticker_2 = "WAVESUSDT"
signal_positive_ticker = ticker_2
signal_negative_ticker = ticker_1
"""
------This is now found on func_get_roundings-----
#********************************
#rounding_ticker_1 = get_price_rounding(ticker_1)   
#rounding_ticker_2 = get_price_rounding(ticker_2)
quantity_rounding_ticker_1 = get_qty_rounding(ticker_1) 
quantity_rounding_ticker_2 = get_qty_rounding(ticker_2) 
#********************************
"""

limit_order_basis = True # Will ensure positions except for close) will be placed on limit basis

tradeable_capital_USDT = 400 #this is $1000 for each pair (long and short)
stop_loss_fail_safe = 0.15 #(this will be 20%)
signal_trigger_threshold = 1.1 # Current signal is ZSCORE

timeframe = 60 # thisis hourly, can also be used in other. make sure this matches strategy
kline_limit = 200
z_score_window = 21 #this must match stragety

#LIVE API DATA
api_key_mainnet = ""
api_secret_mainnet = ""

#TEST API DATA
api_key_testnet = "tSlxIPDxxvzSyi0n3O"
api_secret_testnet = "JHRrUCdt1fdBIAm3IUFuqerJIwRzr3B7HFRe"

#selected API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

#selected URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"
ws_public_url = "wss://stream-testnet.bybit.com/realtime_public" if mode == "test" else "wss://stream.bybit.com/realtime_public"



#********************

"""This area needs to be updated"""
#
# ************************8
# SESSION Activation OLD
# session_public = HTTP(api_url)
# session_private = HTTP(api_url, api_key=api_key, api_secret=api_secret)
# #Session Activation NEW
# session_public = usdt_perpetual.HTTP(
#     endpoint=api_url
# )
# session_private = usdt_perpetual.HTTP(
#     endpoint="api_url",
#     api_key=api_key_testnet,
#     api_secret=api_secret_testnet
# )