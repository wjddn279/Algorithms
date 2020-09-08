import sys
sys.stdin = open("input.txt")

# 2시 50분

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N:
        return False
    elif matrix[x][y] == '1':
        return False
    else:
        return True

def check_turn(x,y,dir):
    if dir == 0:
        for i in range(x-1,x+2):
            for j in range(y,y+3):
                if not iswall(i,j):
                    return False
        return True
    else:
        for i in range(x,x+3):
            for j in range(y-1,y+2):
                if not iswall(i,j):
                    return False
        return True

def search():
    tree,des = [], []
    tree_dir,des_dir = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'B':
                tree.append((i,j))
            if matrix[i][j] == 'E':
                des.append((i,j))
    # 1 : 세로, 0 : 가로
    if tree[0][0] + 1 == tree[1][0]:
        tree_dir = 1
    if des[0][0] + 1 == des[1][0]:
        des_dir = 1
    return tree[0],des[0],tree_dir,des_dir


def bfs():
    while queue:
        x, y, dir, cnt = queue.popleft()
        if dir == 0:
            # 가로니까 위 아래로 이동
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 다음 똘마니들
                x1, y1, x2, y2 = nx, ny+1, nx, ny+2
                if iswall(nx, ny) and iswall(x1, y1) and iswall(x2, y2):
                    if (nx, ny) == des and dir == des_dir:
                        return cnt + 1
                    if visited[nx][ny][dir] > cnt+1:
                        visited[nx][ny][dir] = cnt + 1
                        queue.append((nx, ny, dir, cnt + 1))
            if check_turn(x,y,dir) and visited[x-1][y+1][1] > cnt +1:
                if (x-1, y+1) == des and des_dir == 1:
                    return cnt + 1
                queue.append((x-1,y+1,1,cnt+1))
                visited[x - 1][y + 1][1] = cnt + 1
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 다음 똘마니들
                x1, y1, x2, y2 = nx+1, ny, nx+2, ny
                if iswall(nx, ny) and iswall(x1, y1) and iswall(x2, y2):
                    if (nx, ny) == des and dir == des_dir:
                        return cnt + 1
                    if visited[nx][ny][dir] > cnt + 1:
                        visited[nx][ny][dir] = cnt + 1
                        queue.append((nx, ny, dir, cnt + 1))
            if check_turn(x,y,dir) and visited[x+1][y-1][0] > cnt + 1:
                if (x+1, y-1) == des and des_dir == 0:
                    return cnt + 1
                queue.append((x+1,y-1,0,cnt+1))
                visited[x+1][y-1][0] = cnt + 1
    return 0
global N
N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[[float('inf'),float('inf')] for _ in range(N)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
tree,des,tree_dir,des_dir = search()
visited[tree[0]][tree[1]][tree_dir] = 1
queue = deque()
queue.append((tree[0],tree[1],tree_dir,0))
# 1 : 세로, 0 : 가로
print(bfs())