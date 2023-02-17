import sys

n=int(sys.stdin.readline())
a=sys.stdin.readline().rstrip()
b=31
c=1234567891
sum=0
for x in range(n):
    k=ord(a[x])-ord('a')+1
    sum+=k*(b**x)
print(sum%c)