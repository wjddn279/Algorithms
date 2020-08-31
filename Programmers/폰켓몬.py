def solution(nums):
    now,total = len(set(nums)), len(nums)
    if now > total//2:
        answer = total//2
    else:
        answer = now
    return answer

print(solution([3,3,3,2,2,4]))