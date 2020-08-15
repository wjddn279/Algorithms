from _collections import deque

# 주식 가격
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    total = len(prices)
    for i in range(total):
        while stack and prices[i] < prices[stack[-1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    while stack:
        temp = stack.pop()
        answer[temp] = total - temp-1
    return answer

# 다리를 지나가는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 1
    total = len(truck_weights)
    queue = deque(truck_weights)
    truck = queue.popleft()
    stack = deque([truck])
    time = deque([1])
    arrive = 0
    while arrive < total:
        iteration = len(time)
        for _ in range(iteration):
            now = time.popleft()
            truck = stack.popleft()
            if now + 1 <= bridge_length:
                time.append(now + 1)
                stack.append(truck)
            else:
                arrive += 1

        if len(queue) != 0 and sum(stack) + queue[0] <= weight:
            stack.append(queue.popleft())
            time.append(1)
        answer += 1

    return answer

# 프린터
def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx,pri in enumerate(priorities):
        queue.append([pri,idx])
    while queue:
        length = len(queue)
        max_value,max_index = 0,-1
        for i in range(length):
            pri,idx = queue.popleft()
            if max_value < pri:
                max_value, max_index = pri, i
            queue.append([pri,idx])
        for _ in range(max_index):
            queue.append(queue.popleft())
        result = queue.popleft()
        answer += 1
        if result[1] == location:
            break
    return answer


print(solution([2, 1, 3, 2],2))

