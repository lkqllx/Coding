'''Mistakes!!'''

'''Try to use inline if statement'''
print(1 if True else 0)

'''Try to separate large number'''
million = 100_000_000
ten_thousand = 10_000
print(million+ten_thousand)
print(f'{(million+ten_thousand):,}')

'''Using context manager to open and close a file'''
with open('sample.txt', 'r') as f:
    file = f.readlines()
# print(file)

'''!!!!!!!!!!Use zip to combine two list!!!!!!!'''
chars = ['a', 'b' ,'c', 'd']
numbers = [1, 2, 3, 4]

for char, num in zip(chars, numbers):
    print(f'{char} is in position of {num}')

'''!!!!!Use * to unpack'''
a, b, *c, d = [1, 2, 3, 4, 5]
print(c)
print(d)

'''!!!!!!setattr and getattr to iteratively set attribute'''
class Person():
    pass

p = Person()
info = {'first': 'Andrew', 'last': 'LI'}
for first, name in info.items():
    setattr(p, first, name)

for key in info.keys():
    print(f'{getattr(p, key)}')

'''Use getpass to keep password secret'''
# from getpass import getpass
# user_name = input('Username:')
# password = getpass('Password:')

'''!!!!!When using method to default create a EMPTY list, the list will be created only once'''
def add_attr(attr, attrs = []):
    attrs.append(attr)
    print(attrs)

add_attr('Andrew')
add_attr('LI')


'''!!!!!The zip file can only be iterated once!!!'''
chars = ['a', 'b' ,'c', 'd']
numbers = [1, 2, 3, 4]
combined_list = zip(chars, numbers)
print(list(combined_list))
print(list(combined_list))

