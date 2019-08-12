import pandas_datareader as web
import pandas as pd
import datetime as dt
import time

start = dt.datetime(2015,1,1)
# end = dt.datetime(2019,5,10)
# google = web.DataReader('GOOGL','iex', start=start, end=end)
# print(google.tail())

# def timer(func):
#     def timer_wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         end = time.perf_counter()
#         time_comsumed = end - start
#         print(f'Total time elapsesd: {time_comsumed}')
#         return func(*args, **kwargs)
#     return timer_wrapper
#
# @timer
# def waste_time(iter):
#     for _ in range(iter):
#         pass
#     return 'Yes'
#
# print(waste_time(100000))

import threading
def sleep(num):
    print(f'Thread {num}: before sleeping')
    time.sleep(2)
    print(f'Thread {num}: end sleeping')

for idx in range(3):
    thread = threading.Thread(target=sleep, args=(idx,))
    thread.start()
    thread.join()

