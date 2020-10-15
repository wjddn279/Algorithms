# 1시 45분

import sys
sys.stdin = open("input.txt")

from _collections import deque

T = int(input())

def powerset(n,k,step):
    if n == k:
        can.append(step)
        return
    powerset(n,k+1,step+[0])
    powerset(n,k+1,step+[1])

def distance(t1,t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

def move(t1,t2,answer):
    # t1 : 0 번째 계단으로 가는 애들 , t2 : 1번째 계단으로 가는 유저
    onstair1, onstair2 = deque(), deque()
    wait1,wait2 = deque(),deque()
    len1, len2 = stair[0][2],stair[1][2]
    dis = []
    for x,y in t1:
        dis.append((distance((x,y),stair[0]),x,y,0))
    for x,y in t2:
        dis.append((distance((x,y),stair[1]),x,y,1))
    dis.sort()
    dis = deque(dis)
    # 거리, 위치, 목표물
    time = 0
    # print(time)
    # print(dis, wait1, wait2, onstair1, onstair2)
    while dis or wait1 or wait2 or onstair1 or onstair2:
        if time == answer:
            return answer
        time += 1
        # 시간 다된 사람들 내려 0 -> 끝나는 시간
        while onstair1 and onstair1[0][0] <= time:
            onstair1.popleft()
        while onstair2 and onstair2[0][0] <= time:
            onstair2.popleft()
        # 대기자들 올라가 # 타는 시간
        while wait1 and wait1[0][0] <= time:
            if len(onstair1) < 3:
                now,index = wait1.popleft()
                onstair1.append((time+len1,index))
            else:
                break
        while wait2 and wait2[0][0] <= time:
            if len(onstair2) < 3:
                now,index = wait2.popleft()
                onstair2.append((time+len2,index))
            else:
                break
        # 도착자들
        while dis and dis[0][0] <= time:
            d,x,y,t = dis.popleft()
            # stair1
            if t == 0:
                wait1.append((d+1,(x,y)))
            else:
                wait2.append((d+1,(x,y)))
    return min(answer,time)

for test_case in range(1,T+1):

    # 계단을 내려가는 시간
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    user,stair = [], []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 1:
                stair.append((i,j,matrix[i][j]))
            if matrix[i][j] == 1:
                user.append((i,j))
    can = []
    powerset(len(user),0,[])
    answer = float('inf')
    for target in can:
        t1,t2 = [] , []
        for idx,num in enumerate(target):
            if num == 0:
                t1.append(user[idx])
            else:
                t2.append(user[idx])
        answer = move(t1,t2,answer)
    print('#{} {}'.format(test_case,answer))
