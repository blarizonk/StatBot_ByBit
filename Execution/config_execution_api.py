
#API link
#https://bybit-exchange.github.io/docs/linear/#t-introduction

#API imports


# Config Variables:

mode = "test"
ticker_1 = "BNBUSDT"
ticker_2 = "APEUSDT"
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

tradeable_capital_USDT = 100 #this is $1000 for each pair (long and short)
stop_loss_fail_safe = 0.20 #(this will be 20%)
signal_trigger_threshold = 2.5 # Current signal is ZSCORE
sell_zscore = 0

timeframe = 60 # this is hourly, can also be used in other. make sure this matches strategy
kline_limit = 200
z_score_window = 21 #this must match stragety

#LIVE API DATA
api_key_mainnet = ""
api_secret_mainnet = ""

#TEST API DATA
api_key_testnet = "sFYkYknOnG2LPG5gnM"
api_secret_testnet = "UikDR9sUvvmEovKE9aOf1caeXs7wNrTEuafP"

#selected API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

#selected URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"
ws_public_url = "wss://stream-testnet.bybit.com/realtime_public" if mode == "test" else "wss://stream.bybit.com/realtime_public"
