from config_REST_api_connect import session_unauth
from config_REST_api_connect import session_auth
from config_REST_api_connect import get_orderbook_api
from func_calculations import get_single_trade_details
from func_price_calls import get_latest_klines
from func_stats import calculate_metrics
from config_execution_api import ticker_1
from config_execution_api import ticker_2




#get latest zscore
def get_latest_zscore():

    #get latest asset orderbook prices and add dummy price for latest
    orderbook_ticker_1, orderbook_ticker_2 = get_orderbook_api(ticker_1, ticker_2)

    mid_price_1, _, _, = get_single_trade_details(orderbook_ticker_1)
    mid_price_2, _, _, = get_single_trade_details(orderbook_ticker_2)

    #Get Latest Price History Kline
    series_1, series_2 = get_latest_klines()

    #Get ZScore and confirm if HOT
    if len(series_1) > 0 and len(series_2) > 0:

        #replace last kline price with latest orderbook mid price
        series_1 = series_1[:-1]
        series_2 = series_2[:-1]
        series_1.append(mid_price_1)
        series_2.append(mid_price_2)

        #get latest zscore and check if still cointegrated. if there is a requirement for cointegration, call coint flag from calculate metrics, if not, leave blank
        coint_flag, zscore_list = calculate_metrics(series_1, series_2)
        zscore = zscore_list[-1]
        if zscore > 0:
            signal_sign_positive = True
        else:
            signal_sign_positive = False


        return (coint_flag, zscore, signal_sign_positive)

    return

