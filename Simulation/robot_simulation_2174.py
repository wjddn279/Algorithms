import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()


def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= B or y >= A: return False
    else: return True

def crashrobot(num,x,y,dx,dy,val):
    for mul in range(1, val + 1):
        nx, ny = x + mul * dx, y + mul * dy
        if not iswall(nx,ny):
            print('Robot {} crashes into the wall'.format(num + 1))
            return True
        if matrix[nx][ny] != [-1, -1]:
            print('Robot {} crashes into robot {}'.format((num + 1), matrix[nx][ny][0] + 1))
            return True
    return False

global A,B
A, B = map(int,input().split())
N, M = map(int,input().split())
matrix = [[[-1,-1] for _ in range(A)] for _ in range(B)]
locate = [0 for _ in range(N)]
dic = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
turn = {'L':{'E':0,'N':1,'W':2,'S':3,0:'E',1:'N',2:'W',3:'S'},
        'R':{'E':0,'S':1,'W':2,'N':3, 0:'E',1:'S',2:'W',3:'N'}}
for num in range(N):
    x,y,dir = input().split()
    matrix[B-int(y)][int(x)-1] = [num,dir]
    locate[num] = [B-int(y),int(x)-1]
orders = [input().split() for _ in range(M)]
for order in orders:
    num,ord,val = int(order[0])-1,order[1],int(order[2])
    x, y = locate[num][0], locate[num][1]
    dir = matrix[x][y][1]
    if ord == 'F':
        dx,dy = dic[dir]
        nx, ny = x + val * dx, y + val * dy
        if crashrobot(num,x,y,dx,dy,val):
            break
        locate[num] = [nx,ny]
        matrix[x][y],matrix[nx][ny] = [-1,-1],[num,dir]
    else:
        matrix[x][y][1] = turn[ord][(turn[ord][dir]+val)%4]
else:
    print('OK')

