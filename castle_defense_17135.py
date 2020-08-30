import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()


from itertools import combinations

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M: return False
    else: return True

def search(num,rnd):

    for i in range(0,D):
        for idx,y in enumerate(range(num-i,num+i+1)):
            x = rnd-1-i+abs(idx-i)
            if iswall(x,y) and matrix[x][y] == 1 and visited[x][y] == 0:
                return [x,y]

    return 0

global N,M,D
N, M, D = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
matrix.append([0 for _ in range(M)])
result = 0

combination = combinations(range(M),3)
for comb in combination:
    visited =[[0 for _ in range(M)] for _ in range(N)]
    temp = 0
    for rnd in range(N,0,-1):
        target = [0,0,0]
        for idx,num in enumerate(comb):
            target[idx] = search(num,rnd)
        for tar in target:
            if tar != 0 and visited[tar[0]][tar[1]] == 0:
                visited[tar[0]][tar[1]] = 1
                temp += 1
    result = max(result,temp)

print(result)
