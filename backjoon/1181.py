n=int(input())
a=[]
for x in range(n):
    a.append(input())
a=list(set(a))
a.sort()
a.sort(key=len)
for x in a:
    print(x)