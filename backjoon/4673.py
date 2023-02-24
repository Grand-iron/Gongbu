L=[]

for x in range(1,10001):
    a=x
    for y in list(str(x)):
        a+=int(y)
    L.append(a)
    if x not in L:
        print(x)