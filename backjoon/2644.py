전체사람=int(input())
a=input().split()
촌수1=int(a[0])
촌수2=int(a[1])
리얼관계={x:[] for x in range(1,전체사람+1)}
q=0
for x in range(int(input())):
    a=input().split()
    리얼관계[int(a[0])].append(int(a[1]))
    리얼관계[int(a[1])].append(int(a[0]))

def gogo(key,value,count):
    answer=count+1
    check=[]
    while 리얼관계[key]:
        x=리얼관계[key].pop()
        if x==value:
            global q
            print(answer)
            q+=1
            break
        else:
            check.append(x)
    else:
        for x in check:
            gogo(x,value,answer)

gogo(촌수1,촌수2,0)
if q==0:
    print(-1)