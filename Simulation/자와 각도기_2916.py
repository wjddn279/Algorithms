import sys
sys.stdin = open("input.txt")

def sol(ang):
    if angle[ang]:
        return
    angle[ang] = 1
    for num in start:
        if 0 <= ang-num < 360:
            sol(ang-num)
        elif ang-num < 0:
            sol(360+(ang-num))
        else:
            sol((ang-num)-360)
        if 0 <= ang + num < 360:
            sol(ang+num)
        elif ang+num < 0:
            sol(360+(ang+num))
        else:
            sol((ang+num)-360)

N, M = map(int,input().split())
start = list(map(int,input().split()))
target = list(map(int,input().split()))
angle = [0 for _ in range(361)]
for num in start:
    sol(num)
for num in target:
    if angle[num]:
        print('YES')
    else:
        print('NO')
