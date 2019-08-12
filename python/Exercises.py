from functools import reduce
# Lambda
pairs = [(2, 'two'), (3, 'three'),(1, 'one'),  (4, 'four')]
pairs.sort(key=lambda x: x[0],reverse=True)
print(pairs)

# Map
list_words = ['big', 'small', 'able', 'about', 'hairdresser', 'laboratory']
print(*map(lambda x: len(x), list_words))

# Filter
print(*filter(lambda x: x % 2 == 1, range(-15,15)))

# Reduce
sentence = "Dis-moi ce. que. "
print(reduce(lambda x, y: x + y, list(map(lambda x: 1 if x.isalpha() else 0, list(sentence)))))

# A：4 B：9 Z:6

def find_ways(a,b,z):
    print([x for x in range(20) if x * a % b == z])
find_ways(3,5,4)

