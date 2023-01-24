a= int(input())
count=0
for x in range(1,a):
    if x**2 - (x-1)**2 > a:
        break
    for y in range(1,x+1):
        if x**2-y**2==a:
            count+=1
print(count)
