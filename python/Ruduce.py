from functools import reduce

def multiply(lst):
    prod = 1
    for idx in range(len(lst)):
        prod *= lst[idx]

    return prod
lst = [1,2,3,4,5,6,7]

mx = reduce(lambda x,y: x * y, lst)

print(multiply(lst))
print(mx)