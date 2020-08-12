import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def iswall(x,y):
    if x <0 or y < 0:
        return False
    elif x >= N or y >= M :
        return False
    elif matrix[x][y] == '*':
        return False
    else:
        return True

def bfs(x,y):
    queue = deque()
    if matrix[x][y] == '.':
        queue.append((x,y))
        visited[x][y] = 1
    else:
        if matrix[x][y].islower():
            key.append(matrix[x][y])
            visited[x][y] = 1
            temp = matrix[x][y].upper()
            if temp in block:
                for point in block[temp]:
                    if matrix[point[0]][point[1]] == temp:
                        queue.append(point)
            matrix[x][y] = '.'
            queue.append((x,y))
        else:
            temp = matrix[x][y]
            if temp.lower() in key:
                queue.append((x,y))
                visited[x][y] = 1
                matrix[x][y] = '.'
            else:
                # 벽에 막혔어? 그럼 기억해 둬
                if matrix[x][y] not in block:
                    block[matrix[x][y]] = [(x,y)]
                else:
                    block[matrix[x][y]] += [(x, y)]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not visited[nx][ny]:
                if matrix[nx][ny] == '$':
                    result.append((nx,ny))
                    matrix[nx][ny] = '.'
                if matrix[nx][ny] != '.':
                    if matrix[nx][ny].islower():
                        key.append(matrix[nx][ny])
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        temp = matrix[nx][ny].upper()
                        if temp in block:
                            for point in block[temp]:
                                if matrix[point[0]][point[1]] == temp:
                                    queue.append(point)
                        matrix[nx][ny] = '.'
                    else:
                        temp = matrix[nx][ny]
                        if temp.lower() in key:
                            queue.append((nx,ny))
                            visited[nx][ny] = 1
                            matrix[nx][ny] = '.'
                        else:
                            # 벽에 막혔어? 그럼 기억해 둬
                            if matrix[nx][ny] not in block:
                                block[matrix[nx][ny]] = [(nx,ny)]
                            else:
                                block[matrix[nx][ny]] += [(nx,ny)]
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

T = int(input())

for _ in range(T):

    global N,M
    N, M = map(int,input().split())
    matrix = [list(input()) for _ in range(N)]
    key = list(input())
    if key == ['0']:
        key = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    block = {}
    result = []
    cnt = 0
    for j in range(M):
        for i in [1,N-1]:
            if matrix[i][j] == '$':
                result.append((i,j))
                matrix[i][j] = '.'
            if matrix[i][j] != '*':
                bfs(i, j)

    for i in range(1,N-1):
        for j in [0,M-1]:
            if matrix[i][j] == '$':
                result.append((i,j))
                matrix[i][j] = '.'
            if matrix[i][j] != '*':
                bfs(i, j)

    print(len(result))