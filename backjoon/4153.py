x=[]
z=0
while(True):
    a,s,d=input().split()
    a=int(a)*int(a)
    s=int(s)*int(s)
    d=int(d)*int(d)
    if int(a)==0 and int(s)==0 and int(d)==0:
        break
    elif a+s==d:
        x.append("right")
    elif d+s==a:
        x.append("right")
    elif a+d==s:
        x.append("right")
    else:
        x.append("wrong")
for n in x:
    print(n)