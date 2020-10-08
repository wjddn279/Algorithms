def solution(n):
    answer = 0
    flag = 100
    bit = [0 for _ in range(21)]
    for i in range(20,-1,-1):
        if pow(3,i+1) > n >= 2 * pow(3,i):
            if flag == 100:
                flag = i
            n = n - 2 *pow(3,i)
            bit[i] = 2
        elif 2 * pow(3,i) > n >= pow(3,i):
            if flag == 100:
                flag = i
            n = n -pow(3,i)
            bit[i] = 1
    bit = bit[0:flag+1]
    for idx,num in enumerate(bit[::-1]):
        answer += num * pow(3,idx)
    return answer

print(solution(125))