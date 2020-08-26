def solution(num, tar):
    global answer,numbers,target
    numbers,target,answer = num,tar,0
    solve(len(numbers),0,0)
    return answer

def solve(n,k,now):
    global answer,numbers,target
    if n == k and now == target:
        answer += 1
    elif n != k:
        solve(n,k+1,now+numbers[k])
        solve(n,k+1,now-numbers[k])


print(solution([1, 1, 1, 1, 1],3))