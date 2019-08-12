def function(*args, **kwargs):
    print(*args)
    print(kwargs)

q = "Elon Mask"
w = "Genius"
e = "Just Like Me"


function(q,w,e,a = 1, b = [1], c = 3)