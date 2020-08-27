import heapq

# 더 맵게
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        answer += 1
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    else:
        return answer

# 디스크 컨트롤러

def solution(jobs):
    answer = 0
    data = [[] for _ in range(1001)]
    for arrive,lasting in jobs:
        data[arrive].append(lasting)
    time,arrive = 0, 0
    waiting = []
    flag = True
    heapq.heapify(waiting)
    while True:
        if flag:
            if time < 1001 and len(data[time]) != 0 :
                # 그 시간에 요청 받은 것들 전부 waiting에 담아
                for content in data[time]:
                    heapq.heappush(waiting,[content,time])
            # 지속 시간, 입장 시간
            if time > arrive:
                if len(waiting) != 0:
                    last,dispatch = heapq.heappop(waiting)
                    arrive = time + last
                    answer = answer + last + time - dispatch
                time += 1
                if time > 1001 and len(waiting) == 0:
                    return answer//len(jobs)

            elif time == arrive:
                if len(waiting) != 0:
                    last,dispatch = heapq.heappop(waiting)
                    arrive = time + last
                    answer = answer + last + time - dispatch
                    if time > 1000:
                        flag = False
                        time += last
                    else:
                        time += 1
                else:
                    if time > 1000:
                        return answer//len(jobs)

                    else:
                        time += 1
            else:
                time += 1
        else:
            if len(waiting) != 0:
                last, dispatch = heapq.heappop(waiting)
                arrive = time + last
                answer = answer + last + time - dispatch
                time += last
            else:
                return answer//len(jobs)


print(solution([[0, 3], [1, 9], [999, 1000],[1000,1000]]))