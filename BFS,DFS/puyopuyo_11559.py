import sys
from _collections import deque
sys.stdin = open("input10.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
def search():
    result = []
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                result.append([i,j,matrix[i][j]])
    return  result
def wall(nx,ny,color):
    if nx < 0 or ny < 0:
        return False
    elif nx >= 12 or ny >= 6:
        return False
    elif matrix[nx][ny] != color:
        return False
    else:
        return True
def bfs():
    can = search()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    flag = False
    for i in can:
        x,y,color = i
        if matrix[x][y] != '.':
            queue = deque()
            queue.append((x,y))
            step = [(x,y)]
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if wall(nx,ny,color):
                        if (nx,ny) not in step:
                            queue.append((nx,ny))
                            step.append((nx,ny))
            if len(step) >= 4:
                flag = True
                for st in step:
                    matrix[st[0]][st[1]] = '.'
    return flag

def sorting():
    mat = [['.' for _ in range(6)] for _ in range(12)]
    res =[[] for _ in range(6)]
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                res[j].append(matrix[i][j])
    for i in range(6):
        for j in range(11,11-len(res[i]),-1):
            a = res[i].pop()
            mat[j][i] = a

    return mat

matrix = [list(input()) for _ in range(12)]
cnt = 0
while True:
    flag = bfs()
    if flag:
        cnt += 1
        matrix = sorting()
    else:
        break
print(cnt)

