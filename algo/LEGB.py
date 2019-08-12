'''
L: Local
E: Enclosing
G: Global
B: Built-in
'''

'''interpretate of global and local variable'''
# x = 'global_x'
#
# def func():
#     # global x
#     x = 'local_x'
#     print(x)module 'thread' has no attribute 'start_new_thread'
#
# func()
# print(x)

'''input s'''

y = 'global y'

def func(z):
    print(z)
    z = 'local_y'
    print(z)

func(y)

print(y)