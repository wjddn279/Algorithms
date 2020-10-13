import sys
sys.stdin  = open("input.txt")

from itertools import permutations

def rotate(x,y,R):
    for r in range(1,R+1):
        temp = matrix[x-r][y-r]
        for j in range(y-r,y+r):
            new = matrix[x-r][j+1]
            matrix[x-r][j+1] = temp
            temp = new
        for i in range(x-r,x+r):
            new = matrix[i+1][y+r]
            matrix[i+1][y+r] = temp
            temp = new
        for j in range(y+r,y-r,-1):
            new = matrix[x+r][j-1]
            matrix[x+r][j-1] = temp
            temp = new
        for i in range(x+r,x-r,-1):
            new = matrix[i-1][y-r]
            matrix[i-1][y-r] = temp
            temp = new

def cal():
    global answer
    for i in range(len(mat)):
        answer = min(answer,sum(matrix[i]))

N, M, K = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
data = [list(map(int,input().split())) for _ in range(K)]
answer = float('inf')
val = [0 for _ in range(len(mat))]
# r,c,s
for can in permutations(data,len(data)):
    matrix = [i[:] for i in mat]
    for r,c,s in can:
        rotate(r-1,c-1,s)
    cal()
print(answer)