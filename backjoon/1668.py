n=int(input())
a=[]
z=0
count=0
count2=0
for x in range(n):
    a.append(int(input()))
for x in a:
    if z<x:
        z=x
        count+=1
z=0
for x in reversed(a):
    if z<x:
        z=x
        count2+=1
print(count)
print(count2) 