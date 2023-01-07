import math
a,b,c=input().split()

d=int(c)-int(a)
z=int(a)-int(b)
z=math.ceil(d/z)
print(int(z)+1)