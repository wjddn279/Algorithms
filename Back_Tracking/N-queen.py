import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()



def rec(c):
    global answer,N
    if c == N:
        answer += 1
        return
    for r in range(N):
        queen[c] = r
        if isvalid(c):
            rec(c+1)

def isvalid(c):
    for i in range(c):
        if queen[c] == queen[i] or abs(queen[c]-queen[i]) == c-i:
            return False
    return True

global answer, N
N = int(input())
queen = [0 for _ in range(N)]
answer = 0
rec(0)
print(answer)