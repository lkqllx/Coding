def over_2(lst):
    new_lst = [x for x in lst if x > 2]
    return new_lst

lst = [1,2,3,4,5]

mx = list(filter(lambda x: x > 2, lst))

print(over_2(lst))
print(mx)