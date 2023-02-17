from collections import deque
A=input()
A=int(A)
for _ in range(A):
    Q=deque()
    S = deque()
    B,C=input().split()
    B,C=int(B),int(C)
    for i in range(B):
        S.append(i)
    D=input().split()
    for i in D:
        i=int(i)
        Q.append(i)
    c=0
    while Q:
        if max(Q)==Q[0]:
            comp = Q.popleft()
            count = S.popleft()
            c += 1
            if count==C:
                break
            continue
        else:
            comp = Q.popleft()
            count = S.popleft()
            Q.append(comp)
            S.append(count)
    print(c)