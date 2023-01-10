n=int(input())
a=input().split()
while(True):
    count=0
    for x in a:
        if int(x)>=n:
            count+=1
    if count>=n:
        print(n)
        break
    else:
        n-=1