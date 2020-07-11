def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
matrix = [[0 for _ in range(4)] for _ in range(4)]
matrix[3][3] = 1

from _collections import deque

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= 4 or y >= 4:
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
                        print(step)
                    else :
                        queue.append((nx,ny,count+1,step+[(nx,ny)]))
    return 0


bfs(0,0)







# visited = [[0 for _ in range(4)] for _ in range(4)]
# prin(matrix)
# print(bfs(0,0))
#
# queue = deque()
# queue.append((x, y, 0, [(x, y)]))
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# while queue:
#     a, b, number, foot_step = queue.popleft()
#     for i in range(4):
#         nx = a + dx[i]
#         ny = b + dy[i]
#         if wall(nx, ny):
#             if (nx, ny) not in foot_step:
#                 if matrix[nx][ny] == 1:
#                     print(foot_step)
#                 else:
#                     queue.append((nx, ny, number + 1, foot_step + [(nx, ny)]))
#                     visited[x][y] = 1
# # return 0