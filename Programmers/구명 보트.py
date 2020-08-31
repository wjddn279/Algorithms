def solution(people, limit):
    global histogram
    answer = 0
    histogram = [0 for _ in range(241)]
    for weight in people:
        histogram[weight] += 1
    for weight in people:
        if histogram[weight] > 0:
            check(weight,limit)
            answer += 1
    return answer

def check(num,limit):
    global histogram
    histogram[num] -= 1
    if limit - num < 40:
        return 0
    for i in range(limit-num,39,-1):
        if histogram[i] > 0:
            histogram[i] -= 1
            return 0
    return 0
print(solution([70, 50, 80, 50],100))