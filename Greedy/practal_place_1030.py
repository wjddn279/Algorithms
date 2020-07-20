import sys
sys.stdin = open("practal_place_1030.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

def solve(iteration,N,k,0,0):
    length = pow(N,iteration)
    x,y = 0,0
    dx = [0,]
    dy = [0,]
    for i in range(3):
        for j in range(3):


s, N, K, R1, R2, C1, C2 = map(int,input().split())
iteration = s//K
matrix = [[0 for _ in range(C1,C2+1)] for _ in range(R1,R2+1)]
prin(matrix)