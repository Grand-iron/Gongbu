n=input()
z=int(n)
a=0
w=0
if z<9:
    if z%2==0:
        a=a+int((z/2))
elif z<18:
    if z%2==0:
        a=a+int((z/2))
    else:
        a=a+9
else:
    for x in range(len(n)):
        a+=9
for x in range(a):
    z=int(n)
    z-=a
    z+=x
    c=list(str(z))
    for y in range(len(c)):
        z+=int(c[y])
    if z==int(n):
        print(z-a+x)
        w=1
        break
if w==0:
    print(0)