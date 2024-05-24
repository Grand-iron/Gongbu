n,m=input().split()
a=[]
a2=[]
q=[]
for x in range(int(n)):
  z=input()
  a.append(z)
for x in range(int(m)):
  a2.append(input())
hap=set(a)&set(a2)
q=list(hap)
q.sort()
print(len(q))
for x in q:
  print(x)