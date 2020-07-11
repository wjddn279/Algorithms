import sys
sys.stdin = open("input6.txt")

def Per(n,k,r,sum):
    if sum < -9999:
        return
    if k == r:
        b.append(a[0:r])
        max_sum = sum
    else:
        for i in range(k,n):
            a[k], a[i] = a[i], a[k]
            sum += a[k]
            Per(n,k+1,r,sum)
            a[k], a[i] = a[i], a[k]

    # nPr 순열 구현

T = int(input())
for test_case in range(1,T+1):
    global max_sum
    max_sum = -9999
    b, c = [], []
    N, M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    a = list(range(1,M+1))
    if N <= M:
        Per(M,0,N)
    else:
        Per(M,0,M)
    # 사탕 숫자보다 아이들 수가 많다면 사탕 숫자를 기준, 사탕 숫자가 많다면 사탕 숫자 기준
    # b에 순열의 경우의 수를 담는다.
    max_value = -999999
    for can in b:
        k = [[0 for _ in range(M+1)] for _ in range(N)]
        for i in range(N):
            for j in range(1,data[i][0]+1):
                k[i][data[i][j]] += 1
        # 각 순열의 경우의 수 마다 기존의 아이들이 가지고 있던 사탕 갯수 새로 저장
        for i in range(len(can)):
            k[i][can[i]] += 1
        cnt = 0
        # 순열의 위치 마다 새로 받는 사탕 갯수 더해줌
        for i in range(M+1):
            for j in range(N):
                if k[j][i] != 0:
                    cnt += 1
        # 아이들이 가지고 있는 사탕 종류 계산
        if cnt > max_value:
            max_value = cnt
        # 최대값 계산

    print('#{} {}'.format(test_case,max_value))






    # for i in range(N):
    #     dic = {}
    #     for j in range(1,data[i][0]+1):
    #         dic[data[i][j]] = dic.get(data[i][j], 0)+1
    #     c.append(dic)
    # a = list(range(1,M+1))
    # Per(M,0,N)
    # for can in b:
    #     arr = []
    #     for dics in c:
    #         k = dics
    #         arr.append(k)
    #     result = 0
    #     for i in range(len(can)):
    #         if can[i] not in arr[i]:
    #             arr[i][can[i]] = 1
    #     for i in arr:
    #         result += len(arr)
    # print(d)