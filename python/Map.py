def square_list(lst):
    new_lst = []
    for idx in range(len(lst)):
        new_lst.append(lst[idx] ** 2)

    return new_lst

lst = [1,2,3,4]
mx = list(map(lambda x: x ** 2, lst))

print(square_list(lst))
print(mx)