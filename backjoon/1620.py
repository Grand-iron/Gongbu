n,m=input().split()
a={}
a2={}
q=[]
for x in range(int(n)):
  z=input()
  a[x+1]=z
  a2[z]=x+1
for x in range(int(m)):
  q.append(input())
for x in q:
  if x.isdigit() is True:  #isdigit = 오직 숫자인지 판별함
    print(a[int(x)])
  else:
    print(a2[x])
   