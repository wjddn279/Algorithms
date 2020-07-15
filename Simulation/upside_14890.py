import sys
sys.stdin = open("upside_14890.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
N, L = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = 0

# 행 계산
for i in range(N):
    j = 0
    flag = True
    height = 0
    ladder = [0 for _ in range(N)]
    while flag and j < N-1:
        if matrix[i][j] == matrix[i][j+1]:
            j = j+1
            continue
        elif matrix[i][j] == matrix[i][j+1] +1:
            temp = matrix[i][j+1]
            for k in range(1,L+1):
                if j+k >= N or ladder[j+k] != 0 or temp != matrix[i][j+k]:
                    flag = False
                    break
                else:
                    ladder[j+k] = 1
            else:
                j = j+1
        elif matrix[i][j] == matrix[i][j+1] - 1:
            temp = matrix[i][j]
            for k in range(0,L):
                if j-k < 0 or ladder[j-k] != 0 or temp != matrix[i][j-k]:
                    flag = False
                    break
                else:
                    ladder[j-k] = 1
            else:
                j = j+1
        else:
            flag = False
            break
    if flag:
        result += 1

for i in range(N):
    j = 0
    flag = True
    ladder = [0 for _ in range(N)]
    while flag and j < N-1:
        if matrix[j][i] == matrix[j+1][i]:
            j = j+1
            continue
        elif matrix[j][i] == matrix[j+1][i] +1:
            temp = matrix[j+1][i]
            for k in range(1,L+1):
                if j+k >= N or ladder[j+k] != 0 or temp != matrix[j+k][i]:
                    flag = False
                    break
                else:
                    ladder[j+k] = 1
            else:
                j = j+1
        elif matrix[j][i] == matrix[j+1][i]-1:
            temp = matrix[j][i]
            for k in range(0,L):
                if j-k < 0 or ladder[j-k] != 0 or temp != matrix[j-k][i]:
                    flag = False
                    break
                else:
                    ladder[j-k] = 1
            else:
                j = j+1
        else:
            flag = False
            break
    if flag:
        result += 1
print(result)