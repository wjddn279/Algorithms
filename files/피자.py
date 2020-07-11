import sys
sys.stdin = open("피자.txt")

from _collections import deque

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())
    li = list(map(int,input().split()))
    data = deque(li)
    deq = deque()
    cir = deque()
    for i in range(N):
        var = data.popleft()
        deq.append(var)
        cir.append(var)
    result = []
    while len(result) != M:
        if deq[0] == 0:
            result.append(cir.popleft())
            deq.popleft()
            if len(data) != 0:
                next = data.popleft()
                cir.append(next)
                deq.append(next//2)
        else:
            num = deq.popleft()
            deq.append(num//2)
            k = cir.popleft()
            cir.append(k)
    for i in range(M):
        if li[i] == result[M-1]:
            ans = i
    print('#{} {}'.format(test_case,ans+1))
