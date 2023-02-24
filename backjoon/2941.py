cro=['c=','c-','d-','lj','nj','s=','z=']
count=0
a=input()
for x in cro:
    count+=a.count(x)
count+=(a.count('dz=')*2)
if x in 'z=' and 'dz=':
    count-=(a.count('dz='))
print(len(a)-count)
