"""
Everything in Python is an Object

Even a class
"""

Student = type('Student', (object,), {'__author__': 'Andrew'})
print(Student)

andrew = Student()
print(andrew.__author__)