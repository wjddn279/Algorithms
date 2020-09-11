from _collections import deque

def solution(cacheSize, cities):
    answer = 0
    heap = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city not in heap:
            # 앞에꺼가 제일 나중에 사용 뒤에꺼가 최신
            if len(heap) >= cacheSize:
                heap.popleft()
                heap.append(city)
            else:
                heap.append(city)
            answer += 5
        # queue 안에 있다는 거니까 최신으로 바꿔 줘야함
        else:
            heap.remove(city)
            heap.append(city)
            answer += 1
    return answer

print(solution(
  	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))