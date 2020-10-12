import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from itertools import combinations
import copy

def iswall(x,y):
    if x < 0 or y < 0 or y >= M:
        return False
    else:
        return True

def kill(k,l):
    i,j = k-1,l
    for d in range(0,D):
        for idx,y in enumerate(range(l-d,l+d+1)):
            x = i-(d-abs(d-idx))
            if iswall(x,y) and matrix[x][y]:
                if (x,y) not in dead:
                    dead.append((x,y))
                return 0
    return cnt

global N,M,D
N, M, D = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
answer = 0

for can in combinations(list(range(M)),3):
    cnt = 0
    matrix = copy.deepcopy(mat)
    for k in range(N,0,-1):
        dead = []
        for num in can:
            kill(k,num)
        for x,y in dead:
            matrix[x][y] = 0
        cnt += len(dead)
    answer = max(answer,cnt)
print(answer)
