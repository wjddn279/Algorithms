import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)

import copy

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= N: return False
    else: return True

global N
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
answer = 0
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
route = [(i,j) for i in range(N) for j in range(N)]
result = 0
for start in range(0,N*N):
    answer = 0
    matrix = copy.deepcopy(mat)
    for idx in range(start,start+N*N):
        x,y = route[idx%len(route)]
        if matrix[x][y]:
            answer += 1
            for i in range(4):
                k = 1
                while iswall(x + k * dx[i], y + k * dy[i]):
                    matrix[x + k * dx[i]][y + k * dy[i]] = 0
                    k += 1
    if result < answer:
        result = answer
print(result)