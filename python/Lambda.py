def xORy(x, y):

    if x >= y:
        return x
    else:
        return y

mx = lambda x,y: x if x >= y else y


print(xORy(9,5))
print(mx(9,5))