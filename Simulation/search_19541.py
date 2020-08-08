import sys
sys.stdin = open("search.txt")

N, M = map(int,input().split())
data = []
for i in range(M):
    temp = list(map(int,input().split()))
    data.append(temp[1:temp[0]+1])
last = list(map(int,input().split()))

result = last[:]
for i in range(M-1,-1,-1):
    for num in data[i]:
        if result[num-1] == 0:
            for k in data[i]:
                result[k-1] = 0
            break
state = result[:]
for i in range(M):
    for idx in data[i]:
        if state[idx-1] == 1:
            for idx in data[i]:
                state[idx-1] = 1
            break

if state == last:
    print('YES')
    print(*result)
else:
    print('NO')