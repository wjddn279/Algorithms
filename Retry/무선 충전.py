# 12시 40분

import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

def radio(x,y,c,p,cnt):
    for idx,j in enumerate(range(y-c,y+c+1)):
        if j <= y:
            for i in range(x-idx,x+idx+1):
                if 0 <= i < 10 and 0 <= j < 10:
                    matrix[i][j].append((p,cnt))
                    matrix[i][j].sort(reverse=True)
        else:
            for i in range(x-(2*c-idx),x+(2*c-idx)+1):
                if 0 <= i < 10 and 0 <= j < 10:
                    matrix[i][j].append((p,cnt))
                    matrix[i][j].sort(reverse=True)

T = int(input())
for test_case in range(1,T+1):
    M, K = map(int,input().split())
    path = [[0]+list(map(int,input().split())) for _ in range(2)]
    matrix = [[[] for _ in range(10)] for _ in range(10)]
    dx = [0,-1,0,1,0]
    dy = [0,0,1,0,-1]
    for i in range(K):
        # c: 충전범위 , p: 처리량
        x,y,c,p = map(int,input().split())
        radio(y-1,x-1,c,p,i)
    A = [0 for _ in range(M+1)]
    B = [0 for _ in range(M+1)]
    ax,ay,bx,by = 0,0,9,9
    for i in range(M+1):
        ad,bd = path[0][i],path[1][i]
        nax,nay,nbx,nby = ax+dx[ad],ay+dy[ad],bx+dx[bd],by+dy[bd]
        # 동시에 같은 곳 접속
        if matrix[nax][nay] and matrix[nbx][nby] and matrix[nax][nay][0][1] == matrix[nbx][nby][0][1]:
            if len(matrix[nax][nay]) == 1 and len(matrix[nbx][nby]) == 1:
                A[i] += matrix[nax][nay][0][0]//2
                B[i] += matrix[nbx][nby][0][0]//2
            elif len(matrix[nax][nay]) == 1 and len(matrix[nbx][nby]) > 1:
                A[i] += matrix[nax][nay][0][0]
                B[i] += matrix[nbx][nby][1][0]
            elif len(matrix[nbx][nby]) == 1 and len(matrix[nax][nay]) > 1:
                A[i] += matrix[nax][nay][1][0]
                B[i] += matrix[nbx][nby][0][0]
            else:
                if matrix[nax][nay][1] > matrix[nbx][nby][1]:
                    A[i] += matrix[nax][nay][1][0]
                    B[i] += matrix[nbx][nby][0][0]
                else:
                    A[i] += matrix[nax][nay][0][0]
                    B[i] += matrix[nbx][nby][1][0]
        else:
            if matrix[nax][nay]:
                A[i] += matrix[nax][nay][0][0]
            if matrix[nbx][nby]:
                B[i] += matrix[nbx][nby][0][0]
        ax, ay, bx, by = nax,nay,nbx,nby
    print('#{} {}'.format(test_case,sum(A)+sum(B)))