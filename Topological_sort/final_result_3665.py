import sys
sys.stdin = open("final_result_3665.txt")


T = int(input())

def cycle(k,target):
    if flag[0]:
        return
    for i in data[k]:
        if i == target:
            flag[0] = True
            return
        else:
            cycle(i,target)

for _ in range(T):
    # N : 팀 갯수, prior : 작년  팀 순위
    # M : 변경 정보 갯수 , data : 바뀐 순위
    N = int(input())
    prior = list(map(int,input().split()))
    ranking = [0 for _ in range(N+1)]
    # ranking : i 의 작년 순위
    for i in range(len(prior)):
        ranking[prior[i]] = i+1
    M = int(input())
    # x는 y의 원래는 뒤에 있었는데 앞으로 가야한다.
    data = [[] for _ in range(N+1)]
    for i in range(M):
        x,y = map(int,input().split())
        data[x].append(y)
    flag = [False]
    for i in range(1,N+1):
        cycle(i,i)
        if flag[0]:
            break
    if flag[0]:
        print('IMPOSSIBLE')
