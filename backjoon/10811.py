a,b=input().split()
L=[]
for x in range(int(a)):
    L.append(x+1)
N=0
for x in range(int(b)):
    q,w=input().split()
    N1=int(q)
    N2=int(w)
    while N1<N2:
        N=L[N1-1]
        L[N1-1]=L[N2-1]
        L[N2-1]=N
        N1+=1
        N2-=1
for x in L:
    print(x,end=" ")        