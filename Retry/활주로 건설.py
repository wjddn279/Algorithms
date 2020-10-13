import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

T = int(input())

def transpose(N):
    for i in range(N):
        for j in range(i,N):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

def isgo(arr,X):
    start = 0
    idx = 0
    while idx < len(arr)-1:
        num,next = arr[idx],arr[idx+1]
        if abs(next-num) > 1:
            return False
        # 올라가는거
        elif next-num == 1:
            if idx-start+1 < X:
                return False
            else:
                idx = idx+1
                start = idx
        elif next-num == -1:
            for r in range(X):
                idx += 1
                if idx >= len(arr) or arr[idx] != next:
                    return False
            start = idx+1
        else:
            idx += 1
    return True
#
def solve(N,X,answer):
    for i in range(N):
        if isgo(matrix[i],X):
            answer += 1
    return answer


for test_case in range(1,T+1):
    N, X = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    answer = solve(N,X,0)
    transpose(N)
    answer = solve(N,X,answer)
    print('#{} {}'.format(test_case,answer))
