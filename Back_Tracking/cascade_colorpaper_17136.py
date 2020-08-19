import sys
sys.stdin = open("input.txt")


def Check(i, j, m):
    for x in range(i, i + m):
        for y in range(j, j + m):
            if matrix[x][y] == 0:
                return False
    return True

def MakeReverse(i, j, m, a):
    for x in range(i, i + m):
        for y in range(j, j + m):
            matrix[x][y] = a


def solve(a):
    if sum(frequency) >= result[0]:
        return
    for i in range(a,10):
        for j in range(10):
            if matrix[i][j] == 1:
                for k in range(5,0,-1):
                    if i < 11-k and j < 11-k and frequency[k] < 5:
                        if Check(i, j, k):
                            MakeReverse(i, j, k, 0)
                            frequency[k] += 1
                            solve(i)
                            frequency[k] -= 1
                            MakeReverse(i, j, k, 1)
                return
    result[0] = min(result[0],sum(frequency))

matrix = [list(map(int,input().split())) for _ in range(10)]
frequency = [0 for _ in range(6)]
result = [987654321]
solve(0)
if result[0] == 987654321:
    print(-1)
else:
    print(result[0])


