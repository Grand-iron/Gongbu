a=[]
b=10
for x in range(10):
    z=int(input())
    a.append(z%42)
for x in range(42):
    if a.count(x)>1:
        b=b-a.count(x)+1
print(b)