n = int(input())
 
count = n // 5
a = 0
n = n % 5
ans = -1
while n >= 0:
    if n % 3 == 0:
        a = n // 3
        ans = count + a
        break
 
    if count == 0:
        break
    count -= 1
    n += 5
 
print(ans)