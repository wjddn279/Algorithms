import sys
sys.stdin = open("input.txt")

from _collections import deque

T = int(input())

def prin(a):
    for i in a:
        print(i)
    print()

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    elif matrix[x][y] == 0 : return False
    else : return True

def bfs(x,y):
    queue = deque()
    for i in range(4):
        if i in dic[matrix[x][y]]:
            visited[x][y][i] = 1
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) and not visited[nx][ny][i]:
                if i in dic[matrix[nx][ny]]:
                    queue.append((nx,ny,i,2))
                    visited[nx][ny][i] = 1
    while queue:
        x,y,d,cnt = queue.popleft()
        if cnt > L:
            return 0
        for num in dic[matrix[x][y]][d]:
            nx,ny = x+dx[num],y+dy[num]
            if iswall(nx, ny) and not visited[nx][ny][num] and cnt < L:
                if num in dic[matrix[nx][ny]]:
                    queue.append((nx,ny,num,cnt+1))
                    visited[nx][ny][num] = 1


for test_case in range(1,T+1):
    global N,M,L
    N,M,R,C,L = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 상 하 좌 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dic = {1:{0:[0,2,3],1:[1,2,3],2:[0,1,2],3:[0,1,3]},2:{0:[0],1:[1]},3:{2:[2],3:[3]},4:{1:[3],2:[0]},5:{0:[3],2:[1]},6:{0:[2],3:[1]},7:{1:[2],3:[0]}}
    visited = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
    bfs(R,C)
    answer = 0
    for i in range(N):
        for j in range(M):
            for num in visited[i][j]:
                if num:
                    answer+=1
                    break
    if L == 1:
        print('#{} {}'.format(test_case,1))
    else:
        print('#{} {}'.format(test_case,answer))