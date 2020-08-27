

def solution(array, commands):
    answer = []
    for start,end,idx in commands:
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[idx-1])

    return answer

def solution(numbers):
    answer = ""
    arr = []
    for idx,number in enumerate(numbers):
        temp = list(map(int,str(number)))
        temp = temp * (12//len(temp))
        temp.append(idx)
        arr.append(temp)
    arr.sort(reverse=True)
    for k in arr:
        answer += str(numbers[k[12]])
    return str(int(answer))

def solution(citations):
    citations.sort(reverse=True)
    for answer in range(len(citations),-1,-1):
        for idx,cit in enumerate(citations):
            if answer <= cit:
                if idx+1 >= answer:
                    return answer
            else:
                break


print(solution( [31, 66]))