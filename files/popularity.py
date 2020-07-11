import sys
sys.stdin = open("popularity.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def wall(nx,ny,x,y):
    if nx < 0 or ny < 0:
        return False
    elif nx >= N or ny >= N:
        return False
    elif L <= abs(matrix[nx][ny] - matrix[x][y]) <= R:
        return True

def solve(result):
    flag = False
    for i in range(N):
        for j in range(N):
            if visi[i][j] == 0:
                stack,value = bfs(i,j)
                if len(stack) != 1:
                    for point in stack:
                        matrix[point[0]][point[1]] = value
                    flag = True
    if flag:
        return result+1,flag
    else:
        return result,flag


def bfs(x,y):

    visi[x][y] = 1
    queue = deque()
    stack = []
    queue.append((x,y))
    stack.append((x,y))
    result = matrix[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if wall(nx,ny,x,y):
                if visi[nx][ny] == 0:
                    stack.append((nx,ny))
                    queue.append((nx,ny))
                    visi[nx][ny] = 1
                    result += matrix[nx][ny]
    return stack, int(result/len(stack))


# N : matrix 길이, L : 작은값, R : 큰값
global N, L, R
N, L, R = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
flag = True
result = 0
while flag:
    visi = [[0 for _ in range(N)] for _ in range(N)]
    result,flag = solve(result)
print(result)