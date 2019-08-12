import datetime as dt
import functools
import time
'''Example of decrator'''
# def my_decrator(func):
#     def wrapper():
#         print('Before execution...')
#         func()
#         print('After execution...')
#     return  wrapper
#
# def name():
#     print('andrew'.capitalize() + '...')
#
# decorated_name = my_decrator(name)
# decorated_name()

'''By using the @ to specify the decorator'''
# def not_in_daytime(func):
#     def wrapper():
#         if dt.datetime.now().hour > 22:
#             pass
#         else:
#             func()
#     return wrapper
#
# @not_in_daytime
# def say_hey():
#     print('Heyyyyyy')
#
# say_hey()

'''By using *args and **kwargs to take inputs'''
# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return  wrapper
#
# @do_twice
# def greeting(text: str):
#     print('Hey {}!'.format(text.capitalize()))
#
# @do_twice
# def say_hey():
#     print('Heyyyyyy')
#
# greeting('andrew')
# say_hey()

'''Return a value from decorator'''
# import functools
# def do_twice(func):
#     @functools.wraps(func) # to maintain the original name of say_hey while calling __name__
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @do_twice
# def say_hey(text):
#     print('Generate greetings...')
#     return f'Hi {text}'
#
# hi = say_hey('Andrew')
# print(hi)
# print(say_hey)

'''Write a decorator to count time'''
# def count_time(func):
#     @functools.wraps(func)
#     def time_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         func(*args, **kwargs)
#         end_time = time.perf_counter()
#         execution_time = (end_time - start_time)
#         print(f'Total execution time is {round(execution_time,2)}!!!')
#     return time_wrapper
#
# @count_time
# def waste_some_time(n):
#     for idx in range(n):
#         pass
#
# waste_some_time(100000000)


'''Write a decorator to accept args'''
# def repeat(num):
#     def repeat_wrapper(func):
#         def single_wrapper(*args, **kwargs):
#             for _ in range(num):
#                 func(*args, **kwargs)
#         return single_wrapper
#     return repeat_wrapper
#
# @repeat(num=4)
# def say_hey(text: str):
#     print(f'Heyyy {text.capitalize()}!')
#
# say_hey('andrew')


'''Write  a decorator to count the number of the function has been called'''
def count_calls(func):
    @functools.wraps(func)
    def count_wrapper(*args, **kwargs):
        count_wrapper.num_calls += 1
        print(f'Call {count_wrapper.num_calls} of {func.__name__}')
        func(*args, **kwargs)
    count_wrapper.num_calls = 0
    return count_wrapper

@count_calls
def say_hey(text: str):
    print(f'Heyyy {text.capitalize()}!')

say_hey('andrew')
say_hey('raven')





