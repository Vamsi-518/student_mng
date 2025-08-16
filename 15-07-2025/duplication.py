def unique_tuple(t):
    u = ()
    for x in t:
        if x not in u:
            u += (x,)
    return u

t1 = (1,9,1,6,3,4,5,1,1,2,5,6)
print(unique_tuple(t1))
