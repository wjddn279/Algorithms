import sys
sys.stdin = open("a.txt")

from _collections import deque

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

def bfs(x,y,M):
    visited.append(x)
    deq = deque()
    while True:
        for i in range(M+1):
            if matrix[x][i] == 1 and i not in visited:
                if i == y:
                    return num[x] + 1
                else:
                    deq.append(i)
                    num[i] = num[x] + 1
                    visited.append(i)
        if len(deq) == 0:
            return 0
        else:
            x = deq.popleft()

T = int(input())
for test_case in range(1,T+1):
    M,N = map(int,input().split())
    matrix = [[0 for _ in range(M+1)] for _ in range(M+1)]
    visited = []
    num = [0 for _ in range(M+1)]
    for i in range(N):
        x,y = map(int,input().split())
        matrix[x][y],matrix[y][x] = 1,1
    start,end = map(int,input().split())
    print('#{} {}'.format(test_case,bfs(start,end,M)))