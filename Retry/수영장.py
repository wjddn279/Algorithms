# 6시 30분

import sys
sys.stdin = open("input.txt")

T = int(input())

def prin(a):
    for i in a:
        print(i)
    print()

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else : return True

def check(step):
    for x,y in step:
        if visited[x][y]:
            return False
    return True

def modify(step,a):
    for x,y in step:
        visited[x][y] = a

def pos_honey(bee):
    a = [matrix[x][y] for x,y in bee]
    a.sort(reverse=True)
    return a

def combination(n,k,r,step):
    if len(step) == r:
        can.append(step)
        return
    if k == n:
        return
    combination(n,k+1,r,step)
    if check(bee[k]):
        modify(bee[k],1)
        combination(n,k+1,r,step+[pos_honey(bee[k])])
        modify(bee[k],0)

def powerset(n,k,s,t,c):
    global sub_sum
    if s > c:
        return
    if n == k :
        if sub_sum < t:
            sub_sum = t
        return
    powerset(n,k+1,s,t,c)
    for num in brr:
        powerset(n,k+1,s+num,t+num*num,c)

for test_case in range(1,T+1):
    global N
    N,M,C = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    bee = []
    for i in range(N):
        for j in range(N-M+1):
            temp = []
            for m in range(M):
                temp.append((i,j+m))
            bee.append(temp)
    can = []
    combination(len(bee),0,2,[])
    answer = 0
    for arr in can:
        temp = 0
        for brr in arr:
            sub_sum = 0
            powerset(len(brr),0,0,0,C)
            temp += sub_sum
        answer = max(temp,answer)
    print('#{} {}' .format(test_case,answer))