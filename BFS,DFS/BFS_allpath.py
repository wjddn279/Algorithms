def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= 10 or y >= 10:
        return False
    else:
        return True
def bfs(x,y):
    queue = deque()
    queue.append((x,y,0,[(x,y)]))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while queue:
        a,b,count,step = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if wall(nx,ny):
                if (nx,ny) not in step:
                    if matrix[nx][ny] == 1:
                        print(len(step))
                    else :
                        queue.append((nx,ny,count+1,step+[(nx,ny)]))
    return 0

matrix = [[0 for _ in range(10)] for _ in range(10)]
matrix[7][7] = 1
bfs(0,0)