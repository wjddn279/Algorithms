import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

def isconnected(step):
    stack,vist = [step[0]], [step[0]]
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny]:
                if (nx,ny) not in vist:
                    stack.append((nx,ny))
                    vist.append((nx,ny))
    if len(vist) == 7:
        return True
    else:
        return False


def com(n,k,r,rnd,som,step):
    global answer
    if rnd-som > 4:
        return
    if rnd == r:
        if som < 4:
            return
        else:
            if isconnected(step):
                answer += 1
            return
    if k >= n:
        return
    com(n,k+1,r,rnd,som,step)
    visited[chk[k][0]][chk[k][1]] = 1
    if matrix[chk[k][0]][chk[k][1]] == 'S':
        com(n,k+1,r,rnd+1,som+1,step+[chk[k]])
    else:
        com(n, k + 1, r, rnd + 1, som,step+[chk[k]])
    visited[chk[k][0]][chk[k][1]] = 0


matrix = [list(input()) for _ in range(5)]
chk = [(i,j) for i in range(5) for j in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0
com(25,0,7,0,0,[])
print(answer)