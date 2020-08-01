# 10시 40분
import sys
sys.stdin = open("new_game2_17839.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N:
        return False
    else:
        return True

def moving(nx,ny,x,y,idx):
    stack = []
    for i in range(len(state[x][y])-1,-1,-1):
        temp = state[x][y].pop()
        stack.append(temp)
        data[temp][0],data[temp][1] = nx,ny
        if temp == idx:
            break
    return stack

def go_white(nx,ny,x,y,idx):
    state[nx][ny] += moving(nx,ny,x,y,idx)[::-1]

def go_red(nx,ny,x,y,idx):
    state[nx][ny] += moving(nx,ny,x,y,idx)

def solve():
    for result in range(1,10):
        for iteration in range(K):
            x,y,d = data[iteration]
            nx,ny = x+dx[d],y+dy[d]
            if iswall(nx,ny) == False or matrix[nx][ny] == 2:
                if d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3 : d = 4
                elif d == 4 : d = 3
                nx,ny = x+dx[d],y+dy[d]
                if iswall(nx, ny) == False or matrix[nx][ny] == 2:
                    data[iteration][2] = d
                    nx,ny = x,y
                elif matrix[nx][ny] == 0:
                    go_white(nx,ny,x,y,iteration)
                    data[iteration][2] = d
                elif matrix[nx][ny] == 1:
                    go_red(nx,ny,x,y,iteration)
                    data[iteration][2] = d
            elif matrix[nx][ny] == 0:
                go_white(nx,ny,x,y,iteration)
            elif matrix[nx][ny] == 1:
                go_red(nx, ny,x, y, iteration)

            if len(state[nx][ny]) >= 4:
                return result
        print(data)
        prin(state)
    return -1
global N,K
N,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
state = [[[] for _ in range(N)] for _ in range(N)]
# data[0] : 0번째 유저의 x,y,d
data = []
for i in range(K):
    x,y,d = map(int,input().split())
    data.append([x-1,y-1,d])
    state[x-1][y-1].append(i)

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
print(solve())