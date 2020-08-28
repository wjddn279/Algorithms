def solution(lines):
    answer = 0
    data = []
    for line in lines:
        stack = [int(line[11:13]),int(line[14:16]),float(line[17:23])]
        temp = ''
        for i in range(24,100):
            if line[i] == 's':
                break
            else:
                temp += line[i]
        stack.append(float(temp))
        data.append(stack)

    print(data)

    return answer

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))