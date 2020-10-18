import sys
sys.stdin = open("input.txt")

from _collections import deque

T = int(input())

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else : return True

def solve():
    while queue:
        # 위치, 팠는가 안팠는가, 지금 위치
        x,y,f,h,cnt,visited = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                # 팠으면
                if f:
                    if h > matrix[nx][ny] and (nx,ny) not in visited:
                        queue.append((nx,ny,f,matrix[nx][ny],cnt+1,visited+[(nx,ny)]))
                # 안팠어
                else:
                    # 안파고 가기
                    if h > matrix[nx][ny] and (nx,ny) not in visited:
                        queue.append((nx,ny,f,matrix[nx][ny],cnt+1,visited+[(nx,ny)]))
                    for j in range(1,K+1):
                        if h > matrix[nx][ny] - j and (nx,ny) not in visited:
                            queue.append((nx,ny,1,matrix[nx][ny]-j,cnt+1,visited+[(nx,ny)]))

    return cnt


for test_case in range(1,T+1):
    global N,K
    N,K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_height = 0
    for arr in matrix:
        max_height = max(max_height,max(arr))
    point = [(i,j,0,max_height,1,[(i,j)]) for i in range(N) for j in range(N) if matrix[i][j] == max_height]
    queue = deque(point)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    print('#{} {}'.format(test_case,solve()))