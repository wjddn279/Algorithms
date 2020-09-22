def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a, b = 0 ,0
    while a < len(A) and b < len(B):
        if A[a] >= B[b]:
            b += 1
        else:
            a += 1
            b += 1
            answer += 1
    return answer
print(solution([5,1,3,7],[2,2,6,8]))
