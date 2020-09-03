def solution(N, stages):
    fail = [0 for _ in range(N+2)]
    arrive = [0 for _ in range(N+2)]
    result, answer = [], []
    total = len(stages)
    for stage in stages:
        fail[stage] += 1
    for i in range(1,N+1):
        arrive[i] = total
        total -= fail[i]
    for i in range(1,N+1):
        if arrive[i] == 0:
            result.append([0,-i])
        else:
            result.append([fail[i]/arrive[i],-i])
    result.sort(reverse=True)
    for x,y in result:
        answer.append(-y)
    return answer
print(solution(7,[2, 1, 2 ,6, 2, 4, 3, 3]))