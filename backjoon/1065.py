a=int(input())
count=0
if a<100:
    print(a)
else:
    for x in range(100,a+1):
        k=list(str(x))
        if (int(k[1])-int(k[0]))==(int(k[2])-int(k[1])):
            count+=1
    print(99+count)