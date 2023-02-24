import sys
input = sys.stdin.readline
n, b = map(int, input().split())
avc = list(map(int, input().split()))
badak = 0  
h = max(avc)
ans = 0
while badak <= h:
    total = 0
    middle = (badak + h) // 2
    for i in range(n):
        rest = avc[i] - middle
        if rest > 0:
            total += rest
            if total > b:
                break
    if total >= b:
        ans = middle
        badak = middle + 1
    if total < b:
        h = middle - 1

print(ans)