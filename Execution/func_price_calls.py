from config_execution_api import ticker_1
from config_execution_api import ticker_2
from config_execution_api import timeframe
from config_execution_api import kline_limit
from func_calculations import extract_close_prices
from config_REST_api_connect import session_unauth
import datetime
import time
from time import sleep

#Get Trade Liquidity to save placing huge limit orders on the orderbooks that can be seen and perhaps used to work against you.
def get_trade_liquidity(ticker):
    sleep(0.5)
    trades = session_unauth.public_trading_records(
        symbol=ticker,
        limit=50
    )

    #get the list for calculating the average liquidity
    quantity_list = []
    if "result" in trades.keys():
        for trade in trades["result"]:
            quantity_list.append(trade["qty"])

    #return average liquidity
    if len(quantity_list) > 0:
        average_liquidity = (sum(quantity_list) / len(quantity_list))
        res_trades_price = float(trades["result"][0]["price"])
        return average_liquidity, res_trades_price
    return (0, 0)


def get_timestamps():
    time_start_date = 0
    time_next_date = 0
    now = datetime.datetime.now()
    if timeframe == 60:
        time_start_date = now - datetime.timedelta(hours=kline_limit)
        time_next_date = now + datetime.timedelta(seconds=30)
    if timeframe == "D":
        time_start_date = now - datetime.timedelta(days=kline_limit)
        time_next_date = now + datetime.timedelta(minutes=1)
    time_start_seconds = int(time_start_date.timestamp())
    time_now_seconds = int(now.timestamp())
    time_next_seconds = int(time_next_date.timestamp())
    return (time_start_seconds, time_now_seconds, time_next_seconds)

#Get historical prices
def get_price_klines(ticker):


    time_start_seconds, _, _ = get_timestamps()
    prices = session_unauth.query_kline(
        symbol=ticker,
        interval=timeframe,
        limit=kline_limit,
        from_time=time_start_seconds
    )
    #manage API calls
    time.sleep(0.25)

    #return prices output
    if len(prices["result"]) != kline_limit:
        return []
    else:
        return prices["result"]

#get latest klines
def get_latest_klines():
    series_1 = []
    series_2 = []
    prices_1 = get_price_klines(ticker_1)
    prices_2 = get_price_klines(ticker_2)
    if len(prices_1) > 0:
        series_1 = extract_close_prices(prices_1)
    if len(prices_2) > 0:
        series_2 = extract_close_prices(prices_2)

    return (series_1, series_2)






