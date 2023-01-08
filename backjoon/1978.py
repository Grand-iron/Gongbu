n=int(input())
count1=0
a=list(input().split())
for x in range(n):
    if int(a[x])>=2:
        count=0
        for y in range(2,int(a[x])):
            if int(a[x])%y!=0:
                count+=1
        if count==(int(a[x])-2):
            count1+=1
print(count1)
