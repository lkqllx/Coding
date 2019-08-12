
class Student(object):
    pass

"""We can bind a method to an object but other object cannot have the method"""
from types import MethodType
# andrew = Student()
# raven = Student()

# def set_age(self, age):
#     self.age = age
#     # print(f'{self.__name__.capital()} is {age} years old')

# andrew.set_age = MethodType(set_age, andrew)
# andrew.set_age(25)
# print(andrew.age)


"""Alternatively, we can bind a class method for all objects"""
# Student.set_age = set_age
# raven.set_age(25)
# print(raven.age)

"""We can constrain the attributes in a class through __slots__"""
# class Graduates():
#     __slots__ = ('name', 'age') # Only name and age attrs are allowed
# andrew = Graduates()
# andrew.name = 'andrew'
# andrew.score  = 100
# print(andrew.name)
# print(andrew.score)


"""
Use @property and @method.setter to transfer a method to an attribute

The REASON why we wrote like below is we want to add some constraints to score
"""
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int): # Constraint 1
#             print('Score should be an integer!')
#             raise ValueError
#
#         if value > 100 or value < 0: # Constraint 2
#             print('Score should be in the range(0, 100)')
#             raise ValueError
#
#         self._score = value
#
# andrew = Student()
# andrew.score = 60
# print(andrew.score)


"""
Customize a class - Fibb
1.iterable
2.accessible
3.printable
4.handle unexpected attribute
"""
class Fibb():

    def __init__(self):
        self.a = 0
        self.b = 1

    def __str__(self):
        return f'Current number is - {self.a}'

    __repr__ = __str__

    def __getitem__(self, item):

        if isinstance(item, int):
            if item <= 1:
                return 0 if item == 0 else 1

            for _ in range(item - 1):
                self.a, self.b = self.b, self.a + self.b
            return self.a

        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start == None:
                start = 0

            L = list()
            for idx in range(stop):
                if idx >= start:
                    L.append(self.a)
                self.a, self.b = self.b, self.a + self.b
            return L

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration() # Has to be raise
        return self.a

    def __getattr__(self, item):
        print(f'/{item}')

f = Fibb()
print(f[110])
print([value for value in f])

print(Fibb.__class__)

