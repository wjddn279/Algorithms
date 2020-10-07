import sys
sys.stdin = open("input.txt")

from _collections import deque

def iswall(x,y):
    if x >= N or y >= N: return False
    elif x < 0 or y < 0: return False
    elif matrix[x][y] == 1: return False
    else: return True

def check(x,y,dir):
    if dir == 2:
        return iswall(x+dx[0],y+dy[0]) and iswall(x+dx[1],y+dy[1]) and iswall(x+dx[2],y+dy[2])
    else:
        return iswall(x+dx[dir],y+dy[dir])

def bfs(x,y):
    global answer
    queue = deque()
    queue.append((x,y,0))
    while queue:
        print(queue)
        x,y,dir = queue.popleft()
        nx,ny = x+dx[dir],y+dy[dir]
        if nx == N-1 and ny == N-1:
            answer += 1
        elif dir == 0:
            for i in [0,2]:
                if check(nx,ny,i):
                    queue.append((nx,ny,i))
        elif dir == 1:
            for i in [1,2]:
                if check(nx,ny,i):
                    queue.append((nx,ny,i))
        elif dir == 2:
            for i in [0,1,2]:
                if check(nx,ny,i) :
                    queue.append((nx,ny,i))

global N,answer
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
# 0 : 오른쪽 1 : 아래 2 : 오른쪽 아래 대각선
dx = [0,1,1]
dy = [1,0,1]
answer = 0
bfs(0,0)
print(answer)