import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def search():
    pos = {}
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 'R':
                pos['R'] = [x,y]
                matrix[x][y] = '.'
            if matrix[x][y] == 'B':
                pos['B'] = [x,y]
                matrix[x][y] = '.'
    return pos

def iswall(x,y):
    if x < 0 or y < 0 :return False
    elif x >= N or y >= M: return False
    elif matrix[x][y] != '.': return False
    else: return True

def move():
    queue = deque()
    queue.append((pos['B'][0],pos['B'][1],pos['R'][0],pos['R'][1],0))
    visited[pos['B'][0]][pos['B'][1]][pos['R'][0]][pos['R'][1]] = 1
    while queue:
        x1,y1,x2,y2,cnt = queue.popleft()
        if cnt > 9:
            return -1
        for i in range(4):
            bx,by,rx,ry = x1,y1,x2,y2
            f1, f2 = False, False
            for _ in range(2):
                nbx,nby = bx+dx[i],by+dy[i]
                while iswall(nbx,nby) and not (nbx == rx and nby == ry):
                    bx,by = nbx,nby
                    nbx,nby = bx+dx[i],by+dy[i]
                nrx,nry = rx+dx[i],ry+dy[i]
                while iswall(nrx,nry) and not (nrx == bx and nry == by):
                    rx,ry = nrx,nry
                    nrx,nry = rx+dx[i],ry+dy[i]
                if matrix[nbx][nby] == 'O':
                    f1 = True
                    bx,by = 0,0
                if matrix[nrx][nry] == 'O':
                    f2 = True
                    rx,ry = 0,0
            if not f1:
                if f2:
                    return cnt + 1
                else:
                    if not visited[bx][by][rx][ry]:
                        queue.append((bx,by,rx,ry,cnt+1))
                        visited[bx][by][rx][ry] = 1
    return -1
global N,M,pos
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
pos = search()
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(move())
