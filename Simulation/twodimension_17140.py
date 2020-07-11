import sys
sys.stdin = open("twodimension.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

# R 연산 : 행의 개수 >= 열의 개수 C 연산 : 행의 개수 < 열의 개수
# 정렬 : 각각의 수가 몇번 나왔는지 알기 -> 등장 횟수가 커지는 순으로 -> 수가 커지는 순으로

def solve(x,y,value):
    clone = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    # C < R 이면 행렬 전치
    if len(matrix) >= len(matrix[0]):
        flag = True
    # Symmetric matrix는 기존의 방법으로 전치가 가능하나 anti-symmetry 라면 불가능하므로
    # 새로운 clone 행렬을 만들어서 값만 복사하는 방법으로 처리
    else:
        flag = False
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                clone[i][j] = matrix[j][i]
    result,max_len = [],0
    if flag:
        array = matrix
    else:
        array = clone
    # 딕서너리로 각 값마다 갯수 구하기
    for arr in array:
        dic, stack = {}, []
        for i in arr:
            if i != 0:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        # 딕셔너리 값을 기반으로 stack 배열에 값을 하나씩 집어넣기
        for _ in range(len(dic)):
            min_value, min_key = 999999999, 9999999999
            for key,val in dic.items():
                if val > 0:
                    if val < min_value or (val == min_value and key < min_key) :
                        min_value = val
                        min_key = key
            # 문제조건에 최대 100 이라 했으므로 하드코딩 해줘야함
            if len(stack)<= 100:
                stack.append(min_key)
            if len(stack) <= 100:
                stack.append(min_value)
            dic[min_key] = -1
        if len(stack) > max_len:
            max_len = len(stack)
        if len(result) <= 100:
            result.append(stack)
    # 아닌값 0으로 채워주기
    for i in range(len(result)):
        for _ in range(max_len-len(result[i])):
            result[i].append(0)
    # 전치한거 다시 돌려놓기
    if flag == False:
        clone = [[0 for _ in range(len(result))] for _ in range(len(result[0]))]
        for i in range(len(result[0])):
            for j in range(len(result)):
                clone[i][j] = result[j][i]
        return clone
    else:
        return result

R,C,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(3)]
k = 0
while k < 101:
    # 장난질 요소 중 하나: 무조건 3x3 행렬 안에 있는 값이 시작점이지 않다!!!
    if R-1 >= len(matrix) or C-1 >= len(matrix[0]):
        k += 1
    elif matrix[R-1][C-1] == K:
        break
    else:
        k += 1
    matrix = solve(R,C,K)
if k == 101:
    print(-1)
else:
    print(k)
