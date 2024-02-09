a=int(input())*2-1
b=4
c=1
for x in range(a):
    for q in range(b):
      print(" ",end="")
    for w in range(c):
       print("*",end="")
    print("")
    if x+1>=a/2:
       b+=1
       c-=2
    else:
       b-=1
       c+=2