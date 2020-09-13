def solution(boxes):
    cnt,answer = {}, len(boxes)
    for box in boxes:
        for num in box:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
    for val in cnt.values():
        answer -= val//2
    return answer

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))