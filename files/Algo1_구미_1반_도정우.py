import sys
sys.stdin = open("input5.txt")

def func(x,y):
    square = []
    for i in range(3*(x//3) , 3*(x//3)+3):
        for j in range(3*(y//3), 3*(y//3)+3):
            square.append(data[i][j])
    # 점이 포함되는 3*3 sub-matrix의 왼쪽 위 좌표를 구해서 sub-matrix 값을 square 배열에 1차원으로 저장
    col = []
    for i in range(len(data)):
        col.append(data[i][y])
    # 검사할 열의 값을 col 배열에 1차원으로 저장
    return search(square) and search(col) and search(data[x])
    # 행과 열 submatrix의 search값이 True라면 True 반환
T =  int(input())

def search(a):
    for i in range(len(a)):
        val = a[i]
        if val == 0:
            continue
        else:
            for j in range(i+1,len(a)):
                if  a[j] == val:
                    return False
    return True
    # 배열을 순회하면서 0을 제외한 같은 값이 있다면 False를 반환

for test_case in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(9)]
    exam = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        x,y,value = exam[i]
        data[x][y] = value
        if func(x,y):
            cnt += 1
        else:
            break
    print('#{} {}'.format(test_case,cnt))


