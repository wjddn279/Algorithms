# 5시 15분

import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

T = int(input())

def reverse(d):
    if d == 1 : return 2
    if d == 2 : return 1
    if d == 3 : return 4
    if d == 4 : return 3

def move():
    new = {}
    while data:
        x,y,c,d = data.pop()
        nx,ny = x+dx[d],y+dy[d]
        if matrix[nx][ny]:
            c,d = c//2,reverse(d)
        if c:
            if (nx,ny) not in new:
                new[(nx,ny)] = [c,d,c]
            else:
                if c > new[(nx,ny)][2]:
                    new[(nx,ny)][1] = d
                    new[(nx,ny)][2] = c
                new[(nx,ny)][0] += c
    for key,item in new.items():
        x,y = key
        c,d,_ = item
        data.append((x,y,c,d))

for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                matrix[i][j] = 1
    data = [list(map(int,input().split())) for _ in range(K)]
    for _ in range(M):
        move()
    answer = 0
    for a,b,c,d in data:
        answer += c
    print('#{} {}'.format(test_case,answer))

    # 1 145
    # 2 5507
    # 3 9709
    # 4 2669
    # 5 3684
    # 6 774
    # 7 4797
    # 8 8786
    # 9 1374
    # 10 5040