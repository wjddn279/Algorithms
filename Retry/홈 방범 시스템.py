import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

T = int(input())

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    elif not matrix[x][y] : return False
    else : return True

def radio(x,y,r):
    r = r-1
    answer = 0
    for idx,i in enumerate(range(x-r,x+r+1)):
        if idx <= r:
            for j in range(y-idx,y+idx+1):
                if iswall(i,j):
                    answer += 1
        else:
            for j in range(y-(2*r-idx),y+(2*r-idx)+1):
                if iswall(i,j):
                    answer += 1
    return answer


for test_case in range(1,T+1):
    global N
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    total = sum([sum(i) for i in matrix])
    answer = -float('inf')
    var = 1
    while True:
        cost = var*var + (var-1)*(var-1)
        if total*M - cost < 0:
            break
        for i in range(N):
            for j in range(N):
                home = radio(i,j,var)
                temp =  M * radio(i,j,var) - cost
                if temp >= 0:
                    answer = max(answer,home)
        var += 1
    print('#{} {}'.format(test_case,answer))