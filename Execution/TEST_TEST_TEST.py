
import datetime
from config_execution_api import kline_limit

now = datetime.datetime.now()
time_start_date = now - datetime.timedelta(days=kline_limit)
time_start_seconds = time_start_date.timestamp()
print(time_start_seconds)