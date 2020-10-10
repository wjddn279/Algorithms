import sys
sys.stdin = open("input.txt")

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= 5 or y >= 5 : return False
    else: return True

def isconnect(x,arr):
    if not arr:
        return True
    for i in range(4):
        nx,ny = x[0]+dx[i],x[1]+dy[i]
        if (nx,ny) in arr:
            return True
    return False

def comb(n,k,r,step,num):
    print(n,k,r,step,num)
    if k == r:
        if num >= 5:
            answer += 1
        return
    if k >= n:
        return
    if isconnect(mapping[k],step):
        if matrix[mapping[k][0]][mapping[k][1]] == 'S':
            comb(n,k+1,r,step+[mapping[k]],num+1)
        else:
            comb(n,k+1,r,step+[mapping[k]],num)
    comb(n,k+1,r,step,num)

global answer
matrix = [list(input()) for _ in range(5)]
mapping = [(i,j) for i in range(5) for j in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0
print(mapping)
comb(25,0,7,[],0)
print(answer)
