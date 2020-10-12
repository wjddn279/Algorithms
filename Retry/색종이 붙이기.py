import sys
sys.stdin = open("input.txt")


def search():
    for i in range(10):
        for j in range(10):
            if matrix[i][j]:
                return (i,j)
    return (-1,-1)
def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= 10 or y >= 10 : return False
    else : return True

def isconnect(x,y,d):
    for i in range(x,x+d):
        for j in range(y,y+d):
            if not iswall(i,j) or not matrix[i][j]:
                return False
    return True

def destroy(x,y,d):
    for i in range(x,x+d):
        for j in range(y,y+d):
            matrix[i][j] = 0

def recover(x,y,d):
    for i in range(x,x+d):
        for j in range(y,y+d):
            matrix[i][j] = 1

def sol(cnt):
    global answer
    x,y = search()
    if x == -1 and y == -1:
        answer = min(answer,cnt)
        return
    for i in range(1,6):
        if isconnect(x,y,i) and fre[i] >= 1:
            fre[i] -= 1
            destroy(x,y,i)
            sol(cnt+1)
            recover(x,y,i)
            fre[i] += 1
global answer
matrix = [list(map(int,input().split())) for _ in range(10)]
block = [(i,j) for i in range(10) for j in range(10) if matrix[i][j]]
fre = [5 for _ in range(6)]
answer = float('inf')
sol(0)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
