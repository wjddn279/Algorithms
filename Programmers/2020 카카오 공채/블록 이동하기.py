from _collections import deque


def direct(dir):
    if dir == 0 or dir == 1:
        return (0,1),(2,3)
    else:
        return (2,3),(0,1)

def prin(a):
    for i in a:
        print(*i)
    print()

def solution(board):
    def iswall(x, y, x2, y2):
        if x < 0 or y < 0 or x2 < 0 or y2 < 0:
            return False
        elif x >= len(board) or y >= len(board[0]) or x2 >= len(board) or y2 >= len(board[0]):
            return False
        elif board[x][y] == 1 or board[x2][y2] == 1:
            return False
        else:
            return True

    def cross(x,y):
        if (x,y) == (0,2) or (x,y) == (2,0):
            return (1,1)
        if (x,y) == (0,3) or (x,y) == (3,0):
            return (-1,1)
        if (x,y) == (1,2) or (x,y) == (2,1):
            return (1,-1)
        if (x,y) == (1,3) or (x,y) == (3,1):
            return (-1,-1)

    def inverse(dir):
        if dir == 0:
            return 1
        if dir == 1:
            return 0
        if dir == 2:
            return 3
        if dir == 3:
            return 2
    prin(board)
    N, M = len(board)-1,len(board[0])-1
    answer = float('inf')
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # x, y, 방향
    queue = deque([(0,0,0)])
    # 동 서 남 북
    visited = [[[float('inf') for _ in range(4)] for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[0][0][0] = 0
    while queue:
        x,y,dir = queue.popleft()
        x2,y2 = x+dx[dir],y+dy[dir]
        go, turn = direct(dir)
        for i in go:
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny,nx+dx[dir],ny+dy[dir]) and visited[nx][ny][dir] > visited[x][y][dir] + 1:
                if (nx,ny) == (N,M) or (nx+dx[dir],ny+dy[dir]) == (N,M):
                    answer = min(answer,visited[x][y][dir] + 1)
                queue.append((nx,ny,dir))
                visited[nx][ny][dir] = visited[x][y][dir] + 1
        for i in turn:
            ddx,ddy = cross(dir,i)
            if iswall(x+dx[i],y+dy[i],x+ddx,y+ddy) and visited[x][y][i] > visited[x][y][dir]+1:
                if (x,y) == (N,M) or (x+dx[i],y+dy[i]) == (N,M):
                    answer = min(answer,visited[x][y][dir] + 1)
                queue.append((x,y,i))
                visited[x][y][i] = visited[x][y][dir] + 1
            ddx,ddy = cross(inverse(dir),i)
            if iswall(x2+ddx,y2+ddy,x2+dx[i],y2+dy[i]) and visited[x2+dx[i]][y2+dy[i]][inverse(i)] > visited[x][y][dir] + 1:
                if (x2,y2) == (N,M) or (x2+dx[i],y2+dy[i]) == (N,M):
                    answer = min(answer,visited[x][y][dir] + 1)
                queue.append((x2+dx[i],y2+dy[i],inverse(i)))
                visited[x2 + dx[i]][y2 + dy[i]][inverse(i)] = visited[x][y][dir] + 1
    prin(visited)
    return answer
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution( [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
