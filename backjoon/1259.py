a=list(input())
ans=[]
while(a[0]!='0'):
    count=0
    c=len(a)
    if c%2!=0:
        d=(c-1)/2
    else:
        d=c/2
    for x in range(int(d)):
        if a[x]==a[c-(x+1)]:
            count+=1
    if count==int(d):
        ans.append('yes')
    else:
        ans.append('no')
    a=list(input())
for x in ans:
    print(x)