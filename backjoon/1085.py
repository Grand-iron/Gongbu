x,y,w,h=input().split()

L1=int(w)-int(x)
L2=int(h)-int(y)
def asd(a,s ,d ,f ):
    if a<=s:
        if a<=d:
            if a<=f:
                print(a)
                quit()
asd(int(x),int(y),int(L1),int(L2))
asd(int(y),int(x),int(L1),int(L2))
asd(int(L1),int(x),int(y),int(L2))
asd(int(L2),int(x),int(y),int(L1))