
from pybit import usdt_perpetual
from config_execution_api import api_key
from config_execution_api import api_secret

url = 'https://api-testnet.bybit.com'

session_unauth = usdt_perpetual.HTTP(
        endpoint=url)

session_auth = usdt_perpetual.HTTP(
        endpoint=url,
        api_key=api_key,
        api_secret=api_secret)

def get_single_orderbook(ticker):
    global session_unauth
    orderbook = session_unauth.orderbook(symbol=ticker)['result']
    return orderbook

def get_orderbook_api(ticker_1, ticker_2):
    global session_unauth

    # requesting orderbook data

    orderbook_ticker_1 = session_unauth.orderbook(symbol=ticker_1)['result']
    orderbook_ticker_2 = session_unauth.orderbook(symbol=ticker_2)['result']

    return orderbook_ticker_1, orderbook_ticker_2


def get_position_data(ticker):
    global session_auth

    position = session_auth.my_position(
        symbol=ticker)

    return position







