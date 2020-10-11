# 2시 53분

import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()
# 쏜 횟수, 남은 것

import copy
from _collections import deque

T = int(input())

def rec(k,n,step):
    if k == n:
        can.append(step)
        return
    for i in range(M):
        rec(k+1,n,step+[i])

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else : return True

def shoot(n,temp):
    for i in range(N):
        if now[i][n]:
            queue = deque()
            queue.append((i,n,now[i][n]))
            while queue:
                x,y,b = queue.popleft()
                if now[x][y]:
                    now[x][y] = 0
                    temp -= 1
                for k in range(b):
                    for j in range(4):
                        nx,ny = x+k*dx[j],y+k*dy[j]
                        if iswall(nx,ny) and now[nx][ny]:
                            if now[nx][ny] > 1:
                                queue.append((nx,ny,now[nx][ny]))
                            now[nx][ny] = 0
                            temp -= 1
            return temp
    return temp
def down():
    for j in range(M):
        for i in range(N-2,-1,-1):
            for l in range(i,N-1):
                if now[l][j] and not now[l+1][j]:
                    now[l][j],now[l+1][j] = now[l+1][j],now[l][j]
                else:
                    break

for test_case in range(1,T+1):
    global K,M,N,answer
    K, M, N = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    can = []
    answer = float('inf')
    rec(0,K,[])
    total = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                total += 1
    for arr in can:
        now = copy.deepcopy(matrix)
        temp = total
        for num in arr:
            temp = shoot(num,temp)
            down()
        answer = min(answer,temp)
        if answer == 0:
            break
    print('#{} {}'.format(test_case,answer))