a=input()
a=a.lower()
b='abcdefghijklmnopqrstuvwxyz'
c=a.count('a')
z=0
for x in b:
    if c<=a.count(x):
        c=a.count(x)
        d=x
for x in b:
    if c==a.count(x):
        z+=1
if z>=2:
    d='?'
print(d.upper())