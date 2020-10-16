# 3시 00분

import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from itertools import combinations

T = int(input())

def powerset(n,k,step):
    global val
    if n == k:
        val.append(step)
        return
    powerset(n,k+1,step+[0])
    powerset(n,k+1,step+[1])

def check(can):
    global val,mat
    mat = [i[:] for i in matrix]
    for t in val:
        for idx,i in enumerate(can):
            for j in range(M):
                mat[i][j] = t[idx]
        for j in range(M):
            if not test(mat,j):
                break
        else:
            return True
    return False

def test(mat,j):
    stack,total = [], 0
    for i in range(N):
        num = mat[i][j]
        if len(stack) >= K:
            return True
        if not stack:
            stack.append(num)
        else:
            if stack[-1] == num:
                stack.append(num)
            else:
                stack = [num]
    if len(stack) >= K:
        return True
    else:
        return False

def solve(test_case):
    global val
    for i in range(K):
        val = []
        powerset(i, 0, [])
        for can in combinations(arr,i):
            if check(can):
                print('#{} {}'.format(test_case,i))
                return
    print('#{} {}'.format(test_case,K))


for test_case in range(1,T+1):
    global N,M,K
    N,M,K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    arr = list(range(N))
    solve(test_case)
