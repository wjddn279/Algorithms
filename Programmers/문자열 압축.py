def solution(s):
    total,answer = len(s), len(s)
    for length in range(1,total//2+1):
        stack,temp = [], ""
        for i in range(total//length+1):
            now = s[length * i : length * (i+1)]
            if stack and stack[-1] != now:
                if len(stack) == 1:
                    temp += stack[0]
                else:
                    temp = temp + str(len(stack)) + stack[0]
                stack = []
            stack.append(now)
        if stack:
            if len(stack) == 1:
                temp += stack[0]
            else:
                temp = temp + str(len(stack)) + stack[0]
        answer = min(answer,len(temp))
    return answer


print(solution(
  	"aabbaccc"))

