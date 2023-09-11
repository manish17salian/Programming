def lonelyinteger(a):
    x = -1
    a.sort()
    if len(a) == 1:
        return a[0]
    else:
        for i in a:
            if a.count(i) == 1:
                x = i
    return x

s = lonelyinteger([34,95,34,64,45,95,16,80,80,75,3,25,75,25,31,3,64,16,31])
print(s)