a=list(input().split())
b=0
for x in range(5):
    b+=((int(a[x])*int(a[x])))
print(b%10)