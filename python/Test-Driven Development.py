"""
Test Driven Development - 单元测试
It is a development method by using a completing test class for testing the compatibility and correctness
of the codes, which can largely enhance the robustness of the code.
"""

"""
Suppose we write a new Dict class for test-driven development
Dict should have similar behavior as dict
Dict should be attribute-accessible
"""
class Dict:

    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            self.__dict__[item] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value

    def __setitem__(self, key, value):
        print(key)
        self.__dict__[key] = value

# Alternatively we can inherit from dict class

class Dict2(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def __getattr__(self, item):
        return self[item]

new_dict = Dict(a=1, b=2)
# new_dict = Dict2(a=1, b=2)
print(new_dict.__dict__)
print(new_dict.a)
print(new_dict['a'])
new_dict['c'] = 123
print(new_dict.c)
new_dict.d = 234
print(new_dict.d)