import sys
sys.stdin  = open("input.txt")

from _collections import deque

def isout(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else : return True

def sol(location):
    queue = deque()
    queue.append(location)
    visited[location[0][0]][location[0][1]][location[1][0]][location[1][1]] = 1
    while queue:
        now = queue.popleft()
        x1,y1 = now[0]
        x2,y2 = now[1]
        if x1 == x2 and y1 == y2:
            continue
        cnt = now[2]
        if cnt > 9:
            return -1
        for i in range(4):
            nx1,ny1 = x1+dx[i],y1+dy[i]
            nx2,ny2 = x2+dx[i],y2+dy[i]
            # 둘다 안
            if isout(nx1,ny1) and isout(nx2,ny2):
                if matrix[nx1][ny1] != '#' and matrix[nx2][ny2] == '#' and not visited[nx1][ny1][x2][y2]:
                    queue.append([[nx1,ny1],[x2,y2],cnt+1])
                    visited[nx1][ny1][x2][y2] = 1
                elif matrix[nx1][ny1] == '#' and matrix[nx2][ny2] != '#' and not visited[x1][y1][nx2][ny2]:
                    queue.append([[x1,y1],[nx2,ny2],cnt+1])
                    visited[x1][y1][nx2][ny2] = 1
                elif matrix[nx1][ny1] != '#' and matrix[nx2][ny2] != '#' and not visited[nx1][ny1][nx2][ny2]:
                    queue.append([[nx1,ny1],[nx2,ny2],cnt+1])
                    visited[nx1][ny1][nx2][ny2] = 1
            elif not isout(nx1,ny1) and not isout(nx2,ny2):
                continue
            else:
                return cnt+1
    return -1
global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
location = [[i,j] for i in range(N) for j in range(M) if matrix[i][j] == 'o']+[0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
result = sol(location)
print(result)
