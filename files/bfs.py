import sys
sys.stdin = open("bfs.txt")

from _collections import deque
T = int(input())

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

def bfs(x,N):
    visited = [x]
    deq = deque()
    while True:
        for i in range(1,N+1):
            if matrix[x][i] == 1 and i not in visited:
                deq.append(i)
                visited.append(i)
        if len(deq)== 0:
            return visited
        else:
            x = deq.popleft()

def bfs1(x,y,N):
    visited = [x]
    cnt = [0 for _ in range(N+1)]
    deq = deque()
    while True:
        for i in range(1,N+1):
            if matrix[x][i] == 1 and i not in visited:
                if i == y:
                    return cnt[x] + 1
                else:
                    deq.append(i)
                    cnt[i] = cnt[x] + 1
                    visited.append(i)
        x = deq.popleft()

for test_case in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    print(data)
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(len(data)):
        matrix[i+2][data[i]] = 1
        matrix[data[i]][i+2] = 1
    prin(matrix)
    result = bfs(1,N)
    num = 0
    print(result)
    for i in range(len(result)-1):
        num += bfs1(result[i],result[i+1],N)
    print('#{} {}'.format(test_case,num))