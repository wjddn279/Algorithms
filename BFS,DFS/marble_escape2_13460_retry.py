import sys
sys.stdin = open("marble_escape2_13460.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
from _collections import deque

def init():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'R':
                red = [i,j]
            if matrix[i][j] == 'B':
                blue = [i,j]
            if matrix[i][j] == 'O':
                goal = (i,j)
    return red+blue+[0],goal

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    elif matrix[x][y] == '#':
        return False
    else:
        return True

def bfs():
    queue = deque()
    queue.append(location)
    while queue:
        print(queue)
        r_x,r_y,b_x,b_y,cnt = queue.popleft()
        if cnt > 9:
            return -1
        for i in range(4):
            red_flag = True
            blue_flag = True
            red_x,red_y,blue_x,blue_y = r_x,r_y,b_x,b_y
            r_f = True
            b_f = True
            for k in range(1,11):
                red_nx = red_x + dx[i]
                red_ny = red_y + dy[i]
                blue_nx = blue_x + dx[i]
                blue_ny = blue_y + dy[i]
                if red_flag:
                    red_flag = iswall(red_nx,red_ny)
                if blue_flag:
                    blue_flag = iswall(blue_nx,blue_ny)
                if red_flag or blue_flag:
                    if not red_flag:
                        red_nx,red_ny = red_x,red_y
                    if not blue_flag:
                        blue_nx,blue_ny = blue_x,blue_y
                    if (red_nx,red_ny) != (blue_nx,blue_ny):
                        if (blue_nx, blue_ny) == goal:
                            b_f = False
                        if (red_nx, red_ny) == goal:
                            red_nx,red_ny = -100,-100
                            r_f = False
                        red_x,red_y = red_nx,red_ny
                        blue_x,blue_y = blue_nx,blue_ny
                else:
                    break
            if r_f == False and b_f == False:
                continue
            elif r_f == True and b_f == False:
                continue
            elif r_f == False and b_f == True:
                return cnt + 1
            elif (red_x, red_y, blue_x, blue_y) not in visited:
                queue.append((red_x, red_y, blue_x, blue_y, cnt + 1))
                visited.append((red_x, red_y, blue_x, blue_y))
    return -1


global N,M
N,M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
location,goal = init()
visited = [(location[0],location[1],location[2],location[3])]
print(bfs())
