a=50
b=201
c=0
def gcd(m,n):
    c=m
    m=n
    n=c   
    return(m,n)
a,b=gcd(a,b)
print(a,b)
