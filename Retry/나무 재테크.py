import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 :return False
    elif x >= N or y >= N: return False
    else: return True

def spring():
    death, new = {}, []
    # 봄
    for x in range(N):
        for y in range(N):
            if matrix[x][y]:
                next = deque()
                it = len(matrix[x][y])
                for i in range(it):
                    age = matrix[x][y][i]
                    if age <= energy[x][y]:
                        next.append(age+1)
                        energy[x][y] -= age
                        if (age+1)%5 == 0:
                            new.append((x,y))
                    else:
                        death[(x, y)] = list(matrix[x][y])[i:it]
                        break
                matrix[x][y] = next
    # 여름
    for pos,arr in death.items():
        x,y = pos
        for num in arr:
            energy[x][y] += num//2
    # 가을
    while new:
        x,y = new.pop()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                matrix[nx][ny].appendleft(1)
    # 겨울
    for x in range(N):
        for y in range(N):
            energy[x][y] += A[x][y]

def out():
    result = 0
    for i in range(N):
        for j in range(N):
            result += len(matrix[i][j])
    return result
global N
N, M, K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
matrix = [[deque() for _ in range(N)] for _ in range(N)]
energy = [[5 for _ in range(N)] for _ in range(N)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(M):
    x,y,e = map(int,input().split())
    matrix[x-1][y-1].append(e)
for _ in range(K):
    spring()
print(out())