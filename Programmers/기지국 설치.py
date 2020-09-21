from _collections import deque
import math
def solution(n, stations, w):
    answer = 0
    now = 1
    for station in stations:
        if (station-w) - now > 0:
            answer += math.ceil(((station-w)-now)/(2*w+1))
        now = station + w + 1
        print(now,answer)
    if now < n:
        answer += math.ceil((n-now)/(2*w+1))
    elif now == n:
        answer += 1
    return answer
print(solution(11,[4,11],1))
print(math.ceil(5.6))