# 5시 20분

import sys
sys.stdin = open("input.txt")

T = int(input())

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else : return True

def dfs(x,y,direct,nums,ex,ey):
    global answer
    if len(direct) == 4 and x == ex and y == ey:
        answer = max(answer,nums)
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if iswall(nx,ny):
            val = matrix[nx][ny]
            if not direct:
                disert[val] = 1
                dfs(nx,ny,direct+[i],nums+1,ex,ey)
                disert[val] = 0
            elif i == direct[-1] and not disert[val]:
                disert[val] = 1
                dfs(nx,ny,direct,nums+1,ex,ey)
                disert[val] = 0
            elif i not in direct and not disert[val]:
                disert[val] = 1
                dfs(nx,ny,direct+[i],nums+1,ex,ey)
                disert[val] = 0

for test_case in range(1,T+1):
    global N
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    disert = [0 for _ in range(101)]
    answer = -1
    for i in range(N):
        for j in range(N):
            dfs(i,j,[],0,i,j)
    print('#{} {}'.format(test_case,answer))