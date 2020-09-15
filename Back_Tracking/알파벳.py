import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    else: return True

global N,M
N, M  = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0
stack = [(0,0,1,[matrix[0][0]])]
while stack:
    x,y,cnt,step = stack.pop()
    answer = max(answer,cnt)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if iswall(nx,ny) and matrix[nx][ny] not in step:
            stack.append((nx,ny,cnt+1,step+[matrix[nx][ny]]))

print(answer)
