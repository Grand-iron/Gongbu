n=int(input())
a=[]
k=[]
for x in range(n):
    word=list(input())
    a.append(''.join(word))
    word.reverse()
    k.append(''.join(word))
for x in k:
    for y in a:
        if x==y:
            password=y
password=list(password)
L=len(password)
print(L,password[int(L/2)])