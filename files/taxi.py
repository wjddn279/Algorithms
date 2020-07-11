from _collections import deque
import sys
sys.stdin = open("taxi.txt")

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x>= len(matrix) or y>= len(matrix):
        return False
    elif matrix[x][y] == 1:
        return False
    else:
        return True

def bfs(x,y,energy):
    if matrix[x][y] in start:
        value=matrix[x][y]
        matrix[x][y]=0
        return [x,y,value,energy]
    visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    visited[x][y] = 1
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    queue = deque()
    queue.append((x,y,0))
    maximum = 9999999999
    result=[999999999,99999999999]
    while queue:
        x,y,dist = queue.popleft()
        if dist >= energy:
            return [-1,-1,-1,-1]
        if dist > maximum:
            matrix[result[0]][result[1]] = 0
            return result
        if matrix[x][y] in start:
            if x < result[0] or (x == result[0] and y < result[1]):
                value = matrix[x][y]
                maximum = dist
                result = [x, y, value, energy - dist]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if wall(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny,dist+1))
    if maximum == 9999999999:
        return [-1,-1,-1,-1]
    else:
        matrix[result[0]][result[1]] = 0
        return result

def solve(x,y,target_x,target_y,energy):
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    queue = deque()
    queue.append((x,y,0))
    visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    visited[x][y] = 1
    while queue:
        x,y,dist = queue.popleft()
        if dist < energy:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if wall(nx,ny) and not visited[nx][ny]:
                    if nx == target_x and ny == target_y:
                        return [nx,ny,energy+dist+1]
                    else:
                        visited[nx][ny] = 1
                        queue.append([nx,ny,dist+1])
        else:
            return [-1,-1,-1]
    return [-1,-1,-1]

length,number,energy = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(length)]
x,y = map(int,input().split())
x,y = x-1,y-1
start,end = [],[]
for i in range(number):
    a,b,c,d = map(int,input().split())
    matrix[a-1][b-1] = i+2
    end.append((c-1,d-1))
    start.append(i+2)

for i in range(number):
    x,y,value,energy = bfs(x,y,energy)
    if energy == -1:
        print(-1)
        break
    x,y,energy = solve(x,y,end[value-2][0],end[value-2][1],energy)
    if energy == -1:
        print(-1)
        break
else:
    print(energy)