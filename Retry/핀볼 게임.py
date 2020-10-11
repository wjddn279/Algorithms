# 5시 00분
import sys
sys.stdin = open("input.txt")

T = int(input())

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else: return True

def move(sx,sy,d):
    result = 0
    x,y = sx,sy
    while True:
        nx,ny = x+dx[d],y+dy[d]
        if not iswall(nx,ny) or 0 < matrix[nx][ny] <= 5:
            while not iswall(nx,ny) or 0 < matrix[nx][ny] <= 5:
                result += 1
                if not iswall(nx,ny):
                    nd = direction[5][d]
                    nx,ny = nx+dx[nd],ny+dy[nd]
                else:
                    nd = direction[matrix[nx][ny]][d]
                    nx,ny = nx+dx[nd],ny+dy[nd]
                d = nd
        if 6 <= matrix[nx][ny] <= 10:
            x,y = dic[(nx,ny)]
        if iswall(nx,ny) and matrix[nx][ny] <= 0:
            x,y = nx,ny
        if matrix[x][y] == -1 or (x==sx and y ==sy):
            return result


for test_case in range(1,T+1):
    global N
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    start,holes = [],[[] for _ in range(11)]
    direction = [[],[2,3,1,0],[2,0,3,1],[3,2,0,1],[1,3,0,2],[2,3,0,1]]
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    dic = {}
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                start.append((i,j))
            elif matrix[i][j]> 5:
                holes[matrix[i][j]].append((i,j))
    for i in range(6,11):
        for idx,arr in enumerate(holes[i]):
            dic[arr] = holes[i][abs(idx-1)]
    answer = 0
    for x,y in start:
        for i in range(4):
            answer = max(answer,move(x,y,i))
    print('#{} {}'.format(test_case,answer))
