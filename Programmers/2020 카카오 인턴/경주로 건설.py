def prin(a):
    for i in a:
        print(*i)
    print()
from _collections import deque

def iswall(x,y,N,M,board):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    elif board[x][y] == 1: return False
    else: return True

def iscorner(now,next):
    if now == 0 or now == 1:
        if next == 0 or next == 1:
            return False
        else:
            return True
    else:
        if next == 2 or next == 3:
            return False
        else:
            return True


def bfs(board):
    N, M = len(board), len(board[0])
    # 상 하 좌 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[[float('inf') for _ in range(4)] for _ in range(M)] for _ in range(N)]
    visited[0][0] = [0,0,0,0]
    queue = deque()
    if board[0][1] == 0:
        queue.append((0,1,3,100))
        visited[0][1][3] = 100
    if board[1][0] == 0:
        queue.append((1, 0, 1, 100))
        visited[1][0][1] = 100
    while queue:
        x,y,dir,price = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iscorner(dir,i):
                temp = price + 600
            else:
                temp = price + 100
            if iswall(nx,ny,N,M,board) and visited[nx][ny][i] > temp:
                queue.append((nx,ny,i,temp))
                visited[nx][ny][i] = temp
    return min(visited[M-1][N-1])


def solution(board):
    return bfs(board)

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))