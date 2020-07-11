from _collections import deque
import sys
sys.stdin = open("input7.txt")

def isWall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= len(matrix) or y >= len(matrix):
        return False
    elif visited[x][y]:
        return False
    elif matrix[x][y] == 1:
        return False
    else:
        return True
def search():
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 2:
                return i,j
def bfs(x,y):
    que = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while True:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx,ny):
                if matrix[nx][ny] == 3:
                    return number[x][y]
                else:
                    que.append([nx,ny])
                    number[nx][ny] = number[x][y] + 1
                    visited[nx][ny] = 1
        if que:
            x,y = que.popleft()
        else:
            return 0
T = int(input())

for test_case in range(1,T+1):

    length = int(input())
    matrix = [list(map(int,input())) for _ in range(length)]
    visited = [[0 for _ in range(length)] for _ in range(length)]
    number = [[0 for _ in range(length)] for _ in range(length)]
    x,y = search()
    print('#{} {}'.format(test_case,bfs(x,y)))
