'''This word is to learn what is first-class function
The website can be reached at https://dbader.org/blog/python-first-class-functions

One of key concept in Python is that function is a OBJECT'''

# def yell(text):
#     return text.upper() + '!'
#
# print(yell('hello'))
#
# bark = yell # object


'''Pass function as argument'''
# print(bark('qwe'))
# print(bark.__qualname__)
#
def greeting(func):
    print(func('Hi, I am Andrew'))
#
# def lower(text: str):
#     return text.capitalize() + '...'
# greeting(lower)

'''Nested function'''
# def get_speak_func(threshold):
#     def yell(text: str) -> str:
#         return text.upper() + '!'
#
#     def whisper(test: str) -> str:
#         return test.lower() + '...'
#     if threshold > 0.5:
#         return yell
#     else:
#         return whisper
#
# greeting(get_speak_func(0))

'''Nested function can also capture the parent's state or value'''
# def get_speaker_func(text:str, threshold:float):
#     def whisper():
#         return text.lower() + '...'
#
#     def yell():
#         return text.upper() + '!'
#
#     if threshold > 0.5:
#         return yell
#     else:
#         return whisper
#
# print(get_speaker_func('hEllo', 0.8)())

'''The sub-function will remember the parent's value referring to lexical enclosure'''
# def makeprod(n: int):
#     def prod(value):
#         return value * n
#     return prod
#
# prod_3 = makeprod(3)
# print(prod_3(2))

'''!!! we can use __call__ to make objects callable'''
class MakeAdd:
    def __init__(self, n:int):
        self.n = n
    def __call__(self, value):
        return value + self.n

adder = MakeAdd(3)
print(adder(8))







